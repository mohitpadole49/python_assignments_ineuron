#Write a Python script to create a list of first N even natural numbers.

n=int(input("Enter the value of n :-"))
thislist = []
for x in range(1,n*2):
    if(x%2==0):
        thislist.append(x)
 
    
print(thislist)