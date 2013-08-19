from graphClasses import Node, Graph

graphFile = open('kargerMinCut.txt')
graphData = []
for row in graphFile:
    graphData.append(row.split('\t')[:-1])
    #graphData.append(map(int, row.split('\t')[:-1]))

for i in range(len(graphData)):
    for j in range(len(graphData[i])):
        graphData[i][j] = int(graphData[i][j])
        
graph = Graph()

cuts = []
graphs = []
for i in range(100):
    print("Graph: " + str(i+1) + " contracting...")
    graphs.append(Graph())
    
    for node in graphData:
        graphs[i].addNode(Node(node[0], node[1:]))

    graphs[i].randomizedContraction()
    cuts.append(len(graphs[i].nodes[0].adj))
    print(str(cuts[i]) + " connections")
    
print("\n\nMin Cut = " + str(min(cuts)))
