#insertion sort

def insertion(arr):
   
    for i in range(1,len(arr)):
        key=arr[i]
        j=i-1
        while j>=0 and key<arr[j]:
            arr[j+1]=arr[j]
            j=j-1
        arr[j+1]=key
    return arr
size=int(input("enter the size of the array"))
arr=[]

for num in range(size):
    num=int(input("enter the elements"))
    arr.append(num)
print(insertion(arr))
            

