#subtract one from each node id in SCC.txt!!!
from time import time
import sys, resource
sys.setrecursionlimit(10**6)
resource.setrlimit(resource.RLIMIT_STACK, (2**29, 2**30))
print("Starting Data Parsing...")
start = time()
N = 875714

#round 1: [explored, leader]
revGraph = [[0] for i in range(N)]
graphData = [[0, -1] for i in range(N)]

#round 2: [explored, time, leader]
graphorder2 = [] #[[0, -1, -1] for i in range(N)]

graphFile = open('SCC.txt')
for row in graphFile:
    r = row.split(' ')
    n = int(r[0])-1
    e = int(r[1])-1
    graphData[n].append(e)
    revGraph[e].append(n)

print("TXT Parsed: " + str(time()-start))

#t = 0
s = -1
#c = 0
def DFS_loop_1():
    global s#, c, start
    #c = 0
    #start = time()
    for i in range(N):
        j = N - i - 1
        #print("Processing Node " + str(i))
        if revGraph[j][0] == 0:
            s = j
            #c+=1
            DFS_1(j)
        #if c%10000==0:
            #print("Processed " + str(c) + " nodes @ " + str(time()-start) + "s")
            #start = time()
        #print("Processed " + str(c) + " nodes")

def DFS_1(i):
    global s#, c
    #c += 1
    revGraph[i][0] = 1
    graphData[i][1] = s
    if len(revGraph[i]) > 1:
        outgoing = revGraph[i][1:]
        for arc in outgoing:
            if revGraph[arc][0] == 0:
                DFS_1(arc)

    #t += 1
    #so, first nodes in graphData2 will be lowest finishing time
    #in DFS_2 run in reverse order
    graphorder2.append(i) #[0, t, s] + outgoing)

def DFS_loop_2():
    global s, graphorder2#, c
    #c = 0
    graphorder2.reverse()
    for nodeID in graphorder2:
        if graphData[nodeID][0] == 0:
            s = nodeID
            DFS_2(nodeID)
        #if c%10000==0:
        #    print("Processed " + str(c) + " nodes @ " + str(time()-start) + "s")
            

def DFS_2(i):
    global s#, c
    #c += 1
    graphData[i][0] = 1
    graphData[i][1] = s
    
    if len(graphData[i]) > 2:
        outgoing = graphData[i][2:]
        for arc in outgoing:
            if graphData[arc][0] == 0:
                DFS_2(arc)
                
def Kosaraju():
    #reverse graph
    DFS_loop_1()
    print("Loop 1 Done!" + str(time()-start))
    DFS_loop_2()
    print("Loop 2 Done!" + str(time()-start))

Kosaraju()
a = [b[1] for b in graphData]
c = set(a)
d = {x: 0 for x in c}
for y in a:
    d[y] += 1
    
vals = list(d.values())

maxList = []
for i in range(5):
    maxList.append(max(vals))
    vals.remove(maxList[i])

print("Everything Done!" + str(time()-start))
print(maxList)
