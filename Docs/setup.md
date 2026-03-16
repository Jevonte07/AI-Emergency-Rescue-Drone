# Setup Instructions

## 1 Install Dependencies

Install Python packages:

pip install -r requirements.txt

## 2 Run Drone AI Server

python drone_ai/server.py

## 3 Connect Mobile App

Mobile app sends SOS request to:

http://<raspberry_pi_ip>:5000/sos

## 4 Start Camera Streaming

Run camera streaming module:

python drone_camera/stream.py