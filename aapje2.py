#!/usr/bin/python

#This is a list
aap_list = [12, 34, 56, 78 , 90, 451, 3]
sum_list = sum(aap_list)
len_list = len(aap_list)
result = sum_list/len_list
print("The avarage is: " + str(result) )
print("Number of elements in the list is: " + str(len_list))
print("Sum of all elements yields: " + str(sum_list))

# These are tuples.. Immutable lists... They CANNOT be changed!!!
tup1 = ('physics', 'chemistry', 1997, 2000);
tup2 = (1, 2, 3, 4, 5 );
tup3 = "a", "b", "c", "d";

# And now.... sets...
# A set contains an unordered collection of unique and immutable objects.
set1 = {"Piet", "Klaas", "Jan"}
set1.add("Gijs")
print(set1)
set1.add("Klaas") # This does not work, since Klaas is already in the set
print(set1)

set2 = {"Jan", "Rob", "Frank", "Piet"}
print(set2)

set3 = set1.union(set2)
set4 = set1.difference(set2)
print("Now the union of both previous sets: " + str(set3))
print("Now the difference of both previous sets: " + str(set4))



