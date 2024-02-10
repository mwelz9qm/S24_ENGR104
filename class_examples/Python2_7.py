# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 11:27:23 2024

@author: mwelz
"""
#create a tuple which you generally can't change
tup = (4, 7.2, "dog", -99)
print(tup[3])

#a tuple with a list which you can technically change

tup = (7,-3, [1,4,5],8)

tup[2][1] = -99

print(tup)

#a dictionary example

favNums ={"Matt":17,"Shannon":99,"Jose":9}
favNums["James"] = 23
print(favNums)


#building a dictionary from scratch

d = {}
d[5] = "horse"
d["coffee"] = 7.2
d[(3,5)] = 7.2
d[-17] = [1,2,3]
print(d)

#an example of a dictionary within a dictionary

pops = {1997:{"Springfield":12000, "Bristol":20000, "Lafayette":4500},
       1998:{"Springfield":13500, "Bristol":20000, "Lafayette":4800},
       1999:{"Springfield":12000, "Bristol":20000, "Lafayette":4500,"Richmond":10000}}

print(pops[1999]["Lafayette"])

