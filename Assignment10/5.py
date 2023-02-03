# Write a python script to print table of user’s choice

n = int(input("Enter the number for which the table to be printed :"))

for x in range(1,11):
    print(f"{x} X {n} =",x*n)