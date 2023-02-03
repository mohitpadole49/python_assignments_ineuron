#Write a Python script to remove all non int values from a list.

l=["apple","banana",4.5,1,5,"Mohit"]

for x in l:
    if(x>=chr(48) and x<=chr(57)):
        print(x)
 
