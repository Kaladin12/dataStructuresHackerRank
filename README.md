# Data Structures project #
This is our exam/project which consisted of six Hacker Rank problems that we had to solve as a team. Here is the explanation for each of the problems:
## Problem 1: Cycle detection. ##
This problem wasn't difficult because we had already done a cycle queue, therefore we only checked if every node's next node and added it to a list iteratively. If a node's next
was already on the list it was a cycle, while if the node's next was "None" meant the queue had an end, in which case it was not a cycle queue.
## Problem 2: Is This a Binary Search Tree? ##
This problem was almost an implementation of our binary search tree written in java, with the only excepction that we only needed to know whether the given tree was a bst or not, therefore, we used an in order traversal to enlist the items in a python list, then, we checked with a for loop if the value of every node was greater or equal than its following node, if so, the given tree wasn't a bst, else, it was.
## Problem 3: Castle on the grid. ##
This one was very fun to solve. When a castle is placed on the grid it can move to any position in it's "x" and "y" axis, therefore we added all those positions to a queue to 
repeat the same process with them until an "X" was found. In order to make the algorithm more efficient, we skiped nodes that had an interruped path, which meaned that they were
not going to contribute to the solution of the problem. Also, we saved the direction of the move to sum 1 to the counter in the case that the direction changed, because the 
castle does not take single steps, it moves all along it's axis.
## Problem 4: Balanced Brackets. ##
This problem required us to know whether a string containing brackets (parentheses, braces and brackets) was balanced, namely, that there was an open and a closed bracket in the right place (there always has to be both). To do it, we used a python list as a stack where we entered only open brackets, if a closed bracket was found it should be the same type of bracket than the item popped from the stack, if not, the string was not balanced. We only had to consider two special cases: if the first appearing bracket was a closed bracket, and if the last item on the string was an open bracket (in both cases the string is unbalanced) . These special cases allowed us to return faster the right answer to these cases.
## Problem 5: Merging Communities. ##
This one was tricky. The obvious solution was to make a list to save the communities and search for the items manually, but it was not efficient enough. What we did was to save
them in a list, but also made a dictionary that saved the index of the community that an item belongs to. By that way it was easy to found the items in the array fast, but with
every merge you must change the value of the community in the dictionary for every node, but even taing that into account, it was much faster than doing it iteratively.
### Problems: ###
Python was not fast enough to suit the problem's requierements, so even though it solves the problem for any case, it does not accomplish the task on time always.
## Problem 6: Savita And Friends. ##
This was a very tricky problem because it required us to find a point along certain edge of a connected graph where the maximum distance to all of the nodes in the graph were minimized. To solve it, we needed to know the shortest distance from every node connected to the required edge, to the rest of the nodes in the graph, to do so, we used the dijkstra algorithm to determine this distance.
Once we knew the shortest distance from to each node of the graph, starting from both nodes connected to the given edge, we proceeded to find the point of shortest maximum distance; we used a modified bisection function to find such point. Fisrt of all, we checked wheter the middle point was the answer, if not, we had to check which of the halves on the given range (initially 0 to the edge length) gave us the minimum maximum distance, from that, we iterated changing the limits of search until we found a difference between the values given by both halves of less or equal than 0.00001 (the values converged to the given point as if they were the root of a function). This process allowed us to calculate at the same time the maximum distance from the point found to the rest of the nodes in graph.
### Problems: ###
Our Python implementation was not fast enough to suit the problem's requirements, so even though it solves the problem, it does not accomplish the task on time always, an example of this is with the given datasets with 100000 roads (edges), which lasted very long to finish, that's why our final image only shows as passed the test cases that doesn't contain datasets with 100000 edges in the graph.
## Team members: ##
* Aviles Ulises
* Cruz Elian
* Cruz Daniel
* Dennis David
.
