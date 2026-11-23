fruits = ["banana", "apple", "orange"]
# for fruit in fruits:
#     print(fruit)
#     if fruit == "banana":
#         break # exit the loop where item is apple
#list comprehension
newlist = [x for x in fruits if x!= "apple"]
print(newlist)
# for x in "banana":
#     print(x)

adj =["red","big","tasty"]
fruits =["apple", "banana", "cherry"]
for x in adj:
    for y in fruits:
        print(x,y)


new_list = [ x for x in range(10) if x < 5]
print(new_list)