from flask import Flask, render_template_string, redirect, url_for
from gpiozero import LED

app = Flask(__name__)

led1 = LED(23)
led2 = LED(24)

html = """
<!DOCTYPE html>
<html>
<head>
    <title>Raspberry Pi LED Control</title>
</head>
<body>
    <h1>Raspberry Pi Flask Web Server</h1>
    <h2>LED Control</h2>

    <p>LED 1 Control</p>
    <a href="/led1/on"><button>LED 1 ON</button></a>
    <a href="/led1/off"><button>LED 1 OFF</button></a>

    <p>LED 2 Control</p>
    <a href="/led2/on"><button>LED 2 ON</button></a>
    <a href="/led2/off"><button>LED 2 OFF</button></a>
</body>
</html>
"""

@app.route("/")
def index():
    return render_template_string(html)

@app.route("/led1/on")
def led1_on():
    led1.on()
    return redirect(url_for("index"))

@app.route("/led1/off")
def led1_off():
    led1.off()
    return redirect(url_for("index"))

@app.route("/led2/on")
def led2_on():
    led2.on()
    return redirect(url_for("index"))

@app.route("/led2/off")
def led2_off():
    led2.off()
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)