# System Architecture

AI Emergency Rescue Drone System consists of three major components:

1. Mobile Application
2. Drone AI Server (Raspberry Pi)
3. Emergency Response System

## Workflow

User → Mobile App → Drone AI Server → Drone Camera → AI Processing → Emergency Alerts

## Architecture

Mobile App
   |
   |  SOS Request + Image + GPS
   v
Drone AI Server (Raspberry Pi)
   |
   | Face Recognition
   | Victim Tracking
   | Navigation
   v
Drone Camera System
   |
   | Live Video Feed
   v
Emergency Response
   |
   | SMS Alerts
   | Police Notification