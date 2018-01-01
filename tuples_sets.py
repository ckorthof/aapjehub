#!/usr/bin/python

# These are tuples.. Immutable lists... They CANNOT be changed!!!
tup1 = ('physics', 'chemistry', 1997, 2000);
tup2 = (1, 2, 3, 4, 5 );
tup3 = "a", "b", "c", "d";

# And now.... sets... Look like dictionaries, without the values...
# A set contains an unordered collection of unique and immutable objects.
# Although the objects aare immutable, objects can be added and deleted from sets
set1 = {"Piet", "Klaas", "Jan"}
set1.add("Gijs")  # Gijs is added to the set
print(set1)
set1.add("Klaas") # This does not work, since Klaas is already in the set
print(set1)

set2 = {"Jan", "Rob", "Frank", "Piet"}
print(set2)

set3 = set1.union(set2)
set4 = set1.difference(set2)
print("Now the union of both previous sets: " + str(set3))
print("Now the difference of both previous sets: " + str(set4))

# Demonstrate set operations on unique letters from two words
a = set('abracadabra')
b = set('alacazam')
print(a)                                  # unique letters in a
# {'a', 'r', 'b', 'c', 'd'}
print(b)                                  # unique letters in b
# {a', 'c', 'z', 'm', 'l'}
print(a - b)                              # letters in a but not in b
# {'r', 'd', 'b'}
print(a | b)                              # letters in a or b or both
# {'a', 'c', 'r', 'd', 'b', 'm', 'z', 'l'}
print(a & b)                              # letters in both a and b
# {'a', 'c'}
print(a ^ b)                              # letters in a or b but not both
# {'r', 'd', 'b', 'm', 'z', 'l'}
