import math
import time
from tkinter import *

class Pendulum:
    def __init__(self, master):
        self.master = master
        master.title("Pendulum Simulation")

        self.length = 100
        self.angle = math.pi / 4

        self.canvas = Canvas(master, width=300, height=300)
        self.canvas.pack()

        self.update_pendulum()

    def update_pendulum(self):
        x = 150 + self.length * math.sin(self.angle)
        y = 150 + self.length * math.cos(self.angle)

        self.canvas.create_line(150, 150, x, y, fill="red")
        self.canvas.create_oval(x-5, y-5, x+5, y+5, fill="blue")

        self.angle += 0.05
        self.master.after(50, self.update_pendulum)

root = Tk()
my_pendulum = Pendulum(root)
root.mainloop()
