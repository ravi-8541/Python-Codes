'''fruits = ["apple", "mango", "cherry", "banana" ]  #creat a list
print(fruits)    #print a list
print(type(fruits))   #check type of list
print(len(fruits))    #check length of list

#checking if item is present in the list.
if "banana" in fruits:
    print("Yes, banana is part of list. ")
else:
    print("No, banana is not a part of list.")

#checking if item is not present in the list. 
    
if "kiwi" not in fruits:
    print("kiwi is not a part of list.")
else:
    print("kiwi is in list. ")

#indexing in list.
print(fruits[1])
#negative indexing in a list.
print(fruits[-2])
#range of indexes
print(fruits[1:3])
#range of negative indexes
print(fruits[-3:-1])

#adding element to list.

#append()
print(fruits.append(" grapes "), fruits)

#insert()
print(fruits.insert(4,"papaya"), fruits)

#extend()
more_fruits = ("orange","pineapple","blackberry")
print(fruits.extend(more_fruits), fruits)

'''
'''fruits = ["apple", "mango", "cherry", "banana" ]
#Removing elements from a list.

fruits.remove("banana")
print(fruits)

fruits.pop(1)
print(fruits)'''

'''#changing/updating item in a list.
list = [10,20,30,40]
list[1] = 40
print(list)

list[1:3]=[25,29]
print(list)
'''
'''#sorting a list 
list = ["D","V","L","C","E"]
    #assending order
list.sort()
print(list)
    #descending order
list.sort(reverse=True)
print(list)
'''

''''''#List comprehension
#list = [50,30,40,10,20,60]
'''list.sort()
for i in list:
    if i > 20:
        print(i)'''
'''
new_list = [i for i in list if i > 25]
print(new_list)

#Copy a list
copy_list = list.copy()
print(copy_list)

#append or sum of lists
append_list = list + new_list + copy_list
print(append_list)

'''
'''#Nested list
#ravi = int(input("Enter any digits. "))
list = [10,60,35,[45,40,55],50,70]
list.insert(3,65)
print(list[3])

'''
 

