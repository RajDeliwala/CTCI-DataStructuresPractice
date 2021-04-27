
#Cracking the coding interview 
#Chapter 1: Array and Strings
#4/26/21



#Section 1: Hash Maps 

#A hash table is a data structure that maps key to values for highly efficent lookups. There are a number of ways of implemnting this. 

#Creating a hash function to create an index for the array
def get_hash(key):
    h = 0
    for char in key:
        h += ord(char)
    return h % 100


#Implement a hashtable to get the best understanding for how they works


#Implementing the Hash table first
class HashTable(object):
    def __init__(self):
        #Capacity is the size of the internal array
        #Size is the number of elements that have been inserted
        #Buckets is the internal array storing each inserted value in a bucket
        #Inital capacity is set to 50  
        self.capacity = 50
        self.size = 0
        self.buckets = [None] * self.capacity
    

    def hash(self, key):
        hashsum = 0
        #For each character in the string
        for i, c in enumerate(key):
            #Adding Index + length of key ^ current char code
            #Preforming ord or better know as modulus to keep hasum in range 
            #[0 to self.capacity - 1] index
            hashsum += (i + len(key)) ** ord(c)
            hashsum = hashsum % self.capacity
        return hashsum

    #Insert a key value pair into our hashtable 
    def insert(self, key, value):
        #Increment size of hashtable
        self.size += 1
        #Compute index of key using hash function
        index = self.hash(key)
        #Going to the node that correspondes to the hash
        node = self.buckets[index]
        #if bucket is empty
        if node is None:
            #Create node, add it, return
            self.buckets[index] = Node(key, value)
            return
        #Collision! Iterate to the end of the end of the linked list at the provided key/value
        prev = node
        while node is not None:
            prev = node
            node = node.next
        #Add a new node at the end of the list with the given key/value
        prev.next = Node(key,value)


    def find(self, key):
        #Compute the hash
        index = self.hash(key)

        #Go to the first node in the list at bucket
        node = self.buckets[index]

        #Traverse the linked list at this node
        while node is not None and node.key != key:
            node = node.next
    
            #Now, node is the request key/value pair or none
        if node is None:
                return None
        else:
                return node.value

    def remove(self, key):
        #Compute the hash
        index = self.hash(key)
        node = self.buckets[index]
        prev = None

        #Iterate to the requested node
        while node is not None and node.key != key:
            prev = node
            node = node.next

            if node is None:
                #Node not found
                return None
            else:
                #Key was found
                self.size -= 1
                result = node.value

                #Delete the element from the linked list
                if prev is None:
                    node = None
                else:
                    prev.next = prev.next.next
                #Return the deleted data
                return result



#Implementing Nodes at each point in the hash table
#Using a linked list helps prevent collisions 
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

#We need a good hash function to prevent collision and make an evenly hash table




#Find the value given it's key


#Removing an element from a hash table 



#Creating a new instance of hashtable
ht = HashTable()

#Some data to be stored within the hashtable
ages = ["24", "25", "54"]
#Before inserting it into the hashtable
print("Initally printing ages ",  ages)

#Insert the data under the key "peopleAge"
ht.insert("peopleAge", ages)

ages = None
#Printing ages to make sure it's empty now
print("Ages after the none call " , ages)

ages = ht.find("peopleAge")

print("Ages after the find call ", ages)



