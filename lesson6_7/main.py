import tools
from machine import ADC, Timer, Pin, PWM, RTC

tools.connect()
adc = ADC(4)
pwm = PWM(Pin(15),freq=50)
conversion_factor = 3.3/(65535)
rtc = RTC()

def do_thing(t):
    temperature_value = adc.read_u16()
    temperature = 27 - ((temperature_value*conversion_factor)-0.706)/0.001721
    year, month,day, weekly, hours, minutes, seconds, info = rtc.datetime()
    datetime_str = f"{year}-{month}-{day} {hours}:{minutes}:{seconds}"
    print(datetime_str)
    print(temperature)

def do_thing1(t):
    adc1 = ADC(Pin(26))
    duty = adc1.read_u16()
    pwm.duty_u16(duty)
    print(f"可變電阻{round(duty/65535*10)}")

tim1 = Timer(period=2000, callback=do_thing)
tim2 = Timer(period=500,callback=do_thing1)




