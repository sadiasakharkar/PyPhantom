# Higher order functions = a function that either :
#                           1) return a function
#                           or
#                           2) accept a function as a argument
#                           (In Python, functions are also treated as objects)

def loud(text):
    return text.upper()

def quiet(text):
    return text.lower()
def hello(func):
    text = func("Hello! How are you?")
    print (text)


hello(loud)
hello(quiet)
print()

# returns a function 

def divisor(x):
    def dividend(y):
        return y / x
    return dividend


divide = divisor(2)
print (divide(10))
 