#Write a python script to check whether a given quadratic equation has two real & distinct roots, real & equal roots or imaginary roots

a=int(input("Enter A value of a : "))
b=int(input("Enter A value of b : "))
c=int(input("Enter A value of c : "))

d=b**2-4*a*c
if(d>0):
    print("Roots are real and distict ")
elif(d==0):
    print("Roots are real and equal")
else:
    print("Roots are imaginary ")
