def factorial(x:int)-> int:
    # this is recursive function to find the factorial of integer
    if x== 1:
        return 1
    else:
        return (x * factorial(x-1))
num = 5
print("the factorial of", num, "is", factorial(num))

            