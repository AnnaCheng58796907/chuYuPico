import time
import binascii
import machine
from umqtt.simple import MQTTClient


# Default MQTT server to connect to
SERVER = "192.168.0.252"
CLIENT_ID = binascii.hexlify(machine.unique_id())
TOPIC = b"SA-56/雞舍"


def main(server=SERVER):
    c = MQTTClient(CLIENT_ID, server)
    c.connect()
    print("Connected to %s, waiting for button presses" % server)
    while True:
        while True:
            if button.value() == 0:
                break
            time.sleep_ms(20)
        print("Button pressed")
        c.publish(TOPIC, b"toggle")
        time.sleep_ms(200)

    c.disconnect()