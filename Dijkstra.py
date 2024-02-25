import matplotlib.pyplot as plt
import math

show_animation = True

class Animation():
    def __init__(self, show_animation):
        self.sx = -5.0
        self.sy = -5.0
        self.gx = 50.0
        self.gy = 50.0
        self.grid_size = 2.0
        self.robot_radius = 1.0
        self.right_end = 60.0
        self.left_end = -10.0
        self.upper_end = 60.0
        self.lower_end = -10.0
        self.ox = []
        self.oy = []
        self.show_animation = show_animation

    def add_obstacle(self):
        for i in range(-10, 60):
            self.ox.append(i)
            self.oy.append(-10.0)
        for i in range(-10, 60):
            self.ox.append(60.0)
            self.oy.append(i)
        for i in range(-10, 61):
            self.ox.append(i)
            self.oy.append(60.0)
        for i in range(-10, 61):
            self.ox.append(-10.0)
            self.oy.append(i)
        for i in range(-10, 40):
            self.ox.append(20.0)
            self.oy.append(i)
        for i in range(0, 40):
            self.ox.append(40.0)
            self.oy.append(60.0 - i)
    
    def animation(self, show_animation):
        if show_animation:
            plt.plot(self.ox, self.oy, ".k")
            plt.plot(self.sx, self.sy, "og")
            plt.plot(self.gx, self.gy, "xb")
            plt.grid(True)
            plt.axis("equal")
            plt.show()

def main():
    anim = Animation(show_animation)
    anim.add_obstacle()
    anim.animation(show_animation)

if __name__ == "__main__":
    main()