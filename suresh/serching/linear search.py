def linear_search(arr,target):
    for i in range(len(arr)):
        if arr[i]==target:
           return i
    return -1
            
    
size=int(input("enter the number"))
arr=[]

for num in range(size):
    num=int(input("enter the elements"))
    arr.append(num)
                
target=int(input("search the element"))
result=linear_search(arr,target)

if result != -1:
    print(f"Element found at index: {result}")
else:
    print("Element not found ")


