#Write a python script to calculate factorial of a given number.
n = int(input("Enter a number: "))
p,i = 1,1


while i<=n:
    p = p*i
    i+= 1
print("Factorial is: ", p)
print()
