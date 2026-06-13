import ssl
import os
import paho.mqtt.client as mqtt

BROKER = "687911b1a56e45cb86a3e073a1f868ca.s1.eu.hivemq.cloud"
PORT = 8883
USERNAME = "EBOEXAMPLE"
PASSWORD = os.environ["MQTT_PASSWORD"]

client = mqtt.Client()

client.username_pw_set(USERNAME, PASSWORD)

client.tls_set(cert_reqs=ssl.CERT_REQUIRED)

client.connect(BROKER, PORT)

client.publish("weather/test", "25")

print("Mensaje enviado: 50")

client.disconnect()
