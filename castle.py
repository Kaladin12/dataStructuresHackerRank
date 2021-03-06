import time

grid = [
    '....X...........X....X..X...X.X..X.........X.X..X.X.....X.X..................X...X....XX........X.X.',
    'X..X..........X..X....X.........XX.X.XX...XX..X...X..X.......XX...X..........X...X.....X....X.X.....',
    '..........X....X......X..X...X..........X..X......X....X...X.X..X..X.....X......X...........X......X',
    '......X.X........X..X...........X..XX...X..........X........XX...X....X..XX..X..X......XX...XX......',
    '....X....X..X...XX.X...X...X.................X....XX..XX...X....X.X.....X........X.............X....',
    'X.X......X...X..X.X.X.......X...X..X............XXX....X....X..X.XX..X...XX....XXX.....X.......X....',
    '...X.X....X...X......X.X..X.....X.....X.XX..............X.........X.X.......X..XX.........XX........',
    '..X..XX.......X..X........X.........XX...........X.XX...........X.........X.....XX.X..........XX.X..',
    '...X..........X.....X....X.XX....X..XX.X.X..........X.......XX...X......X.X.....X...X.....X.........',
    '.X...................XX........X..X..........X.X...X.......X..X.X....X.........X...X.X..X.......X...',
    'X....X....X..X.......X......X..X.X..X.........X.....XXXXX..................X....................X...',
    'X.XX......X............X.X....X....X.X.........XXX....XX.....XXXXX...XX.XX...X.XX.....X.X......X.X..',
    '..X..X..XXX.X.........X.....XX...X....X..................X..X..............X..X.XX....XX.X..........',
    '..............X.....X.X...X.X.X..........X...X.X...X...X...X.....X..X...X.X......X.....X...X..X....X',
    '.....................X...............X.X........X..XX.........X.X.......X....X......XXX.....X.X.....',
    '.XX......X..X.........XXX.....X.........X..X.......XX.........X.X..X..X..X...X....XX.....XX.X...X...',
    '......X........X.XX......X..............X....XX.......XX...................X........X.....X.......XX',
    '.XXX......XX................XX...X......X..XX......XXXX......X...X...............X.X................',
    '...X............XX....X....X...XX......X....X...X........X...X...X......X.....X.............X.......',
    '..............XXX.XX..........X..........XXX...X...........X....XX.........X..X......X........X.X...',
    '.....X.........X.X.......X.X......X.............X..XX......X.......X.........X.....XXX....X......X..',
    '....XX..........X....X.XX..X..X...X.............X.........X........XX..X..XX................X..XXX..',
    '.......XX....X..X.....X.XX..X.X.X.X..XX..X.X...X.X.X.....X..X.X.XX..XX.....X....X...X.....XX.X......',
    '...X......X.X..X...XX.X.X..X.X.......X.....X.X......X.....X..XX...X...X..XX..X.X.........X.X.......X',
    '.......X..........X...X......X.........X...X....X..X....X..X.......X..XX......X..X.XX......XX.......',
    '................X.....X.........X...X...............X....X...X.XX....X....X..X.XX.....X....X....X...',
    'X..X.............X.....X....X...............X..XX..X............X...................X........X.X....',
    '..X..........X...................XX.X.X...................X...........X....X....X.....X.X...X.XX.X..',
    '.....XX....X......X.....X.X.................X...XXX..X.X.XX.....X.........X...........X........X....',
    '....X....X.XXX.....X...........X................................X.X.....................X....X......',
    '..X..X.X..............X.......X........X........X..............X....X....X.............X............',
    'XX...X..X.X...X....X................X...........XXX...........X.XXX..X....XX...X.......X.....X.X....',
    '.X...............X.XXX......XX.....X.......X...X............X.XX....................X..XXX..........',
    '.......XX......X.........X..X........X....X.X.....X.X...X.X.....X............X.X....................',
    'XX.XX.........XX....X.....X.....XXX..X........X...X.XX...X.X..X...X......X....X..X..XX...X.....XXXX.',
    '..X..XXX....X.XX.XX....X.....XX......X.............X.X.X...XX.X.XX..X...XX..XX.....X..X......X.X..X.',
    'X.....X.....X......X........X..X...X.X.....X...........X..X....X...X..X......X.XX..X..X.X.....X.....',
    '.........X...X....X......X.....X...X.........X.....XXXX.......X.X.......X...X..X.XX...X..X......X.X.',
    '............X.....X..X....X....XX...X.....X.........X.X..X............X..X.....X...X..............X.',
    '.....X.X..X......X........X..........X......X......X.............X.X..X.....X.X...........X........X',
    '...X..............XX..X.........X............XXX..........X..........X...X..X.X.........X....XX...X.',
    '...................X......X....XX.......XX.....X....XX.X........X.....X..X.....X.X.XXX.....X........',
    '....X.X........XXX......X...X.X.....X.X............X.....X......X.X.XX......X.....X...XXX.........XX',
    '.X...XX...X.........................X......X....X.........XX........X....XX..X..XX.XX.......X...X.X.',
    '......X..X.X.................X..X.....X.X.....X....XX..X.X.XX....X.....X..X.X..X....X......X......X.',
    '...XXX........X........X.XX..X.........X.....X..X...............X........................XX..X......',
    '........X....X...X.....X......X.........................XX......XXX.X........X.X....X.X............X',
    '...X.X..X...X.......XXXX.......X.......X..XX.X...X......XX..X...X.XX..X......X......X..X.X..X.......',
    'X....X.......XXX.X..X.XX.XX...X.X.......XX.X..XX..........X.XX.X.X......X............X..X...X..XXX..',
    'XXX...............X...X....XXX.X...X.....X.....X.......XX..X....X.....X....X........................',
    'X....X......X....X...X..........X..........X..........XXX.........X...X....................X......X.',
    '...XX.......XX...XXXX..X.......X.X.......X.X.......X.X.......X...........XX......X........XX..X..X..',
    'X.X........XX.X.....X......X.X..X.......X...............X...XXXX...........X....X.....X......X......',
    '..X.....X........X..X....X.........XX.XXXX...X....X.X.....................X......X......XX.X...X.X..',
    '...X..XXX............X.....XX....................X..X..XXX....X...............X.....XX.............X',
    'XXXX....X...X...XX...X.............X.....X.....X..........XX..X................X.............X.X.X.X',
    '....X...................X...X......X......X......X..X..............X.......X........X..X.X......X...',
    '.....X.X.X.X........X...X...XX...XX.....XX........X.X..X..X....X.........X.X.......X..X...........X.',
    'X.......X.....X.........X.............X...X...........XX...X.X.XX.......X............X.........X.X..',
    '.....X..X.X..........XX.X......X....X.X.XXX......XX.....X.X...........X......X..........X.XXX.XX.X..',
    '................XX.....X..XX................XX..X....X............X..X..XX....X....X.......X....X..X',
    '.X.......X............X.X....................X........X..........X..............X........X..........',
    '........X.....X....X.X...X.X.....X.......X.X...X.....X.X..X.X.......X...X.....X........XX....X..X..X',
    'X....XX.X.X........XX.X...X......X...X.X....X...X....X...XX.X..........................X..X.X.X...X.',
    '..X...X.......................X......XX.......X..XX....X..X.X....X............X........X..XX....XX..',
    '.....X...X.................XX......X.......X....XXX......X.......X.........X...X.....X.X...X...X....',
    '....X....X..XXX..XX........XX..X.....X.X............X............X..................XX..........X...',
    'XX.....X...X.X....X....X..X...X....XX.....X.....X..X...X.X......X...........X...XX.X.....X..........',
    '.........X...X...X.X......X...........X.....X...XX.X....X.........X....X.....X..X.....X.....X..X....',
    '........XX..X......X..............X...X..........................................X...X.......XX.....',
    '.X.......X.....X..XX...XX........................X...X.............XX.....X...X................X....',
    '...X.......X.XX..X.X....X.......X..X...X.......X..X.X.....XX..X.XX.....X.......X.....X.....X...X...X',
    '...........X...X.X...X.X........X....X..X...X........XX.X...XX..X...X...X......X..XX.........X..X...',
    '...X.X....X.XX.X.....X........X.X.........X.......XX.......XX..X...XX.X....X......X...X...X.XXX.....',
    '......X.........X..X..X...X.......X...XXX....XXX........XX..........XX...X...................X....X.',
    '.X.X........XXXX.X....XX........X...........X......X......X.X...X.X....XX......X..X....X........X...',
    '...XXX...........X..X.....X.X........X..............X..........XX...X.X..X.X............X.......X...',
    'X.................X.XX..X......X.XXX........X.X...X....X.X...X.XXX..X............XX.......X...X..X..',
    '......X..XXXXXX..........XX..X...XX.....XXX.....X......X....X.X..X.X.....XXX.....X.XX...............',
    '...X........X...X.X.X................XX....X.X...X..........X......X..X...XX.X.XXX.X...X.......X....',
    '.....XX..X...X......X................X..........X....X.......X.X.....X..X..X..XX..XX.X...........X.X',
    '.X.........X....X....X.....X...X..X......X..X..X.....X.........XXX.................X.X......XX......',
    '...XX.X.X..X..X..X...X...XX............X..X..X....X......X..X...X.....X.............X...X......X....',
    'X.........XX.XX..X.....XX..X....X............X.........X.........X.X..X.....X............X.......X..',
    '..XX.XX........X.X.............X..........X....X.X..X.XXX.X....X.X............X.X.X....X...X........',
    '.X........X....XX..XX......X...X..X.........XXX.XX......X.XX...X...X.XX.........X.............X.....',
    '.X............X...X....X...X........X.................X.......X.X......X..X..X..................XXX.',
    '.X.X..X.X...........X.X.......XXX...X...........X.X.....X..X.X..X......X.X..............XX.....X...X',
    '.........X.X...X.......X.........X........X........XX....X...X.X.XXX.......X.............X..X.X.....',
    '.....................X...XX.X..X....X.........X......X.X..X...XX....X..........XX....X...XX.......X.',
    '.................XX...X......XX.X....X...X...........XX....X.X...X...XXX....X.X.X.X.X....XXX......X.',
    '..X.....X...X.....X.........X.....X.X.X.........X.....X.....X..............X.....X............XX.X..',
    '...............X....XX...............XX......X.........XX.............X.X.........X........X.X...X..',
    'X...XX.....X..........X.......X......XX....X......X.....X........X..X.X.......XX....................',
    '...X..X..XX.........X.X.....X.X.....X....X....X..X..X..............X.X.........X.X..XX.X.........X..',
    '.............X..XX..X.X...................................XX............XX..X..X.X..X.XX......X.....',
    'XX...X...X.X...X......X.....X.X...X.......X.X.X...XX......X..X...XX......X.....X....X............X.X',
    '............X................XX..XX..X..XX............................X...X..X........X....X.....XXX',
    '.......X..X.......X............X...X.....X............X....X..X...........X...X.........X...........',
    'X..X..X...X.......X....X.X.....XX............X.........X....XX.....X.X..X......X.X...X.X.X.X...X.XX.',
]
# grid = ['...XX', '...X.', '.X.X.', '.X...', '.X..X']
startX = 27
startY = 96
goalX = 94
goalY = 33


def minimumMoves(grid, startX, startY, goalX, goalY):
    # queueItem fromat: {x, y, directionFrom, setepCounter}
    unvisitedNodes = [{"x": startX, "y": startY,
                       "directionFrom":  '', "stepCounter": 0}]
    visitedNodes = [{"x": startX, "y": startY}]
    n = len(grid)
    counter = 0
    while(True):
        node = unvisitedNodes.pop(0)

        # append right
        if(node['y'] != n-1):
            for tempCounter in range(1, (n - node['y']) + 1):
                if (node['y'] + tempCounter < n):
                    if (grid[node['x']][node['y'] + tempCounter] == "X"):
                        break
                    if ({"x": node['x'], "y": node["y"] + tempCounter} not in visitedNodes):
                        if node['x'] == goalX and node["y"] + tempCounter == goalY:
                            return node['stepCounter'] if(node['directionFrom'] == 'right') else node['stepCounter'] + 1
                        if (node['x'] == 0 and grid[1][node['y'] + tempCounter] != "X" or node['x'] == n - 1 and grid[n - 2][node['y'] + tempCounter] != "X" or node['x'] != 0 and node['x'] != n - 1 and grid[node['x'] - 1][node['y'] + tempCounter] != 'X' or node['x'] != 0 and node['x'] != n - 1 and grid[node['x'] + 1][node['y'] + tempCounter] != 'X'):
                            unvisitedNodes.append({"x": node['x'], "y": node['y'] + tempCounter, "directionFrom": "right",
                                                   "stepCounter": node['stepCounter'] if(node['directionFrom'] == 'right') else node['stepCounter'] + 1})
                            visitedNodes.append(
                                {"x": node['x'], "y": node['y'] + tempCounter})
                else:
                    break

        # append left
        if (node['y'] != 0):
            for tempCounter in range(1, (node['y']) + 1):
                if (node['y'] - tempCounter >= 0):
                    if(grid[node['x']][node['y'] - tempCounter] == "X"):
                        break
                    if ({"x": node['x'], "y": node["y"] - tempCounter} not in visitedNodes):
                        if node['x'] == goalX and node["y"] - tempCounter == goalY:
                            return node['stepCounter'] if(node['directionFrom'] == 'left') else node['stepCounter'] + 1
                        if (node['x'] == 0 and grid[1][node['y'] - tempCounter] != "X" or node['x'] == n - 1 and grid[n - 2][node['y'] - tempCounter] != "X" or node['x'] != 0 and node['x'] != n - 1 and grid[node['x'] - 1][node['y'] - tempCounter] != 'X' or node['x'] != 0 and node['x'] != n - 1 and grid[node['x'] + 1][node['y'] - tempCounter] != 'X'):
                            unvisitedNodes.append({"x": node['x'], "y": node['y'] - tempCounter, "directionFrom": "left",
                                                   "stepCounter": node['stepCounter'] if(node['directionFrom'] == 'left') else node['stepCounter'] + 1})
                            visitedNodes.append(
                                {"x": node['x'], "y": node['y'] - tempCounter})
                else:
                    break

        # append up
        if (node['x'] != 0):
            for tempCounter in range(1, (node['x']) + 1):
                if (node['x'] - tempCounter >= 0):
                    if(grid[node['x'] - tempCounter][node['y']] == "X"):
                        break
                    if ({"x": node['x'] - tempCounter, "y": node["y"]} not in visitedNodes):
                        if node['x'] - tempCounter == goalX and node["y"] == goalY:
                            return node['stepCounter'] if(node['directionFrom'] == 'up') else node['stepCounter'] + 1
                        if (node['y'] == 0 and grid[node['x'] - tempCounter][1] != "X" or node['y'] == n - 1 and grid[node['x'] - tempCounter][n - 2] != 'X' or node['y'] != 0 and node['y'] != n - 1 and grid[node['x'] - tempCounter][node['y'] - 1] != 'X' or node['y'] != 0 and node['y'] != n - 1 and grid[node['x'] - tempCounter][node['y'] + 1] != 'X'):
                            unvisitedNodes.append({"x": node['x'] - tempCounter, "y": node['y'], "directionFrom": "up",
                                                   "stepCounter": node['stepCounter'] if(node['directionFrom'] == 'up') else node['stepCounter'] + 1})
                            visitedNodes.append(
                                {"x": node['x'] - tempCounter, "y": node['y']})
                else:
                    break

        # append down
        if (node['x'] != n-1):
            for tempCounter in range(1, (n - node['x']) + 1):
                if (node['x'] + tempCounter < n):
                    if(grid[node['x'] + tempCounter][node['y']] == "X"):
                        break
                    if ({"x": node['x'] + tempCounter, "y": node["y"]} not in visitedNodes):
                        if node['x'] + tempCounter == goalX and node["y"] == goalY:
                            return node['stepCounter'] if(node['directionFrom'] == 'down') else node['stepCounter'] + 1
                        if (node['y'] == 0 and grid[node['x'] + tempCounter][1] != "X" or node['y'] == n - 1 and grid[node['x'] + tempCounter][n - 2] != 'X' or node['y'] != 0 and node['y'] != n - 1 and grid[node['x'] + tempCounter][node['y'] - 1] != 'X' or node['y'] != 0 and node['y'] != n - 1 and grid[node['x'] + tempCounter][node['y'] + 1] != 'X'):
                            unvisitedNodes.append({"x": node['x'] + tempCounter, "y": node['y'], "directionFrom": "down",
                                                   "stepCounter": node['stepCounter'] if(node['directionFrom'] == 'down') else node['stepCounter'] + 1})
                            visitedNodes.append(
                                {"x": node['x'] + tempCounter, "y": node['y']})
                else:
                    break


start_time = time.time()
print(minimumMoves(grid, startX, startY, goalX, goalY))
print("--- %s seconds ---" % (time.time() - start_time))
