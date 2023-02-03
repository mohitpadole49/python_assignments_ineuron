#3. Write a python script to print first M multiples of N.

n=int(input("Enter the value of n:"))
m=int(input("Enter the range till the numbers are required :"))

for x in range(1,m+1):
    print(x*n)