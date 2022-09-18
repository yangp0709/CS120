from asyncio import base_tasks
import math
import time
import random

"""
See below for mergeSort and countSort functions, and for a useful helper function.
In order to run your experiments, you may find the functions random.randint() and time.time() useful.

In general, for each value of n and each universe size 'U' you will want to
    1. Generate a random array of length n whose keys are in 0, ..., U - 1
    2. Run count sort, merge sort, and radix sort ~10 times each,
       averaging the runtimes of each function. 
       (If you are finding that your code is taking too long to run with 10 repitions, you should feel free to decrease that number)

To graph, you can use a library like matplotlib or simply put your data in a Google/Excel sheet.
A great resource for all your (current and future) graphing needs is the Python Graph Gallery 
"""
arr = [211, 122, 213, 433]

def merge(arr1, arr2):
    sortedArr = []

    i = 0
    j = 0
    while i < len(arr1) or j < len(arr2):
        if i >= len(arr1):
            sortedArr.append(arr2[j])
            j += 1
        elif j >= len(arr2):
            sortedArr.append(arr1[i])
            i += 1
        elif arr1[i][0] <= arr2[j][0]:
            sortedArr.append(arr1[i])
            i += 1
        else:
            sortedArr.append(arr2[j])
            j += 1

    return sortedArr

def mergeSort(arr):
    if len(arr) < 2:
        return arr

    midpt = int(math.ceil(len(arr)/2))

    half1 = mergeSort(arr[0:midpt])
    half2 = mergeSort(arr[midpt:])

    return merge(half1, half2)

def countSort(univsize, arr):
    universe = []
    for i in range(univsize):
        universe.append([])

    for elt in arr:
        universe[elt[0]].append(elt)

    sortedArr = []
    for lst in universe:
        for elt in lst:
            sortedArr.append(elt)

    return sortedArr

def BC(n, b, k):
    if b < 2:
        raise ValueError()
    digits = []
    for i in range(k):
        digits.append(n % b)
        n = n // b
    if n > 0:
        raise ValueError()
    return digits

def RadixSort(univsize, b, A):

    n = len(A)
    output = []
    k = math.ceil((math.log(univsize)/ math.log(b)))

    for i in range (n):
        flip = BC(A[i][0],b,k)
        A[i].append((A[i][1], flip, A[i][0]))
        del (A[i][1])
    
    for j in range (k):
        for i in range (n):
            A[i][0] = A[i][1][1][j]  
        A = countSort(b, A)

    for i in range (n):
        output.append((A[i][1][-1], A[i][1][0]))
           
    return output    

# A = [[123, 2], [478, 4], [972, 6], [821, 5]]
# print(RadixSort(999, 10, A))





for x in range(1, 17):
    n = 2**x
    for y in range(1, 21):
        U = 2**y

        A = []
        mstime =[]
        mctime = []
        mrtime = []

        for i in range(n):
            k = random.randint(0, (U-1))
            v = random.randint(0, U)
            A.append([k,v])

        for i in range(10):
            t0 = time.time()
            mergeSort(A)
            t1 = time.time()
            mstime.append(t1-t0)

        for i in range(10):
            t2 = time.time()
            countSort(U,A)
            t3 = time.time()
            mctime.append(t3-t2)

        for i in range(10):
            t4 = time.time()
            RadixSort(U,n,A)
            t5 = time.time()
            mrtime.append(t5-t4)

        avg_m = sum(mstime)/10
        avg_c = sum(mctime)/10
        avg_r = sum(mrtime)/10

        fastest = min(avg_m, avg_c, avg_r)

        if fastest == avg_m:
            name = "M"
        elif fastest == avg_c:
            name = "C"
        else: name = "R"
    
        print("n:", math.log2(n), "U:", math.log2(U), name)
        

    


