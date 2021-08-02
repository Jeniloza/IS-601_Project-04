from flask import Flask, render_template

# Create Flask's `app` object
app = Flask(__name__, template_folder="templates")


@app.route("/")
def hello():
    """Landing page."""
    nav = [
        {'name': 'Home', 'url': '#home'},
        {'name': 'About', 'url': '#about'},
        {'name': 'Contact', 'url': '#contact'}
    ]
    return render_template("index.html", nav=nav)


app.run(host='0.0.0.0', port=5000)