#!usr/bin/micorpython
'''
led->GPIO 15
光敏電阻->GPIO 25
可變電阻->GPIO 26
內建溫度sensor->ADC最後1Pin,共5個Pin

'''

import tools
from machine import ADC, Timer, Pin, PWM, RTC
import binascii
from umqtt.simple import MQTTClient

def do_thing(t):
    '''
    :param t:Timer的實體
    負責溫度和光線

    '''
    
    temperature_value = adc.read_u16()
    temperature = 27 - ((temperature_value*conversion_factor)-0.706)/0.001721
    print(f'溫度:{temperature}')
    mqtt.publish('SA-56/TEMPERATURE', f'{temperature}')
    adc_value = adc_light.read_u16()
    print(f'光線:{adc_value}')
    mqtt.publish('SA-56/LINE_LEVEL', f'{adc_value}')


def do_thing1(t):
    '''
    :param t:Timer的實體
    負責可變電阻和改變led的亮度

    '''
    adc1 = ADC(Pin(26))
    duty = adc1.read_u16()
    pwm.duty_u16(duty)
    led_level = round(duty/65535*10)
    print(f"可變電阻{led_level}")
    mqtt.publish('SA-56/LED_LEVEL', f'{led_level}')
    
    
def main():
    pass


if __name__ == '__main__':

    adc = ADC(4)#內建溫度
    adc1 = ADC(Pin(26))#可變電阻
    adc_light = ADC(Pin(28))#光敏電阻
    pwm = PWM(Pin(15),freq=50)#pwm len
    conversion_factor = 3.3/(65535)
    rtc = RTC()
    #連線internet

    try:
        tools.connect()
    except RuntimeError as e:
        print(e)
    except Exception:
        print('不知名錯誤')
    else:
        #MQTT
        SERVER = "192.168.0.252"
        CLIENT_ID = binascii.hexlify(machine.unique_id())
        mqtt = MQTTClient(CLIENT_ID, SERVER, user='pi', password='raspberry')
        mqtt.connect()
        tim1 = Timer(period=2000, callback=do_thing)
        tim2 = Timer(period=500,callback=do_thing1)
    
    main()


