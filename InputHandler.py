from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

class InputHandler:
    def __init__(self):
        pass

    def getMap(self):
        base = np.array([100, 100, 100])
        size = 15
        img = np.array(Image.open('ukmap5.jpg'))
        result = np.zeros((img.shape[0], img.shape[1]),dtype=int)
        for i in range(img.shape[0]):
            for j in range(img.shape[1]):
                if img[i, j, 0] - base[0] < 0:
                    result[i, j] = 0
                else:
                    result[i, j] = -1
        # result = np.pad(result, ((0, 0), (86, 86)), "constant", constant_values=-1)
        return result.tolist()


if __name__ == '__main__':
    inputHandler = InputHandler()

    result = inputHandler.getMap()

    plt.figure("map")
    plt.imshow(result)
    plt.axis('off')
    plt.show()
