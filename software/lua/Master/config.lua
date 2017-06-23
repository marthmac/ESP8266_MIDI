-- WIFI
id = 1 -->'drumKit'

ssid = 'ESP8266_MASTER'
password = 'enterthevoid'
auth = wifi.WPA_PSK

masterIPcfg =
{
    ip='192.168.1.1',
    netmask='255.255.255.0',
    gateway='192.168.1.1'
}

udpPort = 5000

-- HARDWARE
ledPin = 4            --> GPIO2


-- SOFTWARE
