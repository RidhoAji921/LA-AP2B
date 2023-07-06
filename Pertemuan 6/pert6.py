from PyQt5.QtWidgets import QVBoxLayout, QApplication, QPushButton, QLineEdit, QWidget, QFormLayout, QGridLayout

class myWindow(QWidget):
    def __init__(self):
        super().__init__()
        formlayout = QVBoxLayout()
        mainlayout = QFormLayout()
        bottomlayout = QGridLayout()
        self.LEnama = QLineEdit()
        self.LEkelas = QLineEdit()
        self.LEnpm = QLineEdit()
        self.LEjurusan = QLineEdit()
        self.LEfakultas = QLineEdit()
        tombol = QPushButton("submit")

        mainlayout.addRow("Nama", self.LEnama)
        mainlayout.addRow("Kelas", self.LEkelas)
        mainlayout.addRow("NPM", self.LEnpm)
        mainlayout.addRow("Jurusan", self.LEjurusan)
        mainlayout.addRow("Fakultas", self.LEfakultas)

        bottomlayout.addWidget(tombol,0,0,1,0)

        formlayout.addLayout(mainlayout)
        formlayout.addLayout(bottomlayout)
        tombol.clicked.connect(self.button)

        self.setLayout(formlayout)

    def button(self):
        print(self.LEnama.text())
        print(self.LEkelas.text())
        print(self.LEnpm.text())
        print(self.LEjurusan.text())
        print(self.LEfakultas.text())

app = QApplication([])
window = myWindow()
window.show()
app.exec_()