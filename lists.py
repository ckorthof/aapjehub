#!/usr/bin/python

#This is a list
aap_list = [12, 34, 56, 78 , 90, 451, 3]
sum_list = sum(aap_list)
len_list = len(aap_list)
result = sum_list/len_list
print("The average is: " + str(result) )
print("Number of elements in the list is: " + str(len_list))
print("Sum of all elements yields: " + str(sum_list))

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(letters)
# ['a', 'b', 'c', 'd', 'e', 'f', 'g']
# replace some values
letters[2:5] = ['C', 'D', 'E']
print(letters)
# ['a', 'b', 'C', 'D', 'E', 'f', 'g']
# now remove them
letters[2:5] = []
print(letters)
# ['a', 'b', 'f', 'g']
# clear the list by replacing all the elements with an empty list
letters[:] = []
print(letters)
# []

# Operations on lists: https://docs.python.org/3.6/tutorial/datastructures.html#more-on-lists
"""
list.append(x)
Add an item to the end of the list. Equivalent to a[len(a):] = [x].

list.extend(iterable)
Extend the list by appending all the items from the iterable. Equivalent to a[len(a):] = iterable.

list.insert(i, x)
Insert an item at a given position. The first argument is the index of the element before which to insert, so a.insert(0, x) inserts at the front of the list, and a.insert(len(a), x) is equivalent to a.append(x).

list.remove(x)
Remove the first item from the list whose value is x. It is an error if there is no such item.

list.pop([i])
Remove the item at the given position in the list, and return it. If no index is specified, a.pop() removes and returns the last item in the list. (The square brackets around the i in the method signature denote that the parameter is optional, not that you should type square brackets at that position. You will see this notation frequently in the Python Library Reference.)

list.clear()
Remove all items from the list. Equivalent to del a[:].

list.index(x[, start[, end]])
Return zero-based index in the list of the first item whose value is x. Raises a ValueError if there is no such item.

The optional arguments start and end are interpreted as in the slice notation and are used to limit the search to a particular subsequence of the list. The returned index is computed relative to the beginning of the full sequence rather than the start argument.

list.count(x)
Return the number of times x appears in the list.

list.sort(key=None, reverse=False)
Sort the items of the list in place (the arguments can be used for sort customization, see sorted() for their explanation).

list.reverse()
Reverse the elements of the list in place.

list.copy()
Return a shallow copy of the list. Equivalent to a[:].
"""

fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
print(fruits.count('apple'))
# 2
print(fruits.count('tangerine'))
# 0
print(fruits.index('banana'))
# 3
print(fruits.index('banana', 4))  # Find next banana starting a position 4
# 6
print(fruits)
# ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
fruits.reverse()
print(fruits)
# ['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange']
fruits.append('grape')
print(fruits)
# ['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange', 'grape']
fruits.sort()
print(fruits)
# ['apple', 'apple', 'banana', 'banana', 'grape', 'kiwi', 'orange', 'pear']
print(fruits.pop())
# 'pear'
print(fruits)

"""
It is also possible to use a list as a queue, where the first element added is the first element retrieved (first-in, first-out);
however, lists are not efficient for this purpose. While appends and pops from the end of list are fast, doing inserts or pops from the
beginning of a list is slow (because all of the other elements have to be shifted by one).
To implement a queue, use collections.deque which was designed to have fast appends and pops from both ends. For example:
"""

from collections import deque
queue = deque(["Eric", "John", "Michael"])
print(queue)
queue.append("Terry")           # Terry arrives
queue.append("Graham")          # Graham arrives
print(queue)
print(queue.popleft())          # The first to arrive now leaves
# 'Eric'
print(queue.popleft())          # The second to arrive now leaves
# 'John'
print(queue)                     # Remaining queue in order of arrival
deque(['Michael', 'Terry', 'Graham'])

# List comprehension
"""
List comprehensions provide a concise way to create lists. Common applications are to make new lists where each element is the result of 
some operations applied to each member of another sequence or iterable, or to create a subsequence of those elements that satisfy a certain condition.

For example, assume we want to create a list of squares, like:
"""

print("\nList comprehension:")
print("Three ways to build the same list")
squares = []
for x in range(10):
     squares.append(x**2)

print(squares)
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

squares = list(map(lambda x: x**2, range(10)))
print(squares)

squares = [x**2 for x in range(10)]
print(squares)

# For example, this listcomp combines the elements of two lists if they are not equal:
print([(x, y) for x in [1,2,3] for y in [3,1,4] if x != y])
# [(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]

# Equivalent to:
combs = []
for x in [1,2,3]:
     for y in [3,1,4]:
         if x != y:
             combs.append((x, y))

print(combs)
# [(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]

# When looping through a sequence, the position index and corresponding value can be retrieved at the same time using the enumerate() function.

for i, v in enumerate(['tic', 'tac', 'toe']):
	  print(i, v)

# 0 tic
# 1 tac
# 2 toe

# To loop over two or more sequences at the same time, the entries can be paired with the zip() function.

questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
	  print('What is your {0}?  It is {1}.'.format(q, a))

# What is your name?  It is lancelot.
# What is your quest?  It is the holy grail.
# What is your favorite color?  It is blue.

# To loop over a sequence in reverse, first specify the sequence in a forward direction and then call the reversed() function.
for i in reversed(range(1, 10, 2)):
	  print(i)

# 9
# 7 
# 5
# 3
# 1
# To loop over a sequence in sorted order, use the sorted() function which returns a new sorted list while leaving the source unaltered.

basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for f in sorted(set(basket)):
	  print(f)

#apple
#banana
#orange
#pear
#It is sometimes tempting to change a list while you are looping over it; however, it is often simpler and safer to create a new list instead.

import math
raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
filtered_data = []
for value in raw_data:
	  if not math.isnan(value):
			filtered_data.append(value)

print(filtered_data)
# [56.2, 51.7, 55.3, 52.5, 47.8]

print(float('NaN'))
