'''str = "The unexpected always happens."
print(str)
print(len(str))
print(str.find("pp"))
print(str[ :11])
print(str.replace("always","never"))
str1 = "no matter what"
print(str + str1)
'''


s = input("Enter the word: ")
s1 = s.strip()
s2 = s1.lower()
r = s2[::-1]
if s==r:
    print(True)
else:
    print(False)