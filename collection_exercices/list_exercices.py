mylist = [1, 2, 3, 4, 4]
print(type(mylist))
# print(mylist[0])
# print(len(mylist))
#remove item fromlist
# mylist.remove(4)
# print(mylist)
#remove item from list
# mylist.pop()
# print(mylist)
# #mylist.pop(0)
# #print(mylist)
# #del mylist[0]
# #print(mylist)
# #mylist.clear()
# #print(mylist)

Fruit_list = ["banana", "apple", "grape"]
print(Fruit_list)
Fruit_list.append("orange")
print(Fruit_list)
#join 2 list
mylist.extend(Fruit_list)
print(mylist)

#list comprehension
new_list =[]
for x in Fruit_list:
    if "a" in x:
        new_list.append(x)
print(new_list)
#ranging
ranging_list = [x for x in range(10)]
print(ranging_list)
print(ranging_list[0:5])

