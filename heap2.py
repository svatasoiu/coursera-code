#Heaping
from heapq import *

file = open('MedianData.txt')
##leftSize = 0
##rightSize = 0

leftHeap = []
rightHeap = []

medians = []

count = 0

#special case for first number
n0 = int(file.readline())
heappush(rightHeap, n0)

medians.append(n0)
count += 1
##rightSize += 1
##print(n0)

for i in file:
    n = int(i)
    #inserting integer
    if n > rightHeap[0]:
        heappush(rightHeap, n)
    else:
        heappush(leftHeap, -n)

    count += 1
    
    #balancing heaps
    if len(rightHeap) > len(leftHeap) + 1:
        toMove = heappop(rightHeap)
        toMove *= -1
        heappush(leftHeap, toMove)
    elif len(leftHeap) > len(rightHeap) + 1:
        toMove = heappop(leftHeap)
        toMove *= -1
        heappush(rightHeap, toMove)

    if count % 2 == 0:
        medians.append(-leftHeap[0])
    else:
        if len(rightHeap) > len(leftHeap):
            medians.append(rightHeap[0])
        else:
            medians.append(-leftHeap[0])

#for each integer:
#left heap is a max-heap => must negate all values
    #add to heaps:
    #   if x > right.min:
    #       add to right heap
    #   else:
    #       add to left heap
#
#   balance heaps
#       if size(right) > size(left) + 1: (right is heavy)
#           move_min_of_right_to_left() (negate value before pushing to left!)
#       if size(left) > size(right) + 1: (left is heavy)
#           move_max_of_left_to_right() (negate value before pushing to right!)
