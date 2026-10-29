# selection sort

def selectionsort(arr):
    n = len(arr)
    for i in range(n-1):
        min_pos = i
        for j in range(i+1, n):
            if arr[j] < arr[min_pos]:
                min_pos = j

        arr[i],arr[min_pos] = arr[min_pos],arr[i]

arr = [6,4,7,3,5,1,6,9,8]
selectionsort(arr)
print(arr)