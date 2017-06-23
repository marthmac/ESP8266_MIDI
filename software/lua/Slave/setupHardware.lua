require 'config'
require 'led'

setupLED()
uart.setup(0, 31250, 8, 0, 1, 0)

-- print('Hardware Setup Complete!')
