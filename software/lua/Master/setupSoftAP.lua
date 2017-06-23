require 'config'

cfg={}
cfg.ssid = ssid
cfg.pwd = password
cfg.auth = auth


wifi.ap.config(cfg)
wifi.ap.setip(masterIPcfg)
wifi.setmode(wifi.SOFTAP)

wifi.eventmon.register(wifi.eventmon.STA_CONNECTED, function() print('station connected!') end)

-- print('SoftAP Setup Complete!')
