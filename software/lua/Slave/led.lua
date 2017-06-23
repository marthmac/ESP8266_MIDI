require 'config'

local value = gpio.HIGH

function setupLED ()
  -- Configure ledPin as out
  gpio.mode(ledPin, gpio.OUTPUT)
end

function toggleLED ()
  if value == gpio.LOW then
    value = gpio.HIGH
  else
    value = gpio.LOW
  end

  gpio.write(ledPin, value)
end

function setLED()
  gpio.write(ledPin, gpio.LOW)
end

function clrLED()
  gpio.write(ledPin, gpio.HIGH)
end
