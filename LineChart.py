import numpy as np
import matplotlib.pyplot as plt
from Config import Config
from Status import Status


# x = np.linspace(0, 2 * np.pi, 100)
# y1, y2 = np.sin(x), np.cos(x)
#
# plt.plot(x, y1)
# plt.plot(x, y2)
#
# plt.title('line chart')
# plt.xlabel('x')
# plt.ylabel('y')
#
# plt.show()

class LineChart():
    def __init__(self):
        pass

    def drawLineChart(self, target: list):
        time = list(range(len(target)))
        healthy = []
        incub = []
        sick = []
        immune = []
        for i in range(len(target)):
            healthy.append(target[i][Status.HEALTHY])
            incub.append(target[i][Status.INCUB])
            sick.append(target[i][Status.SICK])
            immune.append(target[i][Status.IMMUNE])

        plt.plot(time, healthy)
        plt.plot(time, incub)
        plt.plot(time, sick)
        plt.plot(time, immune)

        plt.title('line chart')
        plt.xlabel('x')
        plt.ylabel('y')

        plt.show()


if __name__ == '__main__':
    lineChart = LineChart()

    one = {Status.HEALTHY: 10, Status.INCUB: 0, Status.SICK: 10, Status.IMMUNE: 5}
    two = {Status.HEALTHY: 5, Status.INCUB: 5, Status.SICK: 5, Status.IMMUNE: 5}
    three = {Status.HEALTHY: 2, Status.INCUB: 2, Status.SICK: 2, Status.IMMUNE: 2}
    four = {Status.HEALTHY: 3, Status.INCUB: 4, Status.SICK: 5, Status.IMMUNE: 6}
    sample = [one, two, three, four]

    lineChart.drawLineChart(sample)
