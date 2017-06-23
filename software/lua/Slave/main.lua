require 'config'
require 'led'

-- print('main loop entered')
clrLED()

uart.on('data', 0,
  function(data)
    udpSocket:send(udpPort, masterIPcfg.ip, data)
    -- sk:send(data)
    toggleLED()
end, 0)

function checkWiFi ()
  status = wifi.sta.status()

  if status ~= 5 then
    tmr.stop(1)
    dofile('connectToWiFi.lua')
  end

end

function mainLoop ()
  checkWiFi()
end

-- do mainLoop every second
tmr.alarm(1, 1000, 1, mainLoop)
