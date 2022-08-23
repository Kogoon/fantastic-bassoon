# -*- coding: utf-8 -*-
from flask import Flask, request, url_for, redirect, render_template
from controller.authcontroller.forms import RegisterForm
#from flask_login import LoginManager 

app = Flask(__name__)
app.config['SECRET_KEY'] = '1q2w3e4r!'

# login_manager = LoginManager()
# login_manager.init_app(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/register', methods=['GET'])
def register():
    return render_template('register.html')

@app.route('/login')
def login():
    return render_template('login.html')


# @app.route('/logout', methods=['GET'])
# def logout():
#     return redirect(url_for('index'))

# @app.route('/home')
# @login_required
# def private_page():
#     session['page']

# @login_manager.user_loader
# def load_user(user_id):
#     return user_repo.get(user_id)

# @login_manager.unauthorized_handler
# def unauthorized_callback():
#     #print(dir(request))
#     query_string = urlencode(request.args)

#     return redirect(url_for('auth.login', next=f'{request.path}?{query_string}'))



if __name__ == "__main__":
    app.run()