# bubble sort

def bubblesort(arr):
    n = len(arr)

    for i in range(n-1):
        swap = False
        for j in range(n -i -1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
                swap = True

        if swap == False:
            break


# input
arr = [6,4,7,2,9,7,5]
bubblesort(arr)
print(arr)