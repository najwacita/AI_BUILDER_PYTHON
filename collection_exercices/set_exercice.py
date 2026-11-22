#unchangeable , unorder, no duplicates values
set1 ={1, 2, 3, 4, 5}
print(set1)
print(len(set1))
#add new item
set1.add(6)
print(set1)
Fruit_list = { "banana", "apple", "grape" }
set1.update(Fruit_list)
print(set1)
#remove banana
# set1.remove("kiwi")
# print(f'remove result: {set1}')

#discard element 
set1.discard("kiwi")
print(f'discard result: {set1}')
set1.pop() #remove an arbitrary element (a random element, not necessarily the first or last).
print(set1)
#del set1

set1.clear()
print(set1)


