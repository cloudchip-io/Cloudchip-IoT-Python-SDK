

import paho.mqtt.client as mqtt
import json
import time
import random

HOST = 'www.cloudchip.io'
TOKEN='*****************'

client=mqtt.Client()
client.username_pw_set(TOKEN)
client.connect(HOST,1883,60)
client.loop_start()
data={"Temperature":0,"Light":0}

while True:
  
    data['Temperature']= random.randrange(-25, 80)
    data['Light']= random.randrange(0, 100)
    client.publish('v1/devices/me/telemetry',json.dumps(data),0)
    print(data);
    time.sleep(1)
    
