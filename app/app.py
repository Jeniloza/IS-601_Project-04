from flask import Flask

# Create Flask's `app` object
app = Flask(__name__)

@app.route("/")
def index():
    return "Web App with Python Flask!"

app.run(host='0.0.0.0', port=5000)