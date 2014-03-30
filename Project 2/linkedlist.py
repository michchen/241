# CS 241
# Michelle Chen
# mchen01@email.wm.edu
# Linked Lists

class Node (object) :

    def __init__(self, value):

        self._value = value
        self._next = None

    def getValue(self):
        return self._value
    
    def setNext(self, value):
        self._next = value

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
    
    
    def append(self, value):
        
        # appends all of the values
        n = Node(value)
        if self._headNode == None:
            self._headNode = n
        else:
            temp = self._headNode
            while temp._next != None:
                temp = temp._next
            temp.setNext(n)

    
    def __str__(self):
        toReturn = ""
        toReturn += "["
        temp = self._headNode
        while temp != None:
            toReturn += str(temp.getValue())
            if temp._next != None:
                toReturn += ", "
            temp = temp._next
        toReturn += "]"
        return toReturn
        
    
    def __getitem__(self, index):
        temp = self._headNode
        if index < 0:
            index = index + len(self)
        if index >= len(self) or index < 0:
            return IndexError
        for i in range(0, index):
            temp = temp._next
            if temp == None:
                raise StopIteration()
        

        return temp.getValue()
        
    
    def __setitem__ (self, key, value):
        newValue = Node(value)
        temp = self._headNode
        find = self[key + 1:len(self)]
        findList = find._headNode
        
        for x in range(0, (key - 1)):
            temp = temp._next
        
        temp._next = newValue
        
        while findList != None:
            self.append(findList.getValue())
            findList = findList._next       
                       
    
    def __len__(self):
        count = 0
        for item in self:
            if self._headNode != 0:
                count += 1
        return count
        
    
    def __contains__(self, value):
        temp = self._headNode
        while temp is not None:
            if temp._value == value:
                return True
            temp = temp._next
        
        return False
            
        
    def __iter__ (self):
        temp = self._headNode
        while temp is not None:
            yield temp
            temp = temp._next
        
    
    def __getslice__(self, i, j):
        temp = self._headNode
        sliceList = LinkedList()
        for x in range (0, i, 1):
            temp = temp._next
        for y in range (i, j, 1):
            sliceList.append(temp.getValue())
            temp = temp._next
        return sliceList        

        
            
