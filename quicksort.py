count = 0

f = open('QuickSortData.txt')
L = []
for number in f:
    L.append(int(number))
#print(L)

def quickSort(L):
    global count
    
    if len(L) <= 1:
        return L
    
    #swap(L, 0, len(L) - 1) #last element is pivot, problem 2
    #p = midOf3(L)
    #swap(L, 0, p)
    
    (L,p) = partition(L, 0, len(L)-1)
    count += len(L) - 1
    #print("\n")
    #print(L,p)
    
    return quickSort(L[:p]) + [L[p]] + quickSort(L[p+1:])

def midOf3(A):
    if len(A) % 2 == 0:
        m = len(A) // 2 - 1
    else:
        m = len(A) // 2
    a = A[0]
    b = A[m]
    c = A[len(A) - 1]
    if (a > b and a < c) or (a < b and a > c):
        return 0
    elif (b > a and b < c) or (b < a and b > c):
        return m
    else:
        return len(A) - 1
    
def swap(L, i, j):
    if i == j:
        return
    L[i] += L[j]
    L[j] = L[i] - L[j]
    L[i] -= L[j]

def partition(A, l, r):
    global count
    p = A[l]
    i = l+1
    for j in range(l+1, r+1):
        #print A,i,j
        if A[j] < p:
            swap(A, i, j)
            i += 1
    swap(A, l, i-1)
    return A,i-1

           
#L = [5, 4, 3, 12, 21]
#print(partition(L, 0, len(L)-1))
print(quickSort(L))
