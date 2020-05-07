from matplotlib.animation import FuncAnimation
from matplotlib.patches import Circle
import matplotlib.pyplot as plt
import matplotlib as mplib
import numpy as np

class ball:
    def __init__(self, pos, vel, acc, size = 1, mass = 1):
        self.vector = np.array([pos, vel, acc], dtype = 'float64')
        self.circle = Circle(self.vector[0], size)

    def update_vector(self, dt, acc = None):
        if not acc == None:
            try:
                self.vector[2] = acc
            except:
                print('The acc vector should be the correct shape')
                
        self.vector[0] += self.vector[1] * dt
        self.vector[1] += self.vector[2] * dt

    def update_circle(self):
        self.circle.center = self.vector[0]

    def update(self, dt, acc = None):
        self.update_vector(dt, acc)
        self.update_circle()


fig, ax = plt.subplots()

balls = [ball([0, 0], [0, 0], [0,-9.81]),
         ball([0, 0], [0, 0], [0,9.81])]

dt = 1/600

def update(frame):
    for ball in balls:
        ball.update(dt)
        
    return([ball.circle for ball in balls])

def init():
    for ball in balls:
        ax.add_artist(ball.circle)

    return([ball.circle for ball in balls])

ax.set_xlim(-5,5)
ax.set_ylim(-5,5)

ani = FuncAnimation(fig, update, frames=np.linspace(0, 2*np.pi, 128),
                    init_func=init, blit=True, interval=1/60)

fig.show()
