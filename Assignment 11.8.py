#Write a python script to calculate sum of digits of a given number
n=int(input("Enter a number"))

sum=0

for digit in str(n):
    sum=sum+int(digit)

print("Sum of digits",sum)
