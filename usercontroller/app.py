from flask import Flask,jsonify,request,render_template
from database import Database

db = Database()

app = Flask(__name__)

@app.route("/register", methods=["GET"])
def get_register():
    return render_template("register.html")

@app.route("/register", methods=["POST"])
def post_register():
    name = request.form.get("name")
    email = request.form.get("email")
    password = request.form.get("password")

    db.query(f"insert into user (name, email, password) values('{name}', '{email}', '{password}')")

    return "user registered successfully"

@app.route("/login", methods=["GET"])
def get_login():
    return render_template("login.html")


@app.route("/login", methods=["POST"])
def post_login():
    email = request.form.get("email")
    password = request.form.get("password")

    user = db.select_records(f"select user_id, name from user where email = '{email}' and password = '{password}'")
    if len(user) == 0:
        return "Login Failed"
    else:
        return render_template("home.html")


if __name__ == "__main__":
    app.run(debug=True)