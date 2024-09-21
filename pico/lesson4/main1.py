from machine import Pin

led = Pin('LED', Pin.OUT)
led.on() #value(1)
led.off() #value(0)
#led.value(1) #0=off, 1=on