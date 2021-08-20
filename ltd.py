# IMPORTANT   ____Lists___ [ , , , ] --> It is like a link list and structure mixture (Modern linklist) 
    # can randomly access


#Creating a list
a=[1, 2,3 ,4 ,5]
print(a[1])
a[1]= 9

print(a[1])

 # print(a[6])  // Not possible

c = [45, "Harshit ", False , 8.25]
print(c[1])


# List Slicing

friends = ["Harshit ", "Dakshit", "Manit", "Sushma", "Sanjeev"]

print(friends[1:4])   # multiple data



####
#Sort 
 
l1 = [1,5, 7,9, 42, 8, 9]
print(l1)
l1.sort() # function 
print(l1)


# TO Add important....
l1.append(45)
l1.append(999)
print(l1)

# l1.reverse
# l1.insert(index, value)
# l1.pop(index)
# l1.remove(index)    --> remove any index





print("\n")
# --------------------------------------------------------------------------------
print("\n")



        #### TUPLE --> Same as list but not   ...CHangable.. ()
#  Creating a Tuple  ( , , , ,  )
t = (1,3, 6, 9)

# Printing the elements of a tuple
print(t[0])


#Cannot update the values of a tuple 
# t[0]= 34  --> Gives an error ...

d = ()      # empty
e = (1,) # tuple with only one element 

#functions

print(t.count(1))   # --> Methods
print(t.index(1))  


print("\n")
#---------------------------------------------------------------------------------
print("\n")


      #     {  :  ,  :   ,  :   ,  "sagd" : { } }

###      DICTIONARY   -->  It is like a Structure 
                #   --> can be read using index..

myDict= {            # Key : Value  --> mythylogy
    "Harshit":"Me",
    "Dakshit":"Brother",
    "Sushma":"Mother",
    "Sanjeev":"Father",
    "Marks": [1,2,4,6,7],
    "anotherDict":{'A' : 1,'B': 2},
    1:2
}

print(myDict['Harshit'])  ## Using key 
print(myDict['anotherDict']['B'])


# functions 

print(list(myDict.keys()))      # Keys
print("")
print(list(myDict.values())) # Values
print("")
print(myDict)
print("")
updateDict={
    "IIITG": "College", 
    "sadfs": "Friend",
    "Harshit" : "I"
}
myDict.update(updateDict)

print(myDict)

print(myDict.get("adhgs"))  ## ...Used when any KEY other than PRESENT

















