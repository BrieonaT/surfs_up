from flask import Flask
app = Flask(__name__)


#first route
@app.route('/')
def hello_world():
    return 'Hello world'