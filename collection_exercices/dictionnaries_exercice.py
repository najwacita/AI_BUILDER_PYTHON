#Dictionary is a collection which is ordered** and changeable. No duplicate members.
mydict = {
            "name":"souad",
            "age": 30,
             "age":31 #will override the age
          }
print(mydict)
print(len(mydict))
print(mydict["name"])
print(mydict["age"])

newdict = {
            "name":"souad",
            "age": 30,
             "age":31,
             "color": ["red", "green", "blue"]
          }
print(newdict);

mydict.update({"name": "leaa","age":12,"city":"paris"})
print(mydict)
mydict.update({"city":"Beirut"})
print(mydict)
mydict["city"] =["Syr"]
print(mydict)
mydict["country"]= "Lebanon"
print(mydict)
mydict.pop("age")
print(mydict)
del mydict["country"]
print(mydict)






