a=float(input("Enter a:"))
b=float(input("Enter b:"))
c=float(input("Enter c:"))
if (a>=b) and (a>=c):
    largest = a
elif (b>=a) and (b>=c):
    largest = b
else:
    largest = c
print("The largest number is",largest)