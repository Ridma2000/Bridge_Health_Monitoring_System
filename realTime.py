# realtime_serial_web.py
import serial
import threading
import time
from flask import Flask, Response, render_template_string

# ====================
# CONFIG
# ====================
SERIAL_PORT = "COM19"   # <-- Change to your port (e.g. "/dev/ttyACM0" on Linux/Mac)
BAUD_RATE = 115200

# ====================
# Globals
# ====================
latest_line = ""  # store latest serial data

# ====================
# Serial Reader Thread
# ====================
def read_serial():
    global latest_line
    ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
    time.sleep(2)  # wait for Arduino reset
    while True:
        try:
            line = ser.readline().decode("utf-8", errors="ignore").strip()
            if line:
                latest_line = line
                print(line)  # also print to terminal
        except Exception as e:
            print("Serial error:", e)
            time.sleep(1)

# ====================
# Flask App
# ====================
app = Flask(__name__)

# HTML template (auto-updating with SSE)
HTML_PAGE = """
<!DOCTYPE html>
<html>
<head>
    <title>Real-time Serial Monitor</title>
    <style>
        body { font-family: Arial, sans-serif; background: #111; color: #0f0; }
        #data { font-size: 20px; margin-top: 20px; white-space: pre-line; }
    </style>
</head>
<body>
    <h2>Seeed XIAO Edge Impulse - Live Data</h2>
    <div id="data">Waiting for data...</div>

    <script>
        var eventSource = new EventSource("/stream");
        eventSource.onmessage = function(e) {
            document.getElementById("data").innerText = e.data;
        };
    </script>
</body>
</html>
"""

@app.route("/")
def index():
    return render_template_string(HTML_PAGE)

@app.route("/stream")
def stream():
    def event_stream():
        last_sent = ""
        while True:
            global latest_line
            if latest_line != last_sent:
                yield f"data: {latest_line}\n\n"
                last_sent = latest_line
            time.sleep(0.1)
    return Response(event_stream(), mimetype="text/event-stream")

# ====================
# Main
# ====================
if __name__ == "__main__":
    t = threading.Thread(target=read_serial, daemon=True)
    t.start()
    print("Starting web server on http://127.0.0.1:5000 ...")
    app.run(debug=False, port=5000, threaded=True)
