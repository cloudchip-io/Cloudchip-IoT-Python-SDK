
import os
import time
import sys
import json
import paho.mqtt.client as mqtt

HOST = 'www.cloudchip.io'
TOKEN = '*****************'

# MQTT on_connect callback function
def on_connect(client, userdata, flags, rc):
    client.subscribe('v1/devices/me/rpc/request/+')
    #print('Topic Subscribed')

# MQTT on_message caallback function
def on_message(client, userdata, msg):
    print('Topic: ' + msg.topic + '\nMessage: ' + str(msg.payload))
    data = json.loads(msg.payload)
    print(data['method'])
    print(data['params'])

# start the client instance
client = mqtt.Client()

# registering the callbacks
client.on_connect = on_connect
client.on_message = on_message
client.username_pw_set(TOKEN)
client.connect(HOST, 1883, 60)

try:
    client.loop_forever()

except KeyboardInterrupt:
    client.disconnect()

