# nested function = functions called inside other function calls
#                   innermost function calls are resolved first
#                   returned value is used as argument for the next outer function

#num = input("Enter a whole positive number: ") #enter : -3.14
#num = float(num)
#num = abs(num)
#num = round(num)
#print(num)

# the above code can be done with less number of line of code i.e using nested function

print(round(abs(float(input("Enter a whole positive number: ")))))
