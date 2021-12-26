# MQTT-Asterisk-AMI-Event
Simple Asterisk AMI Event publisher to MQTT using Python

Here is the example python code for sending AMI ringing events to MQTT.
Mainly two Python libraries are used.
paho.mqtt.client
asterisk.ami

For the testing run in one terminal 
mosquitto_sub -h localhost -t asterisk/event

and run python script in another terminal

then dial any call using a softphone.

![alt text](https://github.com/annnnnuza/MQTT-Asterisk-AMI-Event/blob/main/Screenshot.png?raw=true)
