#Write a program to mine a log file and find out whether it contains "pyhton"

with open("log.txt", "r") as f:
    content = f.read()

if("python" in content):
    print("Yes Pyhton is present in log.txt")
else:
    print("Python is not present in log.txt")