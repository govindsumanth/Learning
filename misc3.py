def greet(*names):
    """
    This function greets to the person passed in as a parameter
    """
    for name in names:
        print("Good Morning, " + name)

greet('Paul','jong','alex',"pulli")
print(greet.__doc__)


try:
    def factorial(x):
        if x==1:
            return 1
        else:
            return x* factorial(x-1)
    
    n=int(input("enter number:"))
    print("Factorial of " + str(n) + " is "+ str(factorial(n)))
except RecursionError:
    print ("Beyond limit")

my_list = [1, 5, 4, 6, 8, 11, 3, 12]

new_list = list(filter(lambda x: x %2==0 , my_list))

print(new_list)