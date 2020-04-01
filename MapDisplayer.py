import numpy as np
import matplotlib.pyplot as plt
from Config import Config
from Status import Status
import time
from PIL import Image
import matplotlib.pyplot as plt

class MapDisplayer():



    # wall:紫色 1
    # healthy:绿色 3
    # sick:红色
    # 感染：黄色 4
    # 免疫：蓝色 1.7
    # 空地：白色

    def __init__(self):
        pass


    def drawMap(self,map:list,interval):

        blue = [30, 144, 255]
        white = [255, 255, 255]
        red = [255, 0, 0]
        yellow = [255, 215, 0]
        purple = [75, 0, 130]
        green = [0, 128, 0]

        map = np.array(map)
        length = map.shape[0]
        width = map.shape[1]

        colorMap = np.ones((length,width,3),dtype=int)
        for i in range(length):
            for j in range(width):
                if map[i,j] == -1:
                    colorMap[i,j] = purple
                elif map[i,j] == 0:
                    colorMap[i,j] = white
                elif map[i,j] == 1:
                    colorMap[i,j] = green
                elif map[i,j] == 2:
                    colorMap[i,j] = yellow
                elif map[i,j] == 3:
                    colorMap[i,j] = red
                elif map[i,j] == 4:
                    colorMap[i,j] = blue

        fig = plt.figure("Map")
        plt.ion()
        plt.imshow(colorMap)
        plt.axis('off')
        plt.show()
        plt.pause(interval)
        plt.ioff()
        plt.clf()

if __name__ == '__main__':

    mapDisplayer = MapDisplayer()

    map = [[1,2,3],[-1,0,1]]

    mapDisplayer.drawMap(map,5)


