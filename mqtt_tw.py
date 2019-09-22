
#This example illustrates how to connect to Cloudchip IoT Platform using Paho-MQTT

import json
import time
import random
import paho.mqtt.client as mqtt

# Platform credentials
HOST = 'maker.cloudchip.io'
TOKEN = '*****************'

# Creating the varible to store telemetry and widget values
telemetry = dict()
widget = dict()

# MQTT on_connect callback function
def on_connect(client, userdata, flags, rc):
    client.subscribe('v1/devices/me/rpc/request/+')
    

# MQTT on_message callback function
def on_message(client, userdata, msg):
    #print('Topic: ' + msg.topic)
    widget = msg.payload.decode('utf-8')
    print('Message: ' + widget)


# MQTT start the client instance
client = mqtt.Client()
client.username_pw_set(TOKEN)
client.connect(HOST, 1883, 60)

# MQTT registering the callbacks
client.on_connect = on_connect
client.on_message = on_message
client.loop_start()


while True:
    telemetry['sensor'] = random.randrange(1,99)
    client.publish('v1/devices/me/telemetry',json.dumps(telemetry), 1)
    time.sleep(2)
    print(telemetry)
    
#client.disconnect() 

