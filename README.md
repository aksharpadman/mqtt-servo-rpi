#mqtt-servo-rpi
This project deals with controlling a servomotor connected to RPi board remotelty using the Mosquitto broker.The servomotor is controlled using an online IOT platform.For this project,Thingsboard dashboard(demo.thingsboard.io) is used.

#Code Details  
-Mosquitto client for Python is  Paho-mqtt client library.This library is imported initially.  
-The messages sent in Mosquitto broker through Thingsboard is in JavaScript Object Notation format(json).Hence to decode the messages the json library is imported.  
-The servomotor is controlled via the RPi GPIO pins.Hence,the RPi.GPIO library is imported.  
-For communicating with Thingsboard, the  mqtt client requires the address of the website which is specified in the variable THINGSBOARD_HOST.Also the connection requires an access token which need to be specified.The access token is provided by the Thingsboard website.  
-The GPIO library is used to initialize and set the numbering of the pins on the RPi board.Here we use the numbering as shown on the RPi board.Pin 3 is used to control the servomotor(PWM control).A pwm with frequency of 50 Hz is set on pin 3.  
-On_connect and On_message are the functions used to communicate with and recieve the control messages.On_connect contains the name of the topic to be subscribed and the message to be printed initially.On_message function is called when the mqtt client recieves control messages.This message needs to be decoded using the json library.The message contains the value of angle needed to be turned by the servomotor.  
-The angle recieved via the message is argument for the function SetAngle whichin turn calculates the duty cycle of PWM required to turn the servomotor to the specified angle.A servomotor turns from 0 to 180 degrees within a dutycycle range of 2%-12%.So the angle range(0,180) is mapped to a dutycycle range of(2,12).  
 dutycycle is calculated by the equation  
		duty=(angle/18)+2  
A signal of the calculated duty cycle is provided to the servomotor.  
-The client along with message and connect callbacks are registered.The whole code is looped.  
		
 
