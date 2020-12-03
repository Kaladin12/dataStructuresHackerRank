def has_cycle(head):
    visitedNodes = []
    temp = head
    while (True):
        visitedNodes.append(temp)
        temp = temp.next
        if temp in visitedNodes:
            return 1
        if temp == None:
            return 0
