from flask import *
from datetime import *
app = Flask(__name__)
app.secret_key = 'mykey'
app.permanent_session_lifetime = timedelta(seconds=10)
@app.route('/')
def home():
    return """
        <h1>Hello, Welcome to Home page😎</h1>
        <p>Good to see you</p>
        <button type='submit'><a href='/login'>Login</a></button>
    """
@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        session['user'] = request.form['user']
        session['pass'] = request.form['key']
        return redirect(url_for('welcome'))
    else:
        return """
            <form method = 'post' action = '/login'>
                username:<input type='text' name = 'user'><br>
                password:<input type='password' name = 'key'><br>
                <button type='submit'>Submit</button>
            </form>
            """
@app.route('/welcome')
def welcome():
    if 'user' in session:
        return f'Welcome {session['user']}'
    else:
        return redirect(url_for('login'))
if __name__ == '__main__':
    app.run(debug=True)