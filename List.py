# thislist = ["apple", "banana", "cherry", "apple"]
# print(thislist)
# print(len(thislist))
#
# list1 = ["apple", "banana", "cherry", 1, 5, 7, 9, 3, True, False]
# print(list1)
# print(type(list1))
# print(list1[-1])
#
# if 1 in list1:
#     print("the list has one")



# thislist1 = ["apple", "banana", "cherry"]
# thislist1[1:5] = ["watermelon"]
# print(thislist1)
# thislist1.append("banana")
# print(thislist1)
# thislist2 = [1, 2, 3, 4]
# thislist1.extend(thislist2)
# print(thislist1)
# thislist1.remove(1)
# print(thislist1)
# thislist1.pop(1)
# print(thislist1)



thislist = ["apple", "banana", "cherry"]
for i in range(1, 3):
  print(thislist[i])

thislist2 = [x for x in thislist if 'a' in x]
print(thislist2)


thislist.sort(reverse = True)
print(thislist)
thislist.sort(key = str.lower)
thislist.reverse()
print(thislist)

copylist = thislist.copy()
print(copylist)