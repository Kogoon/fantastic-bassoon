from flask import Flask
from flask_simplelogin import SimpleLogin

app = Flask(__name__)
app.secret_key = '1q2w3e4r!'


@app.route('/')
def home():
    return 

SimpleLogin(app)

