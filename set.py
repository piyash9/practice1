# thisset = {"apple", "banana", "cherry", True, 1, 2}
#
# print(thisset)
# print(len(thisset))
# print(type(thisset))



# myset = set({1, 2, 3, 4})
# print(myset)
#
# for x in myset:
#     print(x)
#
# print(2 not in myset)



# thisset = {"apple", "banana", "cherry"}
#
# thisset.add("orange")
# thisset1 = {1, 2, 3}
# print(thisset)
# thisset.update(thisset1)
# print(thisset)


# set1 = {"a", "b", "c"}
# set2 = {1, 2, 3}
# set3 = {"John", "Elena"}
# set4 = {"apple", "bananas", "cherry"}
#
# myset = set1.union(set2, set3, set4)
# print(myset)

# set1 = {"a", "b" , "c"}
# set2 = {1, 2, 3}
#
# set1.update(set2)
# print(set1)

set1 = {"apple", 1,  "banana", 0, "cherry"}
set2 = {False, "google", 1, "apple", 2, True}

set3 = set1.intersection(set2)
set3 = set1.difference(set2)
print(set3)