#Write a python script to print first N odd natural numbers in reverse order


num =int(input("Enter The Value of n :- "))
n=num*2
while(n>=1):
    if(n%2!=0):
        print(n)
    n=n-1