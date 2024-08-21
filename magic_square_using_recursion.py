n = int(input("enter size of matrix:"))
def magic_square(n):
    l = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(0)
        l.append(row)
    i = n//2
    j = n-1
    num = n*n
    magic(l,n,i,j,1,num)
    for i in range(n):
        for j in range(n):
            print(l[i][j], end=" ")
        print()
def magic(l,n,i,j,cnt,num):
    if cnt>num:
        return
    if(i==-1 and j==n): # and condition should come first
        i=0
        j=n-2
    elif(i==-1):
        i=n-1
    elif(j==n):
        j=0
    if(l[i][j] != 0):
        i+=1
        j-=2
        # continue
    else:
        l[i][j]=cnt
        cnt+=1
        i-=1
        j+=1
    magic(l,n,i,j,cnt,num)
magic_square(n)

