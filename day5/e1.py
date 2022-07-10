#Write your code below this row 👇
#A traditional for loop in Python is used for iterating over lists
#A range loop can iterate over anything else
even = 0
for x in range(2, 101):    
    if x % 2 == 0:
        even += x
print(even)