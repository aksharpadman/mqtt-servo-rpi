import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO
import json
from time import sleep
THINGSBOARD_HOST = 'demo.thingsboard.io'
ACCESS_TOKEN = 'UeugaVs0MDlymrwT21GK'
GPIO.setmode(GPIO.BOARD)
GPIO.setup(3,GPIO.OUT)
pwm=GPIO.PWM(3,50)
pwm.start(0)

def On_connect(client, userdata, rc, *extra_params):
    print('Connected with result code ' + str(rc))
    client.subscribe('v1/devices/me/rpc/request/+')

def On_message(client, userdata, msg):
    data = json.loads(msg.payload)
    SetAngle(data)

def SetAngle(angle):
     duty=(angle/18)+2
     GPIO.output(3,True)
     pwm.ChangeDutyCycle(duty)
     sleep(1)
     GPIO.output(3,False)
     pwm.ChangeDutyCycle(0)

client = mqtt.Client()
# Register connect callback
client.on_connect = On_connect
# Registed publish message callback
client.on_message = On_message
# Set access token
client.username_pw_set(ACCESS_TOKEN)
# Connect to ThingsBoard using default MQTT port and 60 seconds keepalive interval
client.connect(THINGSBOARD_HOST, 1883, 60)
try:
    client.loop_forever()
except KeyboardInterrupt:
    GPIO.cleanup()
