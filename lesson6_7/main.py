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
    duty = adc1.read_u16()from machine import Timer,ADC,Pin,PWM,RTC
def do_thing(t):
    '''
    處理溫度和光線
    '''
    reading = adc.read_u16() * conversion_factor
    temperature = 27 - (reading - 0.706)/0.001721
    print(f'溫度:{temperature}')
    light_value = adc_light.read_u16()
    print(f'光線:{light_value}')
    
    
def do_thing1(t):
    '''
    處理可變電阻
    '''
    adc1 = ADC(Pin(26))
    duty = adc1.read_u16()
    pwm.duty_u16(duty)    
    print(f'可變電阻:{round(duty/65535*10)}')
    
def main():
    t1 = Timer(period=1000, mode=Timer.PERIODIC, callback=do_thing)
    t2 = Timer(period=500, mode=Timer.PERIODIC, callback=do_thing1)
    
if __name__ == "__main__":
    #pico_連結電腦時的寫法,要用connect
    try:
        tools.connect()
    except RuntimeError as e:
        print(f"{{e}")
    else:
        #sensor setup
        adc = ADC(4) #內建溫度感測器
        adc_light = ADC(Pin(28)) #光線感測器
        pwm = PWM(Pin(15),freq=50) #可變電阻
        conversion_factor = 3.3 / (65535) #電壓轉換率    
        main()
    pwm.duty_u16(duty)
    print(f"可變電阻{round(duty/65535*10)}")

tim1 = Timer(period=2000, callback=do_thing)
tim2 = Timer(period=500,callback=do_thing1)




