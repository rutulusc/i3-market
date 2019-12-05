import paho.mqtt.client as mqtt
import time
import os

def on_connect(client, userdata, flags, rc):    
    print("Result from connect: {}".format(mqtt.connack_string(rc)))
    client.subscribe(topic[0])


def on_subscribe(client, userdata, mid, granted_qos):    
    print("Subscribed")


def on_message(client, userdata, msg):
    print("Message received. Topic: {}. Payload: {}".format(msg.topic, str(msg.payload)))

if __name__ == "__main__":

    account = 'muser2'
    topic = ['muser1/testhub1996/topic1996']
    pw = 'xgndw220kwuh'
    port = 1883
    host = '18.219.4.146'


    client = mqtt.Client(protocol=mqtt.MQTTv311)    
    client.on_connect = on_connect    
    client.on_subscribe = on_subscribe    
    client.on_message = on_message
    client.username_pw_set(account, pw)
    client.connect(host, port)   
    client.loop_forever()
