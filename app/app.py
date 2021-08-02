from flask import Flask
from logic import square_of_number_plus_nine

# Create Flask's `app` object
app = Flask(__name__)

@app.route("/")
def hello():
    return "square of number five plus nine is " + str(square_of_number_plus_nine(5))

app.run(host='0.0.0.0', port=5000)