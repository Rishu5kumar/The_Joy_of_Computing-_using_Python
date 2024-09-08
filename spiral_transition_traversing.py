import turtle
turtle.bgcolor("black") # for changing bg color
spiral = turtle.Turtle()
from random import randint

width = 5
height = 7
dot_distance = 25

spiral.penup()
list_color = ["white", "yellow", "brown", "red", "blue", "green", "pink", "violet", "grey", "orange"]
spiral.setpos(-250, 250) # it always start from center(0,0)

# def spiral_traversing(arr, row, col):
def spiral_traversing_dot(row, col):
    top, bottom = 0, row-1
    left, right = 0, col-1

    f = 0
    # spiral.color("white")
    color_ind = randint(0,9)
    spiral.color(list_color[color_ind])
    while(left<=right and top<=bottom):
        if f==1:
            spiral.right(90)
        for i in range(left,right+1):
            spiral.dot()
            spiral.forward(dot_distance)
            #print(arr[top][i], end=" ")
        top+=1
        f = 1

        spiral.right(90)
        color_ind = randint(0,9)
        spiral.color(list_color[color_ind])
        for i in range(top,bottom+1):
            spiral.dot()
            spiral.forward(dot_distance)
            # print(arr[i][right], end=" ")
        right-=1

        spiral.right(90)
        color_ind = randint(0,9)
        spiral.color(list_color[color_ind])
        if(top<=bottom):
            for i in range(right,left-1,-1):
                spiral.dot()
                spiral.forward(dot_distance)
                # print(arr[bottom][i], end=" ")
            bottom-=1

        spiral.right(90)
        color_ind = randint(0,9)
        spiral.color(list_color[color_ind])
        if(left<=right):
            for i in range(bottom, top-1, -1):
                spiral.dot()
                spiral.forward(dot_distance)
                # print(arr[i][left], end=" ")
            left+=1

row = int(input("Enter row of a matrix:"))
col = int(input("Enter column of a matrix:"))
spiral_traversing_dot(row,col)
turtle.done()
'''
arr = []
count = 1
for i in range(row):
    arr_row = []
    for j in range(col):
        # element = int(input())
        arr_row.append(count)
        count += 1
    arr.append(arr_row)
print("Matrix elements are in spiral order is:")
spiral_traversing(arr,row,col)
'''

'''
# a turtle is a kind of pen which works on the canvas
tur = turtle.Turtle() # my turtle has been created

# creating simple square box
for i in range(5):
    # i will forward my pen which is tur on my canvas at some predefined starting position
    tur.forward(50)
    # after it got provided with 50 units i will turn this pen position within angle of 90 degree
    # tur.right(90) # it always take parameter as an angle and create a square
    tur.right(144) # create a star

turtle.done()
'''
