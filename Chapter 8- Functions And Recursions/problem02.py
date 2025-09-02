#Convert temperature from fahrenheit to celsius

def f_to_c(f):
    return 5*(f-32)/9

f = int(input("Enter Temperature in fahrenheit: "))
print(round(f_to_c(f), 2)) #Round function rounds the figure that,",2" tells it that round the figure in 2 decimal places