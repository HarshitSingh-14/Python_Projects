import os  #functionality extend 

print("Hello world")

a= "harry"
b=True
C= 3.36
d=None
print(a) 
print(b)
print(C)
print(d)

print(type(C))  

print("The value of 3+8 =is", 3+8 )

e= (4>7)
print(e)

bool1= True
bool2 = False 
print("The alue of and is ",(bool1 and bool2))
print("The value of not bool1 is ",(not bool1))


f= "3462"

print( int(f) - 2)   # Type casting

#Input
a = input("Enter your name : ")
print(a)
print(type(a))


##### String ''  " "   ''' '''

g="harshit 's "
h=''' " Harshit Singh's " '''
print(h)

#catenation
i = g+ h
print(i)

#index
print(i[1])

#slicing
print(i[0:3])  #first including last excluding
print(i[-6:-1])  #Not upto positive

# string Functions

print(len(i))
print(i.endswith("dasf"))
print(i.count("a"))
print(i.capitalize())  # rest small
print(i.find("Harshit"))
print(i.replace("s", "l"))

# \n --> breaking line   \t --> tab   \\ --> backslash
















