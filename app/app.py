from flask import Flask, make_response


# Create Flask's `app` object
app = Flask(__name__)


@app.route("/")
def hello():
    headers = {"Content-Type": "application/json"}
    return make_response('it worked!', 200, headers)

app.run(host='0.0.0.0', port=5000)