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
    print("Password van " + userid + ": " + pwd)