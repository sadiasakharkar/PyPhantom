# sort() method = used with lists 
# sort() method = used with iterable

students = [ " Harry ", " Rohan ", " Shubham ", " Harsh " ]
students.sort()

# for i in students:
#     print(i)
    
# print()
# students.sort(reverse = True)
# for i in students:
#     print(i)
    
print()
sorted_students = sorted(students)
for i in sorted_students:
    print(i)

print()
print()
sorted_students = sorted(students ,reverse = True)
for i in sorted_students:
    print(i)
    
