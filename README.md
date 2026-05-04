📡 GPS Sensor Data Analysis using CounterFit
📌 Project Overview

This project simulates a GPS sensor using CounterFit and processes NMEA sentences to extract useful navigation data such as:

📍 Latitude & Longitude (position)
⏰ UTC Time
📅 Date
🚀 Speed (knots and km/h)
⛰ Altitude (if available in GGA sentence)

The goal is to demonstrate how IoT devices can extract and use real-world GPS data beyond simple coordinates.

🎯 Objectives
Connect a virtual GPS sensor using CounterFit
Read raw NMEA sentences from UART simulation
Parse GPS data programmatically
Extract meaningful information (time, speed, location, etc.)
(Optional) Convert GPS time into system time format
🧰 Technologies Used
Python 3.11
CounterFit IoT Simulator
counterfit-connection
counterfit-shims-serial
NMEA protocol
📡 NMEA Data Format Used

Example NMEA sentence:

$GNRMC,020604.001,A,4738.538654,N,12208.341758,W,0.5,0.0,010203,,,A*68
🧠 Data Extracted from NMEA
📍 Position (Latitude & Longitude)
Latitude: 4738.538654 N
Longitude: 12208.341758 W
⏰ Time (UTC)

From $GNRMC:

020604.001 → 02:06:04 UTC
📅 Date
010203 → 01/02/2003
🚀 Speed
Speed in knots: 0.5
Converted to km/h:
speed_kmh = speed_knots * 1.852
⛰ Altitude (from GGA sentence)

Example:

$GNGGA,...,164.7,M,...
Altitude: 164.7 meters above sea level
⚙️ System Architecture
CounterFit GPS Sensor
        ↓
UART Serial Simulation (/dev/ttyAMA0)
        ↓
Python App (app.py)
        ↓
NMEA Parser
        ↓
Extracted GPS Data Output
💻 Implementation Summary
1. Connect CounterFit
from counterfit_connection import CounterFitConnection
CounterFitConnection.init('127.0.0.1', 5000)
2. Read Serial Data
import counterfit_shims_serial

serial = counterfit_shims_serial.Serial('/dev/ttyAMA0')
3. Parse NMEA Sentence
line = serial.readline().decode('utf-8')

if "$GNRMC" in line:
    parts = line.split(',')
    time = parts[1]
    status = parts[2]
    lat = parts[3]
    lon = parts[5]
    speed = float(parts[7])
    date = parts[9]

    speed_kmh = speed * 1.852
📊 Sample Output
TIME: 020604.001
DATE: 010203
LAT: 4738.538654 N
LON: 12208.341758 W
SPEED: 0.5 knots (0.93 km/h)
STATUS: Active
🚀 Advanced Features (Bonus)

✔ Convert speed from knots → km/h
✔ Parse multiple NMEA sentence types (GGA, RMC)
✔ Extract altitude data
✔ Continuous real-time GPS reading
✔ Ready for IoT system integration (e.g. cloud logging)

🧪 How to Run
1. Start CounterFit
counterfit
2. Configure GPS Sensor
Type: UART GPS
Port: /dev/ttyAMA0
Source: NMEA
3. Run Python App
python app.py
🎯 Learning Outcomes

After completing this project, I learned:

How GPS data is structured using NMEA protocol
How to simulate IoT hardware using CounterFit
How to parse and extract meaningful data from raw sensor streams
How IoT systems process real-time data in embedded environments
📌 Conclusion

This project demonstrates how GPS raw data can be transformed into useful information for IoT applications. It simulates real-world GPS processing and provides a foundation for future projects such as tracking systems, navigation apps, and IoT monitoring systems.
