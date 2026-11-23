#lambda argument: expression
my_lambda = lambda x: x * 2 # craetes a lambda funct take one argument x and multiplies it by 2
print(my_lambda(5))


#multiple arguments
x = lambda a, b : a * b
print(x(5,6))


def my_function(n):
    return lambda a : a * n

my_doubler = my_function(2)

print(my_doubler(5))


words = ["apple", "banana","cherry", "date"]
words_sorted = sorted(words,key=lambda x: len(x))

print(words_sorted)