from flask import Flask
#from datetime import datetime
import time
app = Flask(__name__)

@app.route("/")
def hello():
    return time.strftime("%H:%M:%S")

if __name__ == "__main__":
    app.run()
