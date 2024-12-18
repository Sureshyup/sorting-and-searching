#selection sort

def select(arr):
    n=len(arr)
    for i in range(n):
        min_index=i
        for j in range(i+1,n):
            if arr[j]<arr[min_index]:
                min_index=j
        arr[i],arr[min_index]=arr[min_index],arr[i]

size=int(input("enter the size"))
arr=[]

for num in range(size):
    num=int(input("enter the elements"))
    arr.append(num)

result=select(arr)
print(arr)
