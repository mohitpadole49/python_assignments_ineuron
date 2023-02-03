#Write a Python script to create a list of first N natural numbers.

n=int(input("Enter the value of n :-"))
thislist = []
for x in range(1,n+1):
 
    thislist.append(x)
print(thislist)