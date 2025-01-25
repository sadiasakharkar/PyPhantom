# *args = parameter that will pack all arguments into a tuple 
#         useful so that a fnction can accept a varying amount of arguments

#def sum(num1 , num2 ):
#    sum = num1 + num2
#    return sum

#print(sum(4 , 8))

# in the above program we cannot pass 3 parameters so instead we will write it as

def add(*args): # we can name it anything the imp is to have a '*' (asterisk)
    sum = 0 
    for i in args:
        sum += i
    return sum

print(add(1 , 2, 3, 5, 4 , 6))

def multiply(*numbers):
    result = 1
    numbers = list(numbers) # we are casting the tuples into list so we can perform opertions or changes once packed
    numbers[0] = 9
    for i in numbers:
        result *= i
    return result

print(multiply(2 ,4 ,5 , 7 ))