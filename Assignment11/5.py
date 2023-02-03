#Write a python script to calculate sum of first N even natural numbers

n=int(input("Enter the value f n :"))
sum=0
for x in range(1,n+1):
    if(x%2==0):
        sum=sum+x
print(sum)