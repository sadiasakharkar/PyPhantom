def hello():
    print ("Hello")
    
print(hello) #memory address
hi = hello
hi() # prints "Hello" 
hello() # prints "Hello"

say = print 
say("Whoa!! I cant believe that this works!") # prints "Whoa!! I cant believe that this works
