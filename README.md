# 🌉 Bridge Health Monitoring System

A smart solution for real-time structural health monitoring of bridges using **Arduino Nano 33 BLE Sense** and **Edge Impulse**.

---

## 📌 Overview
This project leverages embedded sensors and machine learning to detect anomalies in bridge vibrations.  
An **on-device ML model** classifies the structural condition as either:

- **Normal**
- **Damage**

Real-time results are visualized on a **Flask-powered web dashboard** for easy monitoring.

---

## 🔍 Features
- ✅ **On-Device Machine Learning** – Classifies vibration patterns in real time.
- 📈 **Live Visualization Dashboard** – View sensor readings and classification results instantly.
- 🔌 **USB Serial Communication** – Reliable data transfer from Arduino to the Flask server.

---

## ⚙️ Tech Stack

| Component       | Technology Used                  |
|-----------------|-----------------------------------|
| Embedded Device | Arduino Nano 33 BLE Sense (C++)  |
| ML Platform     | Edge Impulse                     |
| Backend         | Python Flask (REST API)          |
| Frontend        | HTML, CSS, JavaScript (Dashboard) |

---

## 🚀 How to Run

1. **Train the Model**  
   - Collect vibration data via Arduino & Edge Impulse.  
   - Label and train the model (**Normal** vs **Damage**).  
   - Export as **Arduino C++ library**.

2. **Upload Firmware to Arduino**  
   - Integrate the exported Edge Impulse library into your Arduino sketch.  
   - Upload to **Arduino Nano 33 BLE Sense**.

3. **Start Flask Server**
   ```bash
   python server.py



