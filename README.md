# IoT26-HW04

## Project Overview
This project demonstrates a Raspberry Pi web server using Flask to control GPIO outputs.  
The Raspberry Pi hosts a standalone web server that allows users to control LEDs through a web browser.

---

## Objective
- Build a Flask-based web server on Raspberry Pi
- Control GPIO pins through a web interface
- Toggle LEDs remotely using Raspberry Pi
- Practice web-based IoT interaction with GPIO devices

---

## 🛠️ Hardware Setup
- Raspberry Pi
- Breadboard
- 2 LEDs
- Resistors
- Jumper wires

---

## ⚙️ Circuit
- Two LEDs connected to Raspberry Pi GPIO output pins
- GPIO pins configured as output using Python
- Flask web server sends commands to control LED states

<img src="YOUR_CIRCUIT_IMAGE_HERE" width="400"/>

---

## Flask Web Server
This project follows the tutorial below:

https://randomnerdtutorials.com/raspberry-pi-web-server-using-flask-to-control-gpios/

The Flask web page allows users to:
- Turn LED 1 ON/OFF
- Turn LED 2 ON/OFF
- Monitor GPIO status in real time

---

## IDE / Terminal
<img src="YOUR_TERMINAL_SCREENSHOT_HERE" width="400"/>

---

## Result
- Raspberry Pi successfully hosted the Flask web server
- LEDs were controlled through the browser interface
- GPIO states updated correctly when buttons were pressed


<img alt="HW4_hardware" src="https://github.com/user-attachments/assets/0e0bb48b-4791-439f-9f32-0757ab4f5a86" width="400"/>


---

## Video
비디오링크

---

## Code
```python
from flask import Flask, render_template
import RPi.GPIO as GPIO

app = Flask(__name__)

GPIO.setmode(GPIO.BCM)

led1 = 20
led2 = 21

GPIO.setup(led1, GPIO.OUT)
GPIO.setup(led2, GPIO.OUT)

GPIO.output(led1, GPIO.LOW)
GPIO.output(led2, GPIO.LOW)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/<deviceName>/<action>")
def action(deviceName, action):

    devicePin = 0

    if deviceName == 'led1':
        devicePin = led1

    if deviceName == 'led2':
        devicePin = led2

    if action == "on":
        GPIO.output(devicePin, GPIO.HIGH)

    if action == "off":
        GPIO.output(devicePin, GPIO.LOW)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
