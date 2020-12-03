import math
def solve(n, k, roads):
    myGraph = {}
    nodeEdge1 = None
    nodeEdge2 = None
    edgeNeeded = None
    edge_counter = 1
    selection = []
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

f = open("txt\\test_2_4.txt", "r")
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
            #numbers.append(int(word))
        v.append(temp1)
    else:
        a = x
        for word in a.split():
            if word.isdigit():
                environVars.append(int(word))
    count +=1
print(v[environVars[2]-1])
solve(environVars[0],environVars[2],v)