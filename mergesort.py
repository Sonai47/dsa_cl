# merge sort
def merge(arr,low,mid,high):
    temp = []
    i=low
    j=mid+1

    while i<=mid and j<=high:
        if arr[i] <= arr[j]:
            temp.append(arr[i])
            i = i + 1
        else:
            temp.append(arr[j])
            j = j + 1

    while i<=mid:
        temp.append(arr[i])
        i = i + 1
    while j<=high:
        temp.append(arr[j])
        j = j + 1

    k = 0
    for i in range(low,high+1):
        arr[i] = temp[k]
        k = k + 1

def mergesort(arr,low,high):
    if low < high:
        mid = (low+high)//2

        mergesort(arr,low,mid)
        mergesort(arr,mid+1,high)
        merge(arr,low,mid,high)


arr = [5,4,9,6,2]
mergesort(arr,0,len(arr)-1)
print(arr)