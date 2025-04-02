mylist = ["Welma","Kirsty","Munashe"]
print(mylist[1])
print(len(mylist))

mylist =["Welma","Kirsty","Munashe"]
mylist[1]= ("Simba")
print(mylist)

mylist =["Welma","Kirsty","Munashe"]
print(mylist[1:])

thislist =(mylist[1:])
print(thislist)

thislist =(mylist[1:])
thislist.append("Nicole")
thislist.append("Tadiwa")
print(thislist)
# adding 2 other names

thislist =(thislist[1:])
thislist.insert(0,"kirsty")
print(thislist)
# inserting another name

mylist =["Welma","Kirsty","Munashe"]
hub=['kirsty', 'Munashe', 'Nicole', 'Tadiwa']
mylist.extend(hub)
print(mylist)
# extending the list

name =(input("enter your name "))
age = (input("enter your age "))
score =(input("enter your score "))
print("name: "+ name + " "+ "age : "+ ""+age+" " + "score: "+ score)