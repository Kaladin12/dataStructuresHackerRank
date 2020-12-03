import math
    
def solve(n, k, roads):
    myGraph = {}
    nodeEdge1 = None
    nodeEdge2 = None
    edgeNeeded = None
    edge_counter = 1
    for i in roads:
        a = i[0]
        b = i[1]
        edge = i[2]
        if (not myGraph.get(a)):
            myGraph[a] = {}
        myGraph[a][b] = edge 
        if (not myGraph.get(b)):
            myGraph[b] = {}
        myGraph[b][a] = edge 
        if (edge_counter == k):
            nodeEdge1 = a
            nodeEdge2 = b
            edgeNeeded = edge
        edge_counter+=1
    
    def dijkstra(begin, end):
        shortest = {}

        last = {}
        notVisitedNodes = []
        notVisitedNodes = myGraph.copy()
        path = []
        for everyNode in notVisitedNodes:
            shortest[everyNode] = math.inf
        shortest[begin] = 0
        while (notVisitedNodes):
            closestNode = None
            for node in notVisitedNodes:
                if (closestNode==None) or (shortest[node]<shortest[closestNode]):
                    closestNode = node
            currentPath = myGraph[closestNode].items()  
            for data in currentPath:
                if (data[1]+shortest[closestNode]<shortest[data[0]]):
                    shortest[data[0]] = data[1] + shortest[closestNode]
                    last[data[0]] = closestNode
            notVisitedNodes.pop(closestNode)
        currentNode = end
        while currentNode != begin:
            path.insert(0,currentNode)
            currentNode = last[currentNode] 
        path.insert(0,begin)  
        #print("distancia:", shortest[end])
        #print(path)  
        return shortest[end]#,path] 
    values = []
    for i in myGraph:
        if (i!=nodeEdge1 and i!=nodeEdge2):
            values.append((dijkstra(nodeEdge1, i), dijkstra(nodeEdge2, i)))
        elif (i==nodeEdge1):
            values.append((0, edgeNeeded))
        else:
            values.append((edgeNeeded,0))
    def biseccionChafa(INFER, SUPER):
        if (n==2):
            v =edgeNeeded/2
            return float('%0.05f' % v)
        inf, sup = INFER, SUPER
        er = 8
        while (sup-inf >0.00001):
            currentInf = inf + (sup-inf)/4
            currentSup = inf +3*(sup-inf)/4
            resInf, resSup = [], []
            count = 1
            for i in values:
                if (i[1]==0):
                    resInf.append(edgeNeeded-currentInf)
                    resSup.append(edgeNeeded-currentSup)
                else:
                    resInf.append(i[0]+currentInf)
                    resSup.append(i[0]+currentSup)
            deviationInf = max(resInf)
            deviationSup = max(resSup)
            nextV = (inf+sup)/2
            if (deviationInf<=deviationSup):
                sup = nextV
            else:
                inf = nextV
            er-=1
        return float('%0.05f' % inf)
    def getMax(distance):
        currentMax = 0
        for node in values:
            temp = min(node) + distance
            if temp>currentMax:
                currentMax = temp
        return currentMax


    dis = biseccionChafa(0, edgeNeeded)
    print("%0.05f" %(dis),"%0.05f" % getMax(dis))



    
#2
#2 1 1
#1 2 10
#4 4 1
#1 2 10
#2 3 10
#3 4 1
#4 1 5
dasRoads = [
    [1, 2, 10],
    [2, 3, 10],
    [3, 4, 1],
    [4, 1, 5]
]
dasRoads = [[1,2,10]]
solve(2,1,dasRoads)
dasRoads = [
    [1, 2, 10],
    [2, 3, 10],
    [3, 4, 1],
    [4, 1, 5]
]
solve(4,1,dasRoads)

#if (myGraph.get(a)):
#    myGraph[a].append({b: edge})
#else:
#    myGraph[a] =[{b: edge}]
#if (myGraph.get(b)):
#    myGraph[b].append({a: edge})
#else:
#    myGraph[b] =[{a: edge}]