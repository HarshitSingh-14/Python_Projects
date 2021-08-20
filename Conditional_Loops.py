##   if  elif  else 

a= None   
if(a is None):   # --> ==  or is 
    print("Yes")
else: 
    print("No")

print("")
b = [2,4,6]
print(2 in b)  # is in --> TRUE or False
print("")



##          LOOPS

# WHILE  
i = 1
while i<=10:
    print(i)
    i= i + 1

print("")

fruits=['Banana', 'Watermemlon', 'Grapes', 'Mangoes']

for item in fruits:
    print(item)

print("")


# range(start , stop , step size -> default 1 )
for i in range(1,8):    # i condition 
    print(i)
    if i==5:   # in parallel yo print
        continue
    elif i==7:
        break
else :             # for infinite loop 
    print("This is inside else of for loop")









