#Write a python script to calculate sum of first N odd natural numbers
n= int(input("Enter the value of n: "))
sum=0
for i in range(1,n+1):
    sum = sum + (2*i-1)
print("Sum is: ",sum)
        

