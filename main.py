import flask
from flask import request
app = flask.Flask(__name__)

@app.route("/alogs")
def test():
    import ways
    request.args


app.run()