#Write a python program to append elements from another list to the current list.(firstlist = ["Java", "Python", "SQL"]secondlist = ["C", "Cpp", "NoSQL"] )

firstlist = ["Java", "Python", "SQL"]
secondlist = ["C", "Cpp", "NoSQL"] 

for x in firstlist:
    secondlist.append(x)

print(secondlist)