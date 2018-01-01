#!/usr/bin/python

from all_passwords import password

passworddict = password()

var = "Stringetje "
var2 = 3.75
var3 = 3,75
var4 = {"Piet": "Jansen", 23: 14, "Score": 3}

var *= 3
var2 *= 3
var3 *= 3
#var4 *= 3   ==> This does not work. Cannot multiply dictionary with integer.

print(var)
print(var2)
print(var3)
print(var4)
print("De score is: " + str(var4['Score']))
for userid in passworddict.keys():
    pwd = passworddict[userid]
    print("Password of " + userid + ": " + pwd)
    
# More on dictionaries: https://docs.python.org/3.6/tutorial/datastructures.html#dictionaries

tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
print(tel)
# {'sape': 4139, 'guido': 4127, 'jack': 4098}
print(tel['jack'])
# 4098
del tel['sape']
tel['irv'] = 4127
print(tel)
# {'guido': 4127, 'irv': 4127, 'jack': 4098}
print(list(tel.keys()))
# ['irv', 'guido', 'jack']
print(sorted(tel.keys()))
# ['guido', 'irv', 'jack']
print('guido' in tel)
# True
print('jack' not in tel)
# False


# The dict() constructor builds dictionaries directly from sequences of key-value pairs:

print(dict([('sape', 4139), ('guido', 4127), ('jack', 4098)]))
# {'sape': 4139, 'jack': 4098, 'guido': 4127}

# In addition, dict comprehensions can be used to create dictionaries from arbitrary key and value expressions:

print({x: x**2 for x in (2, 4, 6)})
# {2: 4, 4: 16, 6: 36}

# When the keys are simple strings, it is sometimes easier to specify pairs using keyword arguments:

print(dict(sape=4139, guido=4127, jack=4098))
# {'sape': 4139, 'jack': 4098, 'guido': 4127}

# 5.6. Looping Techniques
# When looping through dictionaries, the key and corresponding value can be retrieved at the same time using the items() method.

knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
     print(k, v)

# gallahad the pure
# robin the brave

"""
Sr.No.	Function with Description
1	cmp(dict1, dict2)
Compares elements of both dict.

2	len(dict)
Gives the total length of the dictionary. This would be equal to the number of items in the dictionary.

3	str(dict)
Produces a printable string representation of a dictionary

4	type(variable)
Returns the type of the passed variable. If passed variable is dictionary, then it would return a dictionary type.

Python includes following dictionary methods

Sr.No.	Methods with Description
1	dict.clear()
Removes all elements of dictionary dict

2	dict.copy()
Returns a shallow copy of dictionary dict

3	dict.fromkeys()
Create a new dictionary with keys from seq and values set to value.

4	dict.get(key, default=None)
For key key, returns value or default if key not in dictionary

5	dict.has_key(key)
Returns true if key in dictionary dict, false otherwise

6	dict.items()
Returns a list of dict's (key, value) tuple pairs

7	dict.keys()
Returns list of dictionary dict's keys

8	dict.setdefault(key, default=None)
Similar to get(), but will set dict[key]=default if key is not already in dict

9	dict.update(dict2)
Adds dictionary dict2's key-values pairs to dict

10	dict.values()
Returns list of dictionary dict's values
"""