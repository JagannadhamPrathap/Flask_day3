from flask import Flask, request, session, redirect, url_for

app = Flask(__name__)
app.secret_key = "mykey"

users = {}

@app.route('/')
def home():
    if 'username' in session:
        return redirect(url_for('welcome'))
    return """
        Please login or register.<br>
        <a href='/login'><button>Login</button></a>
    """
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username in users:
            if users[username] == password:
                session['username'] = username
                return redirect(url_for('welcome'))
            else:
                return "Wrong password! <a href='/login'>Try again</a>"
        else:
            users[username] = password
            session['username'] = username
            return redirect(url_for('welcome'))
    return """
        <form action="/login" method="POST" autocomplete="off">
            Username: <input type="text" name="username" autocomplete="off" required><br>
            Password: <input type="password" name="password" autocomplete="new-password" required><br>
            <button type="submit">SUBMIT</button>
        </form>
    """
@app.route('/welcome')
def welcome():
    if 'username' not in session:
        return redirect(url_for('home'))
    return f"""
        <h2>Welcome {session['username']}!! 👩‍💻</h2>
        <p>You can take it from here</p>
        <p>Don't forget to logout!</p>
        <a href='/logout'><button>Logout</button></a>
    """
@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('home'))
if __name__ == "__main__":
    app.run(debug=True)
