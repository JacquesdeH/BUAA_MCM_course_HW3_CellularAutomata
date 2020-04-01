import random
from Person import Person
from Status import Status
class MainGraph:
    def __init__(self, n, Map):
        self.n = n
        self.Map = Map
        tmpGraph = [[None for i in range(n)] for j in range(n)]
        for i in range(n):
            for j in range(n):
                if Map[i][j] == 0 :
                    tmpGraph[i][j] = []
                else :
                    tmp = None
        self.Graph = tmpGraph
    def getRandomLocation(self):
        while True:
            i = random.sample(range(self.n),1)[0]
            j = random.sample(range(self.n),1)[0]
            #print("random(i,j):(%d,%d)"%(i,j))
            if self.Map[i][j] == 0:
                break
        return (i,j)

    #throw people to the graph
    def addPopulation(self, num):
        for _ in range(num):
            (i,j) = self.getRandomLocation()
            self.Graph[i][j].append(Person())
        

    #随机感染一人
    def randomInfection(self):
        while True:
            (i,j) = self.getRandomLocation()
            #print("random location:(%d,%d)"%(i,j))
            lst = self.Graph[i][j]
            #print(lst)
            if  lst != None and len(lst) > 0:
                break
        lst[0].infect()
        
    #随机移动
    def randomWalk(self):
        movedPerson = []
        for i in range(self.n):
            for j in range(self.n):
                lst = self.Graph[i][j]
                if lst == None:
                    continue
                for person in lst:
                    if person not in movedPerson:
                        self.personWalk(person,i,j)
                        #print(self.Graph)
                        movedPerson.append(person)




    #一个人的移动
    def personWalk(self, person, i, j):
        choices = []
        if i > 0 and self.Map[i-1][j] == 0:
            choices.append("up")
        if i < self.n - 1 and self.Map[i+1][j] == 0:
            choices.append("down")
        if j > 0 and self.Map[i][j-1] == 0:
            choices.append("left")
        if j < self.n - 1 and self.Map[i][j+1] == 0:
            choices.append("right")
        #print(person,end = "")
        #print(choices)
        if len(choices) == 0:
            return
        choice = choices[random.randint(0,len(choices) - 1)]
        if choice == "up":
            self.Graph[i-1][j].append(person)
            self.Graph[i][j].remove(person)
        elif choice == "down":
            self.Graph[i+1][j].append(person)
            self.Graph[i][j].remove(person)
        elif choice == "left":
            self.Graph[i][j-1].append(person)
            self.Graph[i][j].remove(person)
        elif choice == "right":
            self.Graph[i][j+1].append(person)
            self.Graph[i][j].remove(person)
        else :
            print("unknown choice in personWalk")
        return


    #状态转换
    def stateTransfer(self):
        for i in range(self.n):
            for j in range(self.n):
                lst = self.Graph[i][j]
                if lst == None:
                    continue
                if len(lst) == 0:
                    continue
                for person in lst:
                    neighbour = self.getNeighbour(person,i,j)
                    #print(neighbour)
                    person.updateStatus(neighbour)


    def getNeighbour(self,person, i, j):
        res = []
        for m in range(i-1,i+2):
            for n in range(j-1,j+2):
                if m < 0 or m >= self.n:
                    continue
                if n < 0 or n >= self.n:
                    continue
                lst = self.Graph[m][n]
                if lst != None:
                    for p in lst:
                        if p is not person:
                            res.append(p)
        return res
    #给出待显示的矩阵,给hxy输出
    def graphToMap(self):
        res = [[]for _ in range(self.n)]
        for i in range(self.n):
            res[i] = self.Map[i].copy()
        for i in range(self.n):
            for j in range(self.n):
                if self.Map[i][j] == -1:
                    continue
                lst = self.Graph[i][j]
                if len(lst) == 0:
                    res[i][j] = 0
                    continue
                res[i][j] = lst[0].status.value
        return res

    def count(self):
        dct = {}
        healthyCount = 0
        incubCount = 0
        sickCount = 0
        immuneCount = 0
        for i in range(self.n):
            for j in range(self.n):
                lst = self.Graph[i][j]
                if lst == None:
                    continue
                for person in lst:
                    if person.status == Status.HEALTHY:
                        healthyCount += 1
                    elif person.status == Status.INCUB:
                        incubCount += 1
                    elif person.status == Status.SICK:
                        sickCount += 1
                    elif person.status == Status.IMMUNE:
                        immuneCount += 1
        dct[Status.HEALTHY] = healthyCount
        dct[Status.INCUB] = incubCount
        dct[Status.SICK] = sickCount
        dct[Status.IMMUNE] = immuneCount
        return dct
    
def test():
    Map = [[0,-1,0],[0,0,0],[-1,0,-1]]
    g = MainGraph(3,Map)
    #print(g.Map)
    print("----------")
    print("initialize the graph with [] and None")
    print(g.Graph)
    print(g.graphToMap())
    print("----------")
    g.addPopulation(3)
    print("add population")
    print(g.Graph)
    print(g.graphToMap())
    print("----------")
    g.randomInfection()
    print("randomInfection")
    print(g.Graph)
    print(g.graphToMap())
    for i in range(3):
        print("----------")
        print("random walk")
        g.randomWalk()
        print(g.Graph)
        print(g.graphToMap())
        print("----------")
        print("status transfer")
        g.stateTransfer()
        print(g.Graph)
        print(g.graphToMap())
        print("----------")
        print("count graph")
        print(g.count())
        print("----------")
        
