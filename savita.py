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
            values.append((0, dijkstra(nodeEdge2,i)))
        else:
            values.append((dijkstra(nodeEdge1,i),0))

    def biseccionChafa(INFER, SUPER):
        if (n==2):
            v =edgeNeeded/2
            return [float('%0.05f' % v), float('%0.05f' % v)]
        inf, sup = INFER, SUPER
        
        while (sup-inf >0.00001 or sup==inf or sup==0):
            currentInf = inf + (sup-inf)/4
            currentSup = inf +3*(sup-inf)/4
            resInf, resSup = [], []
            for i in values:
                currentMin = min(i[0], i[1])
                u = edgeNeeded-currentInf + i[1]#resInf.append(edgeNeeded-currentInf + i[1])
                v = edgeNeeded-currentSup + i[1]#resSup.append(edgeNeeded-currentSup + i[1])
                u1 = i[0]+currentInf#resInf.append(i[0]+currentInf)
                v1 = i[0]+currentSup#resSup.append(i[0]+currentSup)
                resInf.append(min(u,u1))
                resSup.append(min(v,v1))
            deviationInf = max(resInf)
            deviationSup = max(resSup)
            nextV = (inf+sup)/2
            if (deviationInf<=deviationSup):
                sup = nextV
            else:
                inf = nextV
        return [float('%0.05f' % round(min(inf,sup))),float('%0.05f' % round(max(resInf)) if min(inf,sup)==inf else round(max(resSup)))]
    dis = biseccionChafa(0, edgeNeeded)
    return("%0.05f" %(dis[0]),"%0.05f" % (dis[1]))

#2
#2 1 1
#1 2 10
#4 4 1
#1 2 10
#2 3 10
#3 4 1
#4 1 5
#dasRoads = [
#    [1, 2, 10],
#    [2, 3, 10],
#    [3, 4, 1],
#    [4, 1, 5]
#]
#dasRoads = [[1,2,10]]
#solve(2,1,dasRoads)
#dasRoads = [
#    [1, 2, 10],
#    [2, 3, 10],
#    [3, 4, 1],
#    [4, 1, 5]
#]
#solve(4,1,dasRoads)
#dasRoads = [
#    [3, 7, 43],
#[7, 10, 91],
#[10, 1, 17],
#[1, 9, 86],
#[9, 5, 98],
#[5, 4, 85],
#[4, 8, 48],
#[8, 6, 94],
#[6, 2, 57],
#[5, 2, 80]
#]
#solve(10,4,dasRoads)
#dasRoads = [
#    [6, 9, 93],
#[9, 4, 18],
#[4 ,3 ,80],
#[3, 7, 94],
#[7, 1, 68],
#[1, 5, 58],
#[5 ,10, 72],
#[10, 8, 45],
#[8, 2 ,93],
#[7, 10, 72],
#]
#solve(10,8,dasRoads)
#dasRoads = [
#    [1, 7, 77],
#[7, 8, 1],
#[8 ,10, 85],
#[10, 2, 21],
#[2, 4, 51],
#[4, 5, 66],
#[5, 9, 86],
#[9, 6, 89],
#[6, 3, 26],
#[9, 3, 70]
#]
#solve(10,5,dasRoads)
f = open("txt\\test_2_1.txt", "r")
v = []
environVars = []
count = 0
for x in f:
    if (count!=0):
        a = x
        temp1 = []
        for word in a.split():
            if word.isdigit():
                temp1.append(int(word))
        v.append(temp1)
    else:
        a = x
        for word in a.split():
            if word.isdigit():
                environVars.append(int(word))
    count +=1
print(solve(environVars[0],environVars[2],v))