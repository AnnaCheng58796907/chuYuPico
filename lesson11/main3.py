import network
import time
import rp2
from machine import WDT


rp2.country('TW')
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect('A590301', 'A590301AA')
 
# Wait for connect or fail
max_wait = 10
while max_wait > 0:
    if wlan.status() < 0 or wlan.status() >= 3:
        break
    max_wait -= 1
    print('waiting for connection...')
    time.sleep(1)
 
# Handle connection error
if wlan.status() != 3:
    raise RuntimeError('network connection failed')
    #取得目前日期

    #wdt = WDT(timeout=2000)
    #wdt.feed()
else:
    print('connected')
    status = wlan.ifconfig()
    print( 'ip = ' + status[0] )
    
