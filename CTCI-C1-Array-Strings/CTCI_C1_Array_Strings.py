#Cracking the coding interview 
#Chapter 1: Array and Strings
#4/26/21



#Section 1: Hash Maps 

#A hash table is a data structure that maps key to values for highly efficent lookups. There are a number of ways of implemnting this. 
#Syntax for an Dicionary
prices = {
    'march 6' : 310,
    'march 7' : 430
    }

#Creating a hash function to create an index for the array
def get_hash(key):
    h = 0
    for char in key:
        h += ord(char)
    return h % 100

#You need a dictionary, hash function and an array



