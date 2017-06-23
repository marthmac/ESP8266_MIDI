import sys, getopt
import time
import serial

verbose = 0

def writeFileToESP8266( serPort, pathToFile, fileToWrite, echo ):
    fname = pathToFile + fileToWrite
    f = open(fname, 'r')

    if echo:
        print "Writing " + fname + " to ESP8266"

    serPort.write("file.open(\"" + fileToWrite + "\", \"w+\")\n")
    sent =  serPort.readline()
    if verbose:
        print sent

    while True:
        line = f.readline()

        if line == "":
            break

        if line != '\n':
            line = line.rstrip('\n')
            line = "file.writeline(\""+line+"\")"
            #print line
            serPort.write(line + "\n")
            sent =  serPort.readline()
            sent.rstrip('\n')
            if verbose:
                print sent

        time.sleep(20.0/1000.0)

    serPort.write("file.close()\n")
    sent =  serPort.readline()

    f.close()

    return

def listAllFilesOnESP8266( serPort, echo ):
    filesRead = []

    if echo:
        print "\nReading files on ESP8266:"

    serPort.write("l = file.list();\n")
    sent = serPort.readline()
    serPort.write("for k,v in pairs(l) do\n")
    sent = serPort.readline()
    serPort.write("print(k)\n")
    sent = serPort.readline()
    serPort.write("end\n")
    sent = serPort.readline()


    sent = ""

    while True:
        start = time.time()

        sent = serPort.readline()
        sent = sent.rstrip('\n')
        sent = sent.rstrip('\r')

        if sent == "> ":
            break

        filesRead.append(sent)
        # print sent

        end = time.time()

        if ((end - start) > 0.5):
            break

    numFilesRead = len(filesRead)

    if echo:
        for fileRead in filesRead:
            print fileRead
        print ""

    return filesRead, numFilesRead

def eraseFileFromESP8266( serPort, fileToErase, echo ):

    if echo:
        print "Erasing " + fileToErase + " from ESP8266"

    serPort.write("file.remove(\"" + fileToErase + "\")\n")
    sent = serPort.readline()
    # print sent

    return

def clearESP8266( serPort, echo ):

    [filesToErase, numFiles] = listAllFilesOnESP8266( serPort, 0 )

    if echo:
        print "Erasing all files from ESP8266"

    for fileToErase in filesToErase:
        eraseFileFromESP8266( serPort, fileToErase, echo )

    return

def resetESP8266( serPort, echo ):
    serPort.write("node.restart()\n")
    sent = serPort.readline()

    if echo:
        print "Restarting ESP8266"

    return
