#Write a python script which takes a three digit number from the user and displays only its middle digit.

num = int(input("Enter the number :"))
a=num//10
mid=a%10
print(mid)