#  FILE HANDLING
#  --> Text file   .c , .ext  ,   --> Binary file .py  , . dat
#           open("this.txt" , "r" )   # READ mode...

f=open('FileHandling.txt', 'r')
data= f.read() # to read
print(data)
f.close()

# can't read twice....

f=open('FileHandling.txt', 'r')
data= f.read(5) # to read
print(data)

data = f.readline()  # another function to READ....
print(data)

f.close()


#   r--> open for reading
#   w--> open for writing         --> ** OVERWRITE **
#   a--> open for appending       --> **CONTINUE writting**
#   +--> open for updating 

#       rb will open for Binary mode
#       rt will open for Text mode 


f = open('anotherFH.txt', 'w')
f.write('Yes, you are able to write')
f.close()

f = open('anotherFH.txt', 'r')
print(f.read())
f.close()


     # Continue writing.....
#   appending --> write as many times as we open file 
f=open('apendFH.txt', 'a')
f.write("I am appending ...   ")
f.close()

f=open('apendFH.txt', 'r')
print(f.read())
f.close()





# Context MANAGER
##  ALTERNATEW without closing...
with open('FileHandling.txt', 'r') as f:
    a=f.read()
print(a)

with open('FileHandling.txt', 'w')as f:
    a= f.write("mve")
print(a)
