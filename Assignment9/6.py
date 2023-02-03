# Write a python script to print first N even natural numbers

num =int(input("Enter the value of n :"))
n=num*2
i=1
while(i<=n):
    if(i%2==0):
        print(i)
    i=i+1