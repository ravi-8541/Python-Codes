ar1 = [1,5,10,20,40,80]
s_ar1 = set(ar1)
ar2 = [6,7,20,80,100]
s_ar2 = set(ar2)
ar3 = [3,4,15,20,30,70,80,120]
s_ar3 = set(ar3)

#find common elements in three sorted lists.
s_ar1.intersection_update(s_ar2, s_ar3)
print(s_ar1)

l1 = [1,5,5]
s1 = set(l1)
l2 = [3,4,5,5,10]
s2 = set(l2)
l3 = [5,5,10,20]
s3 = set(l3)

s1.intersection_update(s2, s3)
print(s1)

#join using intersection
s1s2 = s1.intersection(s2)
final_set = s1s2.intersection(s3)
print(final_set)