#Write a python script to calculate sum of cubes of first N natural numbers

n=int(input("Enter the value f n :"))
sum=0
for x in range(1,n+1):
    sum=sum+(x**3)

print(sum)