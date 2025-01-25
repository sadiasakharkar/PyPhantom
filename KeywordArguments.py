# keyword arguments = arguments preceded by an identifier when we pass them to a function. The  order of 
#                     the argument doesn't matters, unlike positional arguments 
#                     Python knows the names of the arguments that our function receives

def hello(first_name , middle_name , last_name):
    print("Hello! "+first_name+" "+middle_name+" "+last_name)

#example of positional arguments
hello("Sadia" , "Ansar" , "Sakharkar")

# keyword argument
hello(last_name="Sakhrakar" , middle_name="Ansar" , first_name="Zikra")