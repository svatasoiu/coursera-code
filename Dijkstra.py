#Dijkstra
from time import time
start = time()
file = open('dijkstraData.txt')
graphData = []

for row in file:
    graphData.append(row.split('\t')[1:-1])

for i in range(len(graphData)):
    for j in range(len(graphData[i])):
        d = graphData[i][j].split(',')
        graphData[i][j] = (int(d[0])-1,int(d[1])) #first is tail vertex, second is length

def Dijkstra(graph, source = 0):
    A = [0] * len(graph) #length of path to each node
    searchedGraph = set([source])
    unsearchedGraph = set(range(source + 1, len(graph))) # every node except source
    while len(unsearchedGraph) > 0:
        #look at all vertices, v, in searched graph
        #compute minimum Greedy Dijkstra Score for all
        #edges that have outgoing edges, such that w is in unsearchedGraph:
        #Value = A[v] + length(v -> w)
        minEdge = []
        minVal = 10000
        for v in searchedGraph: #head node
            for w in graph[v]:
                #print(str(v) + ' -> ' +str(w))
                if w[0] in unsearchedGraph:
                    if A[v] + w[1] < minVal:
                        minEdge = [v, w[0]]
                        minVal = A[v] + w[1]
        v = minEdge[0]
        w = minEdge[1]
        #print('\nFinal')
        #print(v,w)
        A[w] = minVal
        searchedGraph.add(w)
        #print(searchedGraph)
        unsearchedGraph.remove(w)
    return A
print(time() - start)
A = Dijkstra(graphData)
print(time() - start)
for i in range(len(A)):
    print('1 -> ' + str(i+1) + ': ' + str(A[i]))
