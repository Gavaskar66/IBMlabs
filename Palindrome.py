s=input("Enter the string:")
s=s.casefold()
r=''.join(reversed(s))

if s==r:
    print(s,"is a palindrome")
else:
    print(s,"is not a palindrome")