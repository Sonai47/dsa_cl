# quicksort
def partition(a,low,high):
    pivot = a[high]
    i = low -1

    for j in range(low,high):
        if a[j] <= pivot:
            i = i+1
            a[i],a[j] = a[j],a[i]

    a[i+1],a[high] = a[high],a[i+1]

    return i+1

def quicksort(a,low,high):
    if low < high:
        p = partition(a,low,high)

        quicksort(a,low,p-1)
        quicksort(a,p+1,high)

arr = [7,4,6,3,5,8]
quicksort(arr,0,len(arr)-1)
print(arr)
