#Write a python script to check whether a given year is a leap year or not.

year =int(input("Enter the Year :"))

if(year%400==0):
    print("Leap Year ")
elif(year%100!=0 and year%4==0):
    print("leap year")
else:
    print("Not a leap year ")

