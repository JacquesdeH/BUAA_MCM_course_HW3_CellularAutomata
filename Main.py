# _*_coding:utf-8_*_
# Author      : JacquesdeH
# Create Time : 2020/3/31 23:49
# Project Name: project
# File        : Main.py
# --------------------------------------------------
import random
import time

import numpy as np

from Config import Config
from Graph import Graph
from InputHandler import InputHandler
from LineChart import LineChart
from MapDisplayer import MapDisplayer


def initGraph(Map):
    graph = Graph(Config.N_ROW, Config.N_COLUMN, Map)
    graph.addPopulation(Config.Population)
    graph.randomInfection()
    return graph


if __name__ == '__main__':
    random.seed(Config.SEED)
    np.random.seed(Config.SEED)

    inputHandler = InputHandler()
    lineChart = LineChart()
    mapDisplayer = MapDisplayer()

    Map = inputHandler.getMap()
    graph = initGraph(Map)
    timeSeq = []

    for i in range(Config.TotalRefreshCnt):
        if i != 0 and i % 10 == 0:
            print("On Period " + str(i + 1))
        graph.randomWalk()
        graph.stateTransfer()
        timeSeq.append(graph.count())
        curMap = graph.graphToMap()
        mapDisplayer.drawMap(curMap, Config.T)
        # time.sleep(Config.T)

    lineChart.drawLineChart(timeSeq)
