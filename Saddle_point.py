def check():
    r = int(input())
    c = int(input())
    matrix = []
    for i in range(r):
        elements = input()
        ele = elements.split()
        row = [int(x) for x in ele]
        matrix.append(row)
    for i in range(r):
        minimum = min(matrix[i])
        min_index = matrix[i].index(minimum)
        saddle = True
        for k in range(r):
            if matrix[k][min_index] > minimum:
                saddle = False
                break
        if(saddle):
            return 1
    return 0
print(check(), end="")


'''
def check():
  r = int(input())
  c = int(input())
  matrix = []
  for i in range(r):
    elements = input()
    ele = elements.split()
    row = [int(x) for x in ele]
    matrix.append(row)
  for i in range(r):
    minimum = matrix[i][0]
    for j in range(c):
      if(matrix[i][j]<minimum):
        minimum = matrix[i][j]
        saddle = 0
        for k in range(r):
          if(matrix[k][j]>minimum):
            saddle+=1
        if(saddle == 0):
          return 1
  return 0

print(check(), end="")
'''
