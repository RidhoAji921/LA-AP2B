import threading
from threading import Thread
import time

def tugas1():
    for i in range(0, 10):
        print("Ridho Aji Gumilang")

def tugas2():
    for i in range(0, 10):
        print(51422432)

t1 = Thread(target=tugas1())
t2 = Thread(target=tugas2())

t1.start()
t2.start()

time.sleep(0.1)

t1.join()
t2.join()

print("LA Pertemuan 1 Selesai...")