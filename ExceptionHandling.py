# exception = events detected during excution that interrupt the flow of a program

try:
    numerator = int(input("Enter a number to divide: "))
    denominator = int(input("Enter a number to divide by: "))
    result = numerator/denominator
    

except ZeroDivisionError as e: # as e is optional 
    print(e)
    print("You can't divide by zero! idiot")
    
except ValueError as e:
    print(e)
    print("Enter only number plzz")

except Exception as e:
    print(e)
    print("Something went wrong :(")
    
else: 
    print(result)
    
finally: # this is always at the end how this works is that whether or not we catch an exception we will always execute any  code that is within the block of code for our finally clause
    print("This will always execute")
    