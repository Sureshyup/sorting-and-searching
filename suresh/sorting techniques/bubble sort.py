#bubble sort

def bubble(arr):
    n=len(arr)
    for i in range(0,n-1,1):
        for j in range(0,n-1,1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]

size=int(input("enter the size"))
arr=[]

for num in range(size):
    num=int(input("enter the elements"))
    arr.append(num)

result=bubble(arr)
print(arr)
