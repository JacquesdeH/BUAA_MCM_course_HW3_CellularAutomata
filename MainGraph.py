import random

class MainGraph:
    Map = None
    Graph = None
    def __init__(self, n, Map):
        self.n = n
        MainGraph.Map = Map
        tmpGraph = [[None for i in range(n)] for j in range(n)]
        for i in range(n):
            for j in range(n):
                if Map[i][j] == 0 :
                    tmpGraph[i][j] = []
                else :
                    tmp = None
        MainGraph.Graph = tmpGraph
    def getRandomLocation(self):
        while True:
                i = random.randint(0,self.n-1)
                j = random.randint(0,self.n-1)
                if MainGraph.Map[i][j] == 0:
                    break
        return (i,j)

    #throw people to the graph
    def throwInPopulation(self, num):
        for _ in range(num):
            (i,j) = self.getRandomLocation()
            MainGraph.Graph[i][j].append(Person())
        #

    #随机感染一人
    def randomInfection(self):
        while True:
            (i,j) = self.getRandomLocation()
            lst = MainGraph.Graph[i][j]
            if  lst != None and len(lst) > 0:
                break
        lst[0].infect()
        
    #随机移动
    def randomWalk(self):
        for i in range(self.n):
            for j in range(self.n):
                lst = MainGraph.Graph[i][j]
                if lst == None:
                    continue
                for person in lst:
                    self.personWalk(person,i,j)




    #一个人的移动
    def personWalk(self, person, i, j):
        choices = []
        if i > 0 and MainGraph.Map[i-1][j] == 0:
            choices.append("up")
        if i < self.n - 1 and MainGraph.Map[i+1][j] == 0:
            choice.append("down")
        if j > 0 and MainGraph.Map[i][j-1] == 0:
            choices.append("left")
        if j < self.n - 1 and MainGraph.Map[i+1][j] == 0:
            choice.append("right")
        if len(choices) == 0:
            return
        choice = choices[random.randint(0,len(choices) - 1)]
        if choice == "up":
            MainGraph.Graph[i-1][j].append(person)
            MainGraph.Graph[i][j].remove(person)
        elif choice == "down":
            MainGraph.Graph[i+1][j].append(person)
            MainGraph.Graph[i][j].remove(person)
        elif choice == "left":
            MainGraph.Graph[i][j-1].append(person)
            MainGraph.Graph[i][j].remove(person)
        elif cjpoce == "right":
            MainGraph.Graph[i][j+1].append(person)
            MainGraph.Graph[i][j].remove(person)
        else :
            print("unknown choice in personWalk")
        return


    #状态转换
    def stateShift(self):
        for i in range(self.n):
            for j in range(self.n):
                lst = MainGraph.Graph[i][j]
                if lst == None:
                    continue
                if len(lst) == 0:
                    continue
                for person in lst:
                    peron.updateStatus(self.getNeighbour(i,j))


    def getNeighbour(self, i, j):
        res = []
        for m in range(i-1,i+2):
            for n in range(j-1,j+2):
                lst = MainGraph.Map[i][j]
                if lst != None:
                    res.append(lst)

        return res

def test():
    Map = [[0,-1,0],[0,0,0],[-1,0,-1]]
    graph = MainGraph(3,Map)
    print(MainGraph.Graph)
    graph.throwInPopulation(3)
    print(MainGraph.Graph)
