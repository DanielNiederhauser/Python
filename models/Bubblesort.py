def bubblesort(arr):
    l = len(arr)

    for i in range(l):
        for j in range(0, l-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def insertionSort(arr):

    for i in range(1, len(arr)):

        key = arr[i]

        j = i-1
        while j >= 0 and key < arr[j] :
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def selectionsort(A):
    for i in range(len(A)):


        min_idx = i
        for j in range(i+1, len(A)):
            if A[min_idx] > A[j]:
                min_idx = j


        A[i], A[min_idx] = A[min_idx], A[i]

def printOG():
    print("ausgangsarr:")
    for i in range(len(arr)):
        print(arr[i])

import copy
arr = [50,20,32,2,5,10,20,2,16,65]
temp = copy.deepcopy(arr)

bubblesort(arr)
print("Sortiertes Bubblesort Arr: ")
for i in range(len(arr)):
    print(arr[i])
arr = copy.deepcopy(temp)
printOG()
selectionsort(arr)

print("Sortiertes Selectionsort Arr: ")
for i in range(len(arr)):
    print(arr[i])
arr = copy.deepcopy(temp)
printOG()
insertionSort(arr)

print("Sortiertes Insertionsort Arr: ")
for i in range(len(arr)):
    print(arr[i])
arr = copy.deepcopy(temp)
printOG()