a=[2,4,6,8,563,66,3641]


#b=[]
#for item in a:
#    if item%2==0:
#        b.append(item)
#print(b)

b=[i for i in a if i%2==0 ]    # Shortcut as i for i in var if
print(b)


# Typing table using list comp in file


num= int(input("Enter you number : "))
table = [num*i for i in range(1,11)]
print(table)

with open("tables.txt", "a")as f:
    f.write(str(table))
    f.write('\n')


