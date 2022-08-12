from flask import Flask, render_template
from flask_simplelogin import SimpleLogin
from flask_restful import Resource, Api

app = Flask(__name__)
app.secret_key = '1q2w3e4r!'
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'hello' : 'world'}

todos = {}

class TodoSimple(Resource):
    def get(self, todo_id):
        return {todo_id: todos[todo_id]}

    def put(self, todo_id):
        todos[todo_id] = request.form['data']
        return {todo_id: todos[todo_id]}


api.add_resource(HelloWorld, '/helloworld')
api.add_resource(TodoSimple, '/<string:todo_id>')

@app.route('/home', methods=['GET'])
def home():
    return render_template("index.html")


if __name__=="__main__":
    app.run(debug=True)