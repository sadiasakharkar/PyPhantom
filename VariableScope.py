# scope = The region that a variable is recognized
#         A variable is only available from inside the region it is created.
#         A global and locally scoped versions of a variable can be created

name = "bro"  # global scope (available inside and outside the function)

def display_name():
    name = "Code"    #local scope(available only inside this function)
    print(name)
    
print(name)
display_name()


# rule :
#   L = local
#   E = Enclosing
#   G = Global
#   B = built-in

