#Write a program to greet names in list which startswith "S"

l = ["Ali","Shayan","Subhan","Sohaib","Ahmed"]

for name in l:
    if(name.startswith("S")):
        print(f"Hello {name}")