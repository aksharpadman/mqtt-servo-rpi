import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO
import json
from time import sleep
THINGSBOARD_HOST = 'demo.thingsboard.io'
ACCESS_TOKEN = 'UeugaVs0MDlymrwT21GK'
#Set GPIO pins numberingg as on RPi board
GPIO.setmode(GPIO.BOARD)
#Use pin 3 as output
GPIO.setup(3,GPIO.OUT)
#set pin for PWM
pwm=GPIO.PWM(3,50)
pwm.start(0)
#function called when connected to server
def On_connect(client, userdata, rc, *extra_params):
    print('Connected with result code ' + str(rc))
    client.subscribe('v1/devices/me/rpc/request/+')

#function for processing the control message
def On_message(client, userdata, msg):
    data = json.loads(msg.payload)
    SetAngle(data)
#function for turning the servomotor as per requirement
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
