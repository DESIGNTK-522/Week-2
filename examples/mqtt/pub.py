# publisher.py
import paho.mqtt.client as mqtt
import time
import json
import random
from datetime import datetime

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Successfully connected to broker")
    else:
        print(f"Connection failed with code {rc}")

# Create publisher client
publisher = mqtt.Client()
publisher.on_connect = on_connect

# Connect to public broker
print("Connecting to broker...")

# (broker, port, keepalive)
publisher.connect("test.mosquitto.org", 1883, 60)
publisher.loop_start()

try:
    while True:
        # Generate random temperature between 20°C and 25°C
        temperature = round(random.uniform(20.0, 25.0), 1)
        
        humidity = round(random.uniform(40.0, 60.0), 1)
        
        # Create sample sensor data
        sensor_data = {
            "hello": "hello class!!!!!!!",
            "temperature": temperature,
            "humidity": humidity,
            "timestamp": datetime.now().isoformat()
        }
        
        # Publish to topic - using a unique topic to avoid conflicts with other users
        topic = "pythontest/sensors/mysensor"
        publisher.publish(
            topic,
            json.dumps(sensor_data),
            qos=1
        )
        print(f"Published to {topic}: {sensor_data}")
        time.sleep(1)
        
except KeyboardInterrupt:
    print("Stopping publisher...")
    publisher.loop_stop()
    publisher.disconnect()
