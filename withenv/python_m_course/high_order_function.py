# --- Filter ---
# List comprehension
my_list = [1, 4, 5, 6, 9, 13, 19, 21]
odd = [i for i in my_list if i % 2 != 0]
print(odd)

# High order function
odd2 = list(filter(lambda x: x%2 != 0, my_list))
print(odd2)
print()

# --- Map ---
# List comprehension
my_list = [1, 2, 3, 4, 5]
squares = [i**2 for i in my_list]
print(squares)

# High order function
squares2 = list(map(lambda x: x**2, my_list))
print(squares2)
print()

# --- Reduce --- multiply all elements
# List comprehension
my_list = [2, 2, 2, 2, 2]
all_mult = 1
for i in my_list:
	all_mult = all_mult * i
print(all_mult)

# High order function
from functools import reduce
all_mult2 = reduce(lambda a, b: a*b, my_list)
print(all_mult2)
print()
