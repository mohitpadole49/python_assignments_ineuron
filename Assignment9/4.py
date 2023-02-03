#Write a python script to print first N odd natural numbers

num=int(input("Enter the value of n :"))
i=0
while(i<=num*2):
    if(i%2!=0):
        print(i)
    i=i+1