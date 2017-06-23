-- Config
require 'config'

-- Functions
function printStatus()
	status = wifi.sta.status()
	toggleLED()

	if status == 5 then
		connected = 1
		tmr.stop(2)
		tmr.stop(1)
		-- print('connected to wifi')
		-- print('attempting to connect to UDP socket...')
		dofile('connectToUDPSocket.lua')
	else
		connected = 2
		-- print('not connected to wifi')
	end
end

cfg={}
cfg.ssid = ssid
cfg.pwd = password

-- Script
wifi.setmode(wifi.STATION)
wifi.sta.config(cfg)
wifi.sta.connect()

-- print('')
-- print('attempting to connect to:')
-- print(ssid)
-- print('')

connected = 0

-- call printStatus() at 100ms to check if connected to WiFi
tmr.alarm(2, 100, 1, printStatus)
