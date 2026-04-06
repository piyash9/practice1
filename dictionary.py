thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  2 : "piyash"
}
# print(thisdict)
# print(thisdict[2])
# print(len(thisdict))
#
# c = dict(name = 'piyash', age = 24)
# print(c)
# print(thisdict.keys())
# print(thisdict.items())


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020})
# print(thisdict)
# thisdict.pop("year")
# print(thisdict)

for a, b in thisdict.items():
  print(a, b)