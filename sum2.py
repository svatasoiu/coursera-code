from time import time

class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
        #self.parent = parent
    def insert(self, data):
        if data < self.data:
            if self.left is None:
                self.left = Node(data)
            else:
                self.left.insert(data)
        else:
            if self.right is None:
                self.right = Node(data)
            else:
                self.right.insert(data)
    
def getRange(root, lower, upper, s = set()):
    if (root == None):
        return s
    
    if (lower <= root.data) and (root.data <= upper):
        s.add(root.data)

    if (lower < root.data):
        getRange(root.left, lower, upper, s)

    if (root.data < upper):
        getRange(root.right, lower, upper, s)
 
file = open('week6Data.txt')
root = Node(int(file.readline()))
numSet = set()

for line in file:
    n = int(line)
    root.insert(n)
    numSet.add(n)

ran = 200001
pT = set(range(-10000, 10001))

print("Done Processing!")

totals = {t: False for t in pT}
for x in numSet:
    r = set()
    getRange(root, x - ran, x + ran, r)
    getRange(root, -x - ran, -x + ran, r)
    #print(x,r)
    for y in r:
        if x + y in pT:
            totals[x + y] = True

