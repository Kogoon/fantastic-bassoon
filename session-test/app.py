import os
import redis
from flask import Flask, session, redirect, escape, request

app = Flask(__name__)
#app.secret_key = os.environ.get('SECRET_KEY', default=None)
app.secret_key = "POTENTIOAL3GO4SEOUL2GO"

REDIS_URL = 'redis://' + os.environ.get('REDIS_URL')
store = redis.Redis.from_url(REDIS_URL)

@app.route('/')
def index():
    if 'username' in session:
        
        username = escape(session['username'])
        visits = store.hincrby(username, 'visits', 1)

        store.expire(username, 10)

        #return 'Logged in as %s' % escape(session['username'])
        return '''
            Logged in as {0}.<br>
            Visits: {1}
        '''.format(username, visits)

    return 'You are not logged in'


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect('/')

    return '''
        <form method="post">
        <p><input type=text name=username>
        <p><input type=submit value=Login>
        </form>
    '''


@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)