#creating a set.
set = {5, True, 1.5, "Ram"}
print(set)

#check length of set
print(len(set))

#check deta type of set
print(type(set))

#accessing deta from sets
for x in set:
    print(x)

#check if item exist in te set.
    
if 6 in set:
    print("yes 6 exist in the set")
else:
    print("no 6 not exist in the set")

#add elements
set.add(7)
set.add("ravi")
print(set)


#add another sequence in a set.
name = {"reshmi", "ravi","ishika","mandodri","ravan", "kansh","supranakhi"}
new_set = tuple(set) + tuple(name)
print(new_set)         #this is added but not data type = set , this converted into tuple deta type


#add another sequence in a set using update operator
name_list = ["Reshmi","Ravi","Ishika"]
set.update(name_list)
print(set)
print(len(set))

#Removing elements from set
set.remove("Ravi")
set.discard("Mandodari")  #This function will not throw an error if value is not present in set
print(set)

#joining 2 sets
s1 = {"Ravi","Reshmi","Ishika"}
s2 = {"Mandodri","Ravan","Hanuman","Ravi"}
print(s1, s2)

s3 = s1.union(s2)
print(s3)

#keep only duplicates while joining
s1.intersection_update(s2)
print(s1)

#keep all values except duplicates.
s1.symmetric_difference_update(s2)
print(s1)
