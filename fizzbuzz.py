def fizzbuzz(x):
    while(x<51):
        if(x%3==0 and x%5==0):
            print(x, "FizzBuzz")
        elif(x%3==0):
            print(x, "Fizz")
        elif(x%5==0):
            print(x, "Buzz")
        else:
            print(x)
        x+=1
fizzbuzz(1)
