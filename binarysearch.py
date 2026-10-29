#1. Implement Binary Search algorithm for a given sorted sequence to find a given key and to display its index if the key is found.

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while(low <= high):
        mid = low+(high-low)//2

        if(arr[mid] == target):
            print(mid)
            return mid
        elif(arr[mid] > target):
            high = mid - 1
        else:
            low = mid + 1


#input
arr = [2,4,5,7,8,9,11,16,24]
target = 5

binary_search(arr,target)