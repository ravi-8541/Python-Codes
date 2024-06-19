#Creating a dictionary
phones = {
    "Ravi" : 8541909128,
    "Reshmi" : 6204959344, 
    "Boka" : 8003654565,
}
#printing the dictionary
print(phones)

#checking types of dictionary
print(type(phones))

#checking length of dictionary
print(len(phones))

#assesing items of dictionary

print(phones["Ravi"])
#or print(phones.get("Ravi"))
print(phones.keys())

#update value in dictionary
phones["Reshmi"] = 7970838662
print(phones)

#add element in dictionary
phones["Home"] = 6287602625
print(phones)

more_phones = {
    "Ganesh" : 9898989598,
    "Ramesh" : 9740790134,
    "Anjali" : 7277087740,
}
phones.update(more_phones)
print(phones)

#Remove elements in a dictionary
phones.pop("Ramesh")
print(phones)

#This will remove the last item
phones.popitem()
print(phones)

phones.clear()  #This will empty the dictionary
print(phones)

#Printing elements of a dic.
for x in phones.items():
    print(x)

#printing saperate values of a dic.
for x,y in phones.items():
    print(x,y)

#Nested dictionary
ph_no = {
    "Area1" : {
        "x" : 0,
        "y" : 1,
        "z" : 2
    },
    "Area2" : {
        "a" : 4,
        "b" : 5,
        "c" : 6
    }
}

print(ph_no["Area1"]["y"])
print(ph_no["Area2"]["c"])
