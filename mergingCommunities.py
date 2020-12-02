# Enter your code here. Read input from STDIN. Print output to STDOUT
n = input().split()
q = int(n.pop(1))
n = int(n[0])
communities = []
people = {}
for number in range(n):
    people[str(number + 1)] = str(number)
    communities.append([number + 1])
for query in range(q):
    tempQ = input().split()
    if (tempQ[0] == 'M'):
        if (people[tempQ[1]] != people[tempQ[2]]):
            temp = int(people[tempQ[2]])
            communities[int(people[tempQ[1]])
                        ] += communities[int(people[tempQ[2]])]
            for person in communities[int(people[tempQ[2]])]:
                people[str(person)] = people[tempQ[1]]
            communities[temp] = []
    elif (tempQ[0] == 'Q'):
        print(len(communities[int(people[tempQ[1]])]))
