# for loop = a statement that will execute it's block of code a limited amount of times
# while loop = unlimited number of times

#for i in range(10+1):
#    print(i)

#for i in range(50, 100): # range (inclusive , exclusive )
#    print(i)

#for i in range (50 , 100 , 2):
#    print(i)

#for i in "sadia sakharkar":
#    print(i)
    
#QUESTION : to design a countdown starting at 10 and count down to zero n then maybe once we reach zero we can print something such as Happy new year!!

import time
for seconds in range (10 , 0 , -1): # -1 will be a countdown 
    print(seconds)
    time.sleep(1)
print("Happy New Year!!!")