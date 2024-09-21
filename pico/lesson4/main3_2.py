from machine import Timer, Pin

green_led = Pin('LED', Pin.OUT)

green_count = 0
def green_led_mycallback(t:Timer):
    global green_count
    green_count += 1
    green_led.toggle()
    print(f'green_led執行第{green_count}次')
    if green_count >=10 :
        t.deinit()
        
green_led_timer = Timer(period=1000, mode=Timer.PERIODIC, callback=green_led_mycallback)

red_led = Pin(15, Pin.OUT)
red_count = 0
def red_led_mycallback(t:Timer):
    global red_count
    red_count += 1
    red_led.toggle()
    print(f'red_led執行第{red_count}次')
    if red_count >=10 :
        t.deinit()
        
red_led_timer = Timer(period=2000, mode=Timer.PERIODIC, callback=red_led_mycallback)