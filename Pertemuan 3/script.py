from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

#daftar pengguna
users = [
    {'username': 'admin', 'password': 'admin123'},
    {'username': 'user', 'password': 'user123'},
    {'username': 'Ridho_Aji', 'password': 'qwertyuiop'}
]

#halaman login
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

if __name__ == '__main__':
    app.run(debug=True)