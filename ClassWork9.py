#!/usr/bin/python

#names = ['Sam', 'Don', 'Daniel'] 
#for i in range(len(names)): 
#    names[i] = hash(names[i]) 
#print(names)
#---------------
#secret_names = map[hash,names]
#print(list(secret_names))

#------------check amount of red entries----
def check(list):
    return list == "red"

list=["red", "green", "black", "red", "brown", "red", "blue", "red", "red", "yellow"]
print("We have ", len(filter(check, list)),"\"Red\" in list")

#-----------

