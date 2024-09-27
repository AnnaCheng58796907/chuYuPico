import machine
import time

adc = machine.ADC(4)
conversion_factor = 3.3/(65535)
while True:
    temperature_value = adc.read_u16()
    temperature = 27 - ((temperature_value*conversion_factor)-0.706)/0.001721
    print(temperature)
    time.sleep(2)