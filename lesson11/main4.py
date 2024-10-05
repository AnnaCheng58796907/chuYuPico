#!usr/bin/micorpython
'''
led->GPIO 15
光敏電阻->GPIO 25
可變電阻->GPIO 26
內建溫度sensor->ADC最後1Pin,共5個Pin

'''

import tools
from machine import ADC, Timer, Pin, PWM, RTC


def do_thing(t):
    '''
    :param t:Timer的實體
    負責溫度和光線

    '''
    
    temperature_value = adc.read_u16()
    temperature = 27 - ((temperature_value*conversion_factor)-0.706)/0.001721
    print(f'溫度:{temperature}')
    adc_value = adc_light.read_u16()
    print(f'光線:{adc_value}')


def do_thing1(t):
    '''
    :param t:Timer的實體
    負責可變電阻和改變led的亮度

    '''
    adc1 = ADC(Pin(26))
    duty = adc1.read_u16()
    pwm.duty_u16(duty)
    print(f"可變電阻{round(duty/65535*10)}")
    
    
def main():
    try:
        tools.connect()
    except RuntimeError as e:
        print(e)
    except Exception:
        print('不知名錯誤')
    else:
        tim1 = Timer(period=2000, callback=do_thing)
        tim2 = Timer(period=500,callback=do_thing1)


if __name__ == '__main__':

    adc = ADC(4)#內建溫度
    adc1 = ADC(Pin(26))#可變電阻
    adc_light = ADC(Pin(28))#光敏電阻
    pwm = PWM(Pin(15),freq=50)#pwm len
    conversion_factor = 3.3/(65535)
    rtc = RTC()
    main()


