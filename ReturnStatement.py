# retuen statement = functions send python values/ object back to the caller.
#                   these values/ object are known as the function's return value

def multipy(num1 , num2):
    result = num1 * num2
    return result

x = multipy(6,3)
print(x)


def add (num1 , num2):
    return num1+num2

print(add(4,6))