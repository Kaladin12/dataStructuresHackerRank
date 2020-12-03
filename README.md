# Data Structures project #
This is our exam/project which consisted of six Hacker Rank problems that we had to solve as a team. Here is the explanation for each of the problems:
## Problem 1: Cycle detection. ##
This problem wasn't difficult because we had already done a cycle queue, therefore we only checked if every node's next node and added it to a list iteratively. If a node's next
was already on the list it was a cycle, while if the node's next was "None" meant the queue had an end, in which case it was not a cycle queue.
## Problem 2: Is This a Binary Search Tree? ##
Explanation
## Problem 3: Castle on the grid. ##
This one was very fun to solve. When a castle is placed on the grid it can move to any position in it's "x" and "y" axis, therefore we added all those positions to a queue to 
repeat the same process with them until an "X" was found. In order to make the algorithm more efficient, we skiped nodes that had an interruped path, which meaned that they were
not going to contribute to the solution of the problem. Also, we saved the direction of the move to sum 1 to the counter in the case that the direction changed, because the 
castle does not take single steps, it moves all along it's axis.
## Problem 4: Balanced Brackets. ##
Explanation
## Problem 5: Merging Communities. ##
This one was tricky. The obvious solution was to make a list to save the communities and search for the items manually, but it was not efficient enough. What we did was to save
them in a list, but also made a dictionary that saved the index of the community that an item belongs to. By that way it was easy to found the items in the array fast, but with
every merge you must change the value of the community in the dictionary for every node, but even taing that into account, it was much faster than doing it iteratively.
### Problems: ###
Python was not fast enough to suit the problem's requierements, so even though it solves the problem for any case, it does not accomplish the task on time always.
## Problem 6: Savita And Friends. ##
Explanation
### Problems: ###
Python was not fast enough to suit the problem's requierements, so even though it solves the problem for any case, it does not accomplish the task on time always.
## Team members: ##
* Aviles Ulises
* Cruz Elian
* Cruz Daniel
* Dennis David
