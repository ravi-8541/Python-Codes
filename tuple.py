#creating a tuple
colours = ("Red","Green","Yellow")

#Creating a tuple with 1 items.
#books = ("English",)
books = tuple(("English"))

print(type(colours))
print(type(books))

#check length of tuple
print(len(colours))

#accessing items in tuple
print(colours[1])            #positive indexing
print(colours[-1])           #negative indexing
print(colours[1:3])          #range indexing
print(colours[-2:])          #negative range indexing

#check if an item exists in tuple
#if "Red" in colours:
#    print("Red is a part of tuple")

#traverse the tuple
#for i in colours:
#    print(i)

#concatenate 2 tuples
'''more_colours = ("Black","Orange")
colours = colours + more_colours
print(colours)
'''
#unpacking a tuple
colour1, colour2, colour3 = colours
print(colour1, colour2, colour3)






