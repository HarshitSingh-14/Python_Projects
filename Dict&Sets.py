 
 #          SETS --> is a collection of non-repetive elements
                #  --> unordered , unindexed
        #  differnt from dict by    :
            
a= {1, 2, 3, 4, 1}
print(a)

# empty set a=set{}       --> a={} __This Dictionary
b= set()
b.add(9)
#  b.add([2,4,7])  --> Can't add list as changable 
b.add((4,5,6,7))  # --> can add 
# b.add({4:5})     --> Can't add list or dictionary
print(b)

print(len(b))
b.remove()








print("\n")

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
