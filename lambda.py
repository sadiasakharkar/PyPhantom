# Lambda function = functions written in 1 line using lambda keyword 
#                   accepts any number of arguments , but only has one expression.
#                   (think of it as a shortcut)
#                   (useful if needed for a short period of time , throw-away function) 
#                   (useful if passing function as an argument to another function)

# lambda parameter:expression

 
# def double(x):
#     return x * 2

# print(double(5))
    
double = lambda x: x * 2
print(double(5))

multiply = lambda x , y : x * y
print(multiply(4,5))

add = lambda x , y , z : x + y + z
print(add(5 , 3, 2))

full_name = lambda first , last : first + " " + last
print(full_name("Guido" , "Van Rossum"))

age_check = lambda age : True if age >=18 else False
print(age_check(17))
print(age_check(21))
