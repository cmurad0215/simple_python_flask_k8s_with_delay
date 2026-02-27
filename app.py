from flask import Flask
import time
import threading

app = Flask(__name__)

ready = False

def slow_startup():
    global ready
    print("Starting heavy initialization...")
    time.sleep(60)  # simulate cold start (1 minute)
    ready = True
    print("Application is ready now!")

# Run startup task in background
threading.Thread(target=slow_startup).start()


@app.route("/")
def home():
    return "Application is running okay\n"


@app.route("/healthz")
def liveness():
    return "OK\n", 200


@app.route("/readyz")
def readiness():
    if ready:
        return "READY\n", 200
    return "NOT READY\n", 503


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
