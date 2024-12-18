#quick sort

def quick(arr):
    if len(arr)<=1:
        return arr
    pivot=arr[len(arr)//2]

    left=[x for x in arr if x<pivot]
    middle=[x for x in arr if x==pivot]
    right=[x for x in arr if x>pivot]

    return quick(left)+middle+quick(right)
size=int(input("enter the size of the array"))
arr=[]

for num in range(size):
    num=int(input("enter the elements"))
    arr.append(num)
print(quick(arr))
    
