#Write a program to find out the line number where python is present from question 6

with open("log.txt", "r") as f:
    lines = f.readlines()
lineno = 1
for line in lines:
    if("python" in line):
     print(f"Yes Pyhton is present in line: {lineno}")
     break
    lineno += 1
else:
    print("Python is not present in log.txt")