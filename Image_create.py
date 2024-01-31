import numpy as np
import pandas as pd
from lightgbm import LGBMClassifier
import math
import matplotlib.pyplot as plt


def plot_results(a, h, radius = 3):
    # Convert degrees to radians
    rad = math.radians(a)

    # Calculate the width of the triangle
    width = 2 * h * math.tan(rad / 2)

    # Coordinates of the three vertices of the triangle
    x = [0, width / 2, width]
    y = [0, h, 0]

    plt.plot(x, y, 'b')
    # Center of the circle
    center = [width / 2, h]

    # Radius of the circle
    theta = np.linspace(0, 2 * np.pi, 100)
    x_cir = center[0] + radius * np.cos(theta)
    y_cir = center[1] + radius * np.sin(theta)

    # Create a figure and axes
    plt.plot(x_cir, y_cir, 'b')
    plt.ylim(0,h+radius+1)
    plt.xlim(0,width+1)

    plt.savefig("plot.jpg", format = 'jpg')
    # plt.show()
    plt.close()