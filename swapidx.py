'''n = int(input("Enter size of list: "))

list = []
for _ in range(n):
    num = int(input())
    list.append(num)

idx1 = int(input("Enter index1: "))
idx2 = int(input("Enter index2: "))

print(list)
#swapping values at idx1 and idx2
temp = list[idx1]
list[idx1] = list[idx2]
list[idx2] = temp
print(list)'''





#Practice
n = int(input("Enter size of list "))
list = []
for _ in range(n):
    num = int(input())
    list.append(num)
idx1 = int(input("Enter index 1: "))
idx2 = int(input("Enter index 2: "))
print(list)
#swapping
temp = list[idx1]
list[idx1] = list[idx2]
list[idx2] = temp
print(list)











