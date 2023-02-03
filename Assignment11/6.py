#Write a python script to calculate factorial of a given number

n=int(input("Enter te value of n "))

fact=1
for x in range(1,n+1):
    fact=fact*x
print(fact)