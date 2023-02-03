# Write a python script to print first N odd natural numbers

n=int(input("Enter the value of n Till the Even numbers to be printed :"))

for x in range(1,(n*2)+1):
    if(x%2!=0):
        print(x)