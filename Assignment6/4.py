#Write a python script to print greater between two numbers. Print number only once even if the numbers are the same.
from imaplib import Int2AP


num1=int(input("Enter First  numbers "))
num2=int(input("Enter Second number "))
print(num1,num2)
if(num1>num2):
    print("Number 1 is greater ")
elif(num1==num2):
    print(num1)
else:
    print("Number 2 is greater")