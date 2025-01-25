# tuples = collections which is ordered and unchangeable used to group together related data

student = ("bro" , 21 , "male")

print(student.count("male"))
print(student.index(21))

for x in student:
    print(x)
    
if "bro" in student:
    print("bro is a male")
    