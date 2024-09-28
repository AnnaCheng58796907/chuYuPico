from machine import ADC, Timer, Pin

adc = ADC(4)
conversion_factor = 3.3/(65535)

def do_thing(t):
    temperature_value = adc.read_u16()
    temperature = 27 - ((temperature_value*conversion_factor)-0.706)/0.001721
    print(temperature)

def do_thing1(t):
    adc1 = ADC(Pin(26))
    duty = adc1.read_u16()
    print(f"可變電阻{round(duty/65536*10)}")

tim1 = Timer(period=2000, callback=do_thing)
tim2 = Timer(period=500,callback=do_thing1)
