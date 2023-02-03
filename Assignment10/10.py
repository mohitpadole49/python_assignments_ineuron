#Write a python script to display all prime numbers within a range.# range start = 15 end = 45

i=1
count=0
for x in range(14,28):
    if(x%i!=0):
        count=count+1
        print(x)
        i=i+1
    
if(count==2):
    print("prime Number")
else:
    print("Not a prime number ")