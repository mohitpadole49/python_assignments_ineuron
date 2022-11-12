#10. Write a python script to print greater among three numbers. Print number only once even if the numbers are the same.

print("Enter  a Value of a,b,c")
a,b,c=int(input()),int(input()),int(input())

if(a>b and a>c):
    print("A us greater")
elif(b>a and b>c):
    print("B is greater ")
else:
    print("C is greater ")