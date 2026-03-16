from flask import Flask, request, jsonify
import face_recognition_module
import victim_tracking

app = Flask(__name__)

victim_location = None
victim_name = None


@app.route("/")
def home():
    return {"message": "AI Emergency Rescue Drone Server Running"}


@app.route("/sos", methods=["POST"])
def receive_sos():
    global victim_location, victim_name

    data = request.json

    victim_name = data.get("name")
    victim_location = data.get("location")

    print("🚨 SOS RECEIVED")
    print("Victim:", victim_name)
    print("Location:", victim_location)

    # trigger AI identification system
    face_recognition_module.load_known_face()

    return jsonify({
        "status": "Drone dispatched",
        "victim": victim_name
    })


@app.route("/status", methods=["GET"])
def drone_status():

    return jsonify({
        "drone": "active",
        "mission": "searching victim"
    })


@app.route("/identify", methods=["GET"])
def identify_victim():

    result = face_recognition_module.identify_from_camera()

    return jsonify({
        "identified": result
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)