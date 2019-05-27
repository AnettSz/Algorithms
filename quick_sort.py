#sym elements in array
def suma(arr):
    total = 0
    for i in arr:
        total += i
    print(total)

#sum elements in array        
def rsum(arr):
    if len(arr) ==1:
        return arr[0]
    else:
        return arr[0] + rsum(arr[1:])


#count elements in array
def count(arr):
    if arr == []:
        return 0
    return 1 + count(arr[1:])


suma([1,2,3,4,5])
print(rsum([1,2,3,4,5,6,7]))
print(count([1,2,3,4,5,6,7]))

#find max element in array
def findmax(arr):
    
    if len(arr) == 2:
        return arr[0] if arr[0] > arr[1] else arr[1]
    sub_max = findmax(arr[1:])
    return arr[0] if arr[0] > sub_max else sub_max

print(findmax([1,2,34 ,4,5,6,7]))


#sort elements in array with quicksort algorithm
def quicksort(arr):
    
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot]
        greater = [i for i in arr[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)


print(quicksort([9,2,34 ,4,5,1,7]))    
        
