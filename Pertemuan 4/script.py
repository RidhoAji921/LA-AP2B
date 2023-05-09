from flask import Flask
app = Flask(__name__)

def salah(tipe, angka):
    return f"Angka yang dimasukkan salah, angka {angka} adalah angka {tipe}"

def benar(tipe, angka):
    return f"Anda benar, angka {angka} adalah angka {tipe}"

@app.route('/genap/<int:angka>')
def genap(angka):
    if(angka % 2 == 0):
        return benar("genap", angka)
    else:
        return salah("ganjil", angka)

@app.route('/ganjil/<int:angka>')
def ganjil(angka):
    if(angka % 2 != 0):
        return benar("ganjil", angka)
    else:
        return salah("genap", angka)

app.run()