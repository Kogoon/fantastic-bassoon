from flask import Flask
from flask_simplelogin import SimpleLogin
from flask_restful import Resource, Api

app = Flask(__name__)
app.secret_key = '1q2w3e4r!'
api = Api(app)


class HelloWorld(Resource):
    def get(self):
        return {'hello' : 'world'}

api.add_resource(HelloWorld, '/')

if __name__=="__main__":
    app.run(debug=True)