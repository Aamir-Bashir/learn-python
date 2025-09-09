# Repeat problem 4 for a list of censored word

words  = ["Donkey" , "ganda" , "stinks" , "ew"]

with open("file.txt", "r") as f:
    content = f.read()
        
for word in words:
    content = content.replace(word, "#" * len(word))

with open("file.txt" , "w") as f:
    f.write(content)