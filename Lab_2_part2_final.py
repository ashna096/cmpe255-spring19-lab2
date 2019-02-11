import math


def normal_pdf(x, mu=0, sigma=1):
    var1 = 1 / (math.sqrt(2 * math.pi * sigma * sigma))
    var2 = math.exp(-((x - mu) * (x - mu)) / (2 * sigma * sigma))
    y = var1 * var2

    return y


from matplotlib import pyplot as plt

xs = [x / 10.0 for x in range(-50, 50)]
plt.plot(xs, [normal_pdf(x, sigma=1) for x in xs], '-', label='mu=0,sigma=1')
plt.plot(xs, [normal_pdf(x, sigma=2) for x in xs], '-', label='mu=0,sigma=2')
plt.plot(xs, [normal_pdf(x, sigma=0.5) for x in xs], '-', label='mu=0,sigma=0.5')
plt.plot(xs, [normal_pdf(x, sigma=-1) for x in xs], '-', label='mu=0,sigma=-1')
plt.legend()
plt.show()