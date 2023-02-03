#Write a python script to count digits in a given number
count =0
for x in range(1,10):
    if(x%1==0 and x%x==0):
        
        count=count+1
if(count==2):
    print(x)

        
