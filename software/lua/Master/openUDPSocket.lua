require 'config'

udpSocket = net.createUDPSocket()
udpSocket:listen(udpPort)
udpSocket:on('receive', function(s, data, port, ip)
	dataString = string.format('%s', data)
	for i = 1, #dataString do
		a = dataString:byte(i)
		n = tonumber(a)
		if pcall(uart.write, 0, n) then
		else
			-- do nothing
			-- print('uart.write() error')
		end
	end
	toggleLED()
end)

-- print('UDPSocket Open!')
