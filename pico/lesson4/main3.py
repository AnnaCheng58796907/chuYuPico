from machine import Timer, Pin

green_led = Pin('LED', Pin.OUT)

count = 0
def green_led_mycallback(t:Timer):
    global count
    count += 1
    green_led.toggle()
    if count >=10 :
        t.deinit()
        
green_led_timer = Timer(period=1000, mode=Timer.PERIODIC, callback=green_led_mycallback)