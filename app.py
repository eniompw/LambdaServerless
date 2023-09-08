from flask import Flask, make_response

app = Flask(__name__)

@app.route("/")
def hello_from_root():
    return 'Hello from root!'

@app.route("/hello")
def hello():
    return 'Hello from path!'

@app.errorhandler(404)
def resource_not_found(e):
    return make_response('Not found!', 404)
