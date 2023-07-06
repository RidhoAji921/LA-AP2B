from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

users = [
    {'username': 'admin', 'password': 'admin123'},
    {'username': 'RidhoAji921', 'password': 'iniPasswordnya'},
    {'username': 'user', 'password': 'user123'}
]

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        for user in users:
            if user['username'] == username and user['password'] == password:
                return redirect(url_for('dashboard'))
        error  = 'Username atau password salah'
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

app.run(debug=True)