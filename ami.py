import paho.mqtt.client as mqtt
import time
import os
import json
import re


from asterisk.ami import AMIClient
from asterisk.ami import EventListener


client1 = AMIClient(address='127.0.0.1',port=5038)
client1.login(username='admin',secret='ASDFasdf1')


def on_message(client, userdata, message):
    print("message received " ,str(message.payload.decode("utf-8")))
    print("message topic=",message.topic)
    print("message qos=",message.qos)
    print("message retain flag=",message.retain)



broker_address ="localhost"
client = mqtt.Client("P1")
client.on_message=on_message
client.connect(broker_address)
client.loop_start()



def event_listener(event,**kwargs):
    client.publish("asterisk/event",str(event))

client1.add_event_listener(
    on_Newstate=event_listener,
    white_list=re.compile('.*'),
    ChannelStateDesc=re.compile('^Ring.*'),
)


time.sleep(4)
client.loop_forever()

