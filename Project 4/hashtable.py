from collections import Hashable


class Node (object):

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.nextNode = None

    def getValue(self):
        return self.value
    
    def setNext(self, value):
        self.nextNode = value
    

class LinkedList (object):
    
    def __init__(self, pythonlist=None):
        
        # sets up the head node
        self._headNode = None
        
        if pythonlist != None:
            # turns the elements of the list into a linked list
            count = 0
            for element in pythonlist:
                if count == 0:
                    self._headNode = Node(element)
                else:
                    self.append(element)
                count += 1
    
    
    def append(self, key, value):
        
        # appends all of the values
        n = Node(key, value)
        if self._headNode == None:
            self._headNode = n
        else:
            temp = self._headNode
            while temp.nextNode != None:
                temp = temp.nextNode
            temp.setNext(n)

    
    def __str__(self):
        toReturn = ""
        toReturn += "["
        temp = self._headNode
        while temp != None:
            toReturn += str(temp.getValue())
            if temp.nextNode != None:
                toReturn += ", "
            temp = temp.nextNode
        toReturn += "]"
        return toReturn
        
    
    def __getitem__(self, index):
        temp = self._headNode
        if index < 0:
            index = index + len(self)
        if index >= len(self) or index < 0:
            return IndexError
        for i in range(0, index):
            temp = temp.nextNode
            if temp == None:
                raise StopIteration()
        

        return temp.getValue()
        
    
    def __setitem__ (self, key, value):
        newValue = Node(key, value)
        temp = self._headNode
            
        while temp != None:
            if temp.key == key:
                temp.value = value
                temp = temp.nextNode
                break
            temp = self.nextNode     
                       
    
    def __len__(self):
        count = 0
        for item in self:
            if self._headNode != 0:
                count += 1
        return count
        
    
    def __contains__(self, value):
        temp = self._headNode
        while temp is not None:
            if temp.value == value:
                return True
            temp = temp.nextNode
        
        return False
            
        
    def __iter__ (self):
        temp = self._headNode
        while temp is not None:
            yield temp
            temp = temp.nextNode
        
    
    def __getslice__(self, i, j):
        temp = self._headNode
        sliceList = LinkedList()
        for x in range (0, i, 1):
            temp = temp.nextNode
        for y in range (i, j, 1):
            sliceList.append(temp.getValue())
            temp = temp.nextNode
        return sliceList        



class Hashtable (object):

    def __init__(self, hashFunction, size=500):
        """ Initialize a blank hashtable

        hashFunction - a function that contains 2 arguments, key and size of hash
            and returns an index to a bucket
        size - the number of buckets in your hash
        """
        self.array = []
        self.hashFunc = hashFunction
        self.size = size
        
        for num in range (self.size):
            linked = LinkedList()
            self.array.append(linked)

    def __setitem__(self, key, value):
        """ Sets the value at the key to value

        key - any immutable object
        value - any object

        if key is mutable, raise a TypeError
        """
        if isinstance(key, Hashable) == False:
            raise TypeError
        else:
            newIndex = self.array[self.hashFunc(key, self.size)]

            newIndex.append(key, value)

        

    def __getitem__(self, key):
        """ Returns the value at the key 
        key - immutable key value

        if there is no value at key, raise AttributeError
        """
        index = self.hashFunc(key, self.size)
        
        for item in self.array[index]:
            if item.key == key:
                return item.value
        raise AttributeError      


    def getBucketSizes(self):
        """ yield the sizes of each bucket as an iterator"""

        for item in self.array:
            yield len(item)


    def __len__(self):
        """ Returns the total number of items in the hash"""
        count = 0
        for llist in self.array:
            count += len(llist)
            
        return count


    def __contains__(self, key):
        """ Returns True is the hash has a key """
        index = self.hashFunc(key, self.size)
        for item in self.array[index]:
            if item.key == key:
                return True
        
        return False

        


def hashFunction(key, numbuckets):

    indexcount = 0
    key = str(key)
    key = key.lower()
    for letter in key:
        temp = ord(letter)
        
        indexcount += temp
    
    indexcount = indexcount % numbuckets
    return indexcount
        


if __name__ == "__main__":
    h = Hashtable(hashFunction, 1000)
    h["cat"] = "a feline"
    h["memphis"] = "a city"
   
    print h["cat"]
    print h['memphis']
    print 'Does h contain {}, {}'.format('cat', 'cat' in h)
    print 'Does h contain {}, {}'.format('piano', 'piano' in h)
    print 'h has a size {}'.format(len(h))
