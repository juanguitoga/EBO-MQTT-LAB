import ssl
import os
import paho.mqtt.client as mqtt

BROKER = "687911b1a56e45cb86a3e073a1f868ca.s1.eu.hivemq.cloud"
PORT = 8883
USERNAME = "EBOEXAMPLE"
PASSWORD = os.environ.get("MQTT_PASSWORD")

print("Password encontrada:", PASSWORD is not None)

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)

client.username_pw_set(USERNAME, PASSWORD)

client.tls_set(cert_reqs=ssl.CERT_REQUIRED)

print("Intentando conectar...")

client.connect(BROKER, PORT, 60)

print("Conectado")

info = client.publish("weather/test", "50")

print("Código publicación:", info.rc)

client.loop(timeout=2)

client.disconnect()

print("Terminado")
