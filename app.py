from flask import Flask, request, jsonify
import paho.mqtt.client as mqtt
import threading

app = Flask(__name__)

# MQTT Configuration
broker_address = "broker.hivemq.com"
client = mqtt.Client("Dashboard_Client")

# Global variable to store drone data
drone_data = []

def on_message(client, userdata, message):
    global drone_data
    data = message.payload.decode()
    # Assume data is a JSON string, you can process it accordingly
    drone_data.append(data)

client.connect(broker_address)
client.loop_start()
client.subscribe("drone/#")
client.on_message = on_message

@app.route('/drones', methods=['GET'])
def get_drones():
    return jsonify(drone_data)

@app.route('/log', methods=['POST'])
def log_event():
    event_data = request.json
    drone_data.append(event_data)
    return jsonify({"status": "success"})

if __name__ == '__main__':
    app.run(debug=True)
