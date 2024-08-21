# in magic square, magic no. is m = n(n^2+1)/2
# in any magic square, 1 is located at position (n/2, n-1) for any n*n matrix(Assume 0-based indexing)

# let's say the position of 1 is (n/2, n-1) is (p,q) then next number which is 2 is located at (p-1,q+1) position.

# now follow just above step for similarly for finding other numbers
# example:- 1 is at (1,2) then 2 will be at (0,3) means (0,0) then 3 will be at (2,1) i.e same (p-1,q+1)
# Anytime if the calculated row position becomes -1 then make it n-1 and if column position becomes n then make it 0.

# if the calculated position already contains a number then decrement the column by 2 and increment the row by 1.

# if anytime row position becomes -1 and column becomes n, switch it to (0,n-2)

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
    cnt = 1

    while(cnt<=num):
        
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
            continue
        else:
            l[i][j]=cnt
            cnt+=1
        i-=1
        j+=1

    for i in range(n):
        for j in range(n):
            print(l[i][j], end=" ")
        print()

    print("The sum of each row/column/diagonal is: "+str((n*(pow(n,2)+1))//2))

    # we can use ** for exponential

# another way to initialize the matrix with element 0
# l = [[0 for i in range(3)]for j in range(3)]

magic_square(n)

"""
The code you've written is designed to generate a magic square using the "Siamese method," which is a specific algorithm that works only for odd-order magic squares (e.g., 3x3, 5x5). This method is not applicable to even-sized matrices because of the way it handles the placement of numbers.
"""
