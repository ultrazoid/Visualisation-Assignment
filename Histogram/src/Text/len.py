'''
Created on 31/05/2012

@author: ultrazoid_
'''

def length(lists):
    lengths = 0
    for ind in lists:
        lengths +=1
    return lengths

x=[1,2,3,4,5,6,7,8,9,0]

print length(x)