import random
class Node:
    def __init__(self, _n, _adj = []):
        self.id = _n
        self.adj = _adj
        
    def addRef(self, n):
        self.adj.append(n)
        
    def removeRef(self, n):
        self.adj.remove(n)

class Graph:
    def __init__(self):
        self.nodes = []

    def addNode(self, node):
        self.nodes.append(node)

    def removeNode(self, node):
        self.nodes.remove(node)
    
    def getNode(self, n):
        for node in self.nodes:
            if node.id == n:
                return node
            
    def contract(self, node1, node2):
        for nodeID in node2.adj:
            if nodeID != node1.id: #make sure not to add self-loops
                #add node2 ID's to node1
                node1.addRef(nodeID)

                #remove node2 ID's from other nodes
                otherNode = self.getNode(nodeID)
                otherNode.removeRef(node2.id)

                #update reference in other nodes to node1's id
                otherNode.addRef(node1.id)
        #remove all references to node2 in node1
        while node2.id in node1.adj:
            node1.removeRef(node2.id)
        self.removeNode(node2)
            

    def randomizedContraction(self):
        #repeatedly call contract until only two nodes left
        #pick random node; chose one of neighbors randomly
        while len(self.nodes) > 2:
            node1ID = random.randint(0, len(self.nodes) - 1)
            node1 = self.nodes[node1ID]
            node2ID = random.randint(0, len(node1.adj) - 1)
            node2 = self.getNode(node1.adj[node2ID])
            self.contract(node1, node2)
        return self
