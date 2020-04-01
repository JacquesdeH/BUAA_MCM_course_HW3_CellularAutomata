import numpy as np
import matplotlib.pyplot as plt
from Config import Config
from Status import Status
import time
from PIL import Image
import matplotlib.pyplot as plt

class MapDisplayer():
    def __init__(self):
        pass


    def drawMap(self,map:list,interval):

        fig = plt.figure("Map")
        plt.ion()
        plt.imshow(map)
        plt.axis('off')
        plt.show()
        plt.pause(interval)
        plt.ioff()
        plt.clf()

if __name__ == '__main__':

    mapDisplayer = MapDisplayer()

    for i in range(100):

        img = np.array(Image.open('../ukmap2.jpg'))
        mapDisplayer.drawMap(img,2)
        img = np.array(Image.open('../ukmap.jpg'))
        mapDisplayer.drawMap(img,2)


