def binary_Search(arr,x,left,right):
  if left==right:
    if(arr[left]==x):
      return left
    else:
      return -1
  else:
    mid  = int((left+right)/2)
    if arr[mid]==x:
      return mid
    elif arr[mid]>x:
      return binary_Search(arr,x,left,mid-1)
    else:
      return binary_Search(arr,x,mid+1,right)

arr = [int(i) for i in input().split()] # input sorted list
x = int(input("Enter search key:"))
index = binary_Search(arr,x,0,len(arr)-1)
if index==-1:
  print(x,"not found")
else:
  print(x,"is found at",index+1)
