from flask import Flask, make_response, request


# Create Flask's `app` object
app = Flask(__name__)


@app.route("/", methods=['GET'])
def hello():
    if request.method != 'GET':
        return make_response('Malformed request', 400)
    headers = {"Content-Type": "application/json"}
    return make_response('it worked!', 200, headers)

app.run(host='0.0.0.0', port=5000)