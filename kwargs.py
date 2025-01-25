# **kwargs = parameter that will pack all arguments into a dictionary 
#            useful so that a function can accept a varying amount of keywords arguments 

# it is identical to args except with args , args will accept a varying amount of positional arguments and pack them into tuple
# with kwargs tis will accept  a varying amount of keyword arguments and pack them into a dictionary 

#def hello(first , last):
#    print("Hello! " + first +" " + last)
    
#hello(first="Sadia" , last="Sakharkar")

# when passing more than 2 arguments it will not accept , here we use kwargs . The above code can be written as

def hello(**kwargs): # kwargs is just a common naming conversion , imp is to have '**' (double asterisk)
    #print("Hello! " + kwargs['first'] + " " +kwargs['last']) # first method
    
    print("Hello!" , end=" ")
    for value in kwargs.values():
        print(value, end=" ")
    print()  # To ensure there's a newline at the end

hello(title = "Miss.", first="Sadia", middle="Ansar", last="Sakharkar")

