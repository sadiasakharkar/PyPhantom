# logical operator (and , or , not) = used to check if two or more conditional statement is true
# operator (and , or , not) = used to check if two or more conditional statement 
temp = int(input("What is the temperature outside? "))

if temp >= 0 and temp <= 33 :
    print("The temperature is good today!")
    print("Go outside!!")
elif temp < 0 or temp > 30 : 
    print("The temperature is bad today!")
    print("Stay Home!!") 
    
# use of not operator it inverts hold condition at once
if not(temp <= 0 or temp>= 30) : 
    print("Today's climate is good")