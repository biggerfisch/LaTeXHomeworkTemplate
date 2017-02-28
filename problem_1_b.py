import numpy as np
import matplotlib.pyplot as plt
from os.path import basename, splitext

def make_graph():
    x = np.linspace(0, 2*np.pi, 50)
    y = np.sin(x)

    fig = plt.figure()
    plt.plot(x, y)
    plt.savefig("%s.png" % splitext(basename(__file__))[0])

if __name__ == "__main__":
    make_graph()
    print("Hello World!")
