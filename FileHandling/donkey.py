words = ["donkey", "Harshit"]

with open("donkey.txt", "r") as f:
    content = f.read()


for word in words: 
    content = content.replace(word, "Babu Rao")
    with open("donkey.txt", "w")as f:
        f.write(content)
            
    
    
