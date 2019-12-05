import paho.mqtt.client as mqtt
import time
import os


if __name__ == "__main__":

    account = 'muser1$testhub1996$device77'
    topic = ['muser1/testhub1996/topic1996']
    pw = 'rutul1997'
    port = 1883
    host = '18.219.4.146'

    client = mqtt.Client(protocol=mqtt.MQTTv311)
    client.username_pw_set(account, pw)
    client.connect(host, port)
    print("Connected to broker") 
    client.publish(topic[0], payload="I3 Marketplace")
    print("Published")
