# Assignment 3
# linkedmatrix.py
# Michelle Chen
# Makes a matrix of values

class Node (object):
    
    def __init__(self, value):
        self.value = value
        self.north = None
        self.south = None
        self.east = None
        self.west = None

class LinkedMatrix (object) :

    def __init__(self, x, y, defaultValue = None):
        """ creates a new matrix with x columns and y rows with default value default value """
        self.headnode = None
        self.defaultValue = defaultValue
        self.dimensions = (x, y)
        
        self.columns = x
        self.rows = y
        
        self.headnode = Node(defaultValue)
	if self.dimensions == (0, 0):
	    self.headnode = None
	
        temp = self.headnode      
            
        for c in range (self.dimensions[0] - 1):
            newNode = Node(defaultValue)
            newNode.west = temp
            temp.east = newNode
                
            temp = newNode
            
        for r in range(self.dimensions[1] - 1):
            for x in range(self.columns - 1):
                temp = temp.west 
            
            newNode = Node(defaultValue)
            newNode.north = temp
            temp.south = newNode
            
            tempTwo = temp
            temp = newNode 
            
            for c in range(self.dimensions[0] - 1):
                newNode = Node(defaultValue)
                tempTwo = tempTwo.east 
                
                newNode.west = temp
                temp.east = newNode
                
                tempTwo.south = newNode
                newNode.north = tempTwo
                    
                temp = newNode     
            
    def __str__(self):
        """ return the string representation of the matrix """
        temp = self.headnode
        matrixList = []
        matrixList.append(temp)
        while temp.south != None:
            matrixList.append(temp.south)
            temp = temp.south
            
        toReturn = ""
        for item in matrixList:
            toReturn += str(item.value) + " "
            while item.east != None:
                item = item.east
                toReturn += str(item.value) + " "
            toReturn += "\n"
        return toReturn   
            
    def __getitem__(self, index):
        """ return the element at the index expressed as a tuple """
        columns = index[0] 
        rows = index[1] 
        
        temp = self.headnode
        for x in range(rows):
            temp = temp.south 
        for y in range(columns):
            temp = temp.east
            
        return temp.value

    def __setitem__(self, index, a):
        """ set value at index to a """
        columns = index[0] 
        rows = index[1] 
               
        temp = self.headnode
        for x in range(rows):
            temp = temp.south 
        for y in range(columns):
            temp = temp.east
        temp.value = a
        
        
    def __iter__(self):
	"""returns a list of all the items in the matrix first across down then across repeat"""
        x = self.headnode
        y = self.headnode
	for a in range(self.dimensions[1]):
	    for b in range(self.dimensions[0]):
		if x is None:
		    raise StopIteration
		else:
		    value = x.value
		    if x.east != None:
			x = x.east
		    elif y.south != None:
			y = y.south
			x = y
		    else:
			x = None 
		    yield value
	    
    def insertRow(self, rowIndex, defaultValue = None):
        """inserts a row at the given index, shifting columns if necessary"""
        if defaultValue is None:
            defaultValue = self.defaultValue
	
	if self.dimensions[1] == 1 and rowIndex == 1:
	    temp = self.headnode
	    tempUp = temp
	    newNode = Node(defaultValue)
	    temp = newNode
	    
	    temp.north = tempUp
	    tempUp.south = temp
	    
	    for y in range(self.dimensions[0] - 1):
		tempUp = tempUp.east
		newNode = Node(defaultValue)
		
		newNode.west = temp
		temp.east = newNode
		
		newNode.north = tempUp
		tempUp.south = newNode
		
		temp = newNode
	    
	elif rowIndex == 0:
	    
	    temp = self.headnode
	    tempDown = temp
	    newNode = Node(defaultValue)
	    temp = newNode
	    
	    for y in range (self.dimensions[0]):
		newNode = Node(defaultValue)
		newNode.west = temp
		temp.east = newNode
            
		temp.south = tempDown
		tempDown.north = temp 
		tempDown = tempDown.east
            
		temp = newNode
	
	elif rowIndex == (self.dimensions[1] - 1):
	    
	    temp = self.headnode
	    for x in range(self.dimensions[1] - 1):
		temp = temp.south
		
	    tempUp = temp
	    newNode = Node(defaultValue)
	    temp = newNode
	     	    
	    
	    for y in range (self.dimensions[0] - 1):
		
		temp.north = tempUp
		tempUp.south = temp
		tempUp = tempUp.east	
		
		newNode = Node(defaultValue)
		newNode.west = temp
		temp.east = newNode
			
		temp = newNode	    
	
	elif rowIndex < (self.dimensions[1] - 1) and rowIndex != 0:
	    
	    tempUp = None
	    tempDown = None
	    temp = self.headnode
	    
	    for x in range(rowIndex):
		temp = temp.south 
	    
	    tempUp = temp.north
	    tempDown = temp
	    newNode = Node(defaultValue)
	    temp = newNode

	    for y in range (self.dimensions[0] - 1):
		newNode = Node(defaultValue)
		newNode.west = temp
		temp.east = newNode
			
		temp.north = tempUp
		tempUp.south = temp
		tempUp = tempUp.east
			    
		temp.south = tempDown
		tempDown.north = temp 
		tempDown = tempDown.east
			
		temp = newNode	    
        
        self.rows += 1
        self.dimensions = (self.columns, self.rows)        
        
    def insertColumn(self, colIndex, defaultValue = None):
        """inserts a column at the given index, shifting columns if necessary"""
        if defaultValue is None:
            defaultValue = self.defaultValue
	    
	if self.dimensions[0] == 1 and colIndex == 1:
	    temp = self.headnode
	    tempWest = temp
	    newNode = Node(defaultValue)
	    temp = newNode
	    
	    temp.west = tempWest
	    tempWest.east = temp
	    
	    for y in range(self.dimensions[1] - 1):
		tempWest = tempWest.south
		newNode = Node(defaultValue)
		
		newNode.north = temp
		temp.south = newNode
		
		newNode.west = tempWest
		tempWest.east = newNode
		
		temp = newNode
	    
	
	elif colIndex == 0:
	    temp = self.headnode 
	    tempEast = temp
	    newNode = Node(defaultValue)
	    temp = newNode
	    
	    for y in range(self.dimensions[1]):
		newNode = Node(defaultValue)
		newNode.north = temp
		temp.south = newNode
			   
		temp.east = tempEast
		tempEast.west = temp
		tempEast = tempEast.south
		       
		temp = newNode	    
	
	elif colIndex == (self.dimensions[0] - 1):
	    temp = self.headnode 
	    
	    for x in range(self.dimensions[0] - 1):
		temp = temp.east
		
	    tempWest = temp
	    newNode = Node(defaultValue)
	    temp = newNode
	    
	    for y in range(self.dimensions[1]):
		newNode = Node(defaultValue)
		newNode.north = temp
		temp.south = newNode
			   
		temp.west = tempWest
		tempWest.east = temp
		tempWest = tempWest.south
		       
		temp = newNode	    
	
	elif colIndex < (self.dimensions[0] - 1) and colIndex != 0:
	    tempUp = None
	    tempDown = None    
	    temp = self.headnode
        
	    for x in range(colIndex):
		temp = temp.east
        
	    tempWest = temp.west
	    tempEast = temp
	    newNode = Node(defaultValue)
	    temp = newNode
	    
	    for y in range(self.dimensions[1]):
		newNode = Node(defaultValue)
		newNode.north = temp
		temp.south = newNode
            
		temp.east = tempEast
		tempEast.west = temp
		tempEast = tempEast.south
		
		temp.west = tempWest
		tempWest.east = temp
		tempWest = tempWest.south
            
		temp = newNode
        
	
        self.columns += 1
        self.dimensions = (self.columns, self.rows)        

    def removeRow(self, rowIndex):
        """removes a row at the given index, shifting rows if necessary"""
	
	if rowIndex == 0:
	    temp = self.headnode
	    tempDelete = temp
	    temp = temp.south
	    self.headnode = temp
	    
	    for y in range(self.dimensions[0] - 1):
		tempDelete.south = None
		temp.north = None
		
		tempDelete = tempDelete.east
		temp = temp.east
	
	elif rowIndex == (self.dimensions[1] - 1):
	    temp = self.headnode
	    
	    for x in range(self.dimensions[1] - 1):
		temp = temp.south
		
	    tempDelete = temp
	    temp = temp.north
	    self.headnode = temp
	
	    for y in range(self.dimensions[0] - 1):
		tempDelete.north = None
		temp.south = None
		
		tempDelete = tempDelete.east
		temp = temp.east
		
	elif rowIndex < (self.dimensions[1] - 1) and rowIndex != 0:
	    temp = self.headnode
	    
	    for x in range(rowIndex):
		temp = temp.south
        
	    tempDelete = temp
	    tempUp = temp.north
	    tempDown = temp.south    
	    
            for y in range(self.dimensions[0] - 1):
		
		tempDelete.south = None
		tempDelete.north = None
		
		tempUp.south = tempDown
		tempDown.north = tempUp
		
                tempDelete = tempDelete.east
		tempUp = tempUp.east
		tempDown = tempDown.east
                
        self.rows -= 1
        self.dimensions = (self.columns, self.rows)
          
    def removeColumn(self, colIndex):
        """removes a column at the given index, shifting columns if necessary"""
	
	if colIndex == 0:
	    temp = self.headnode
	    tempDelete = temp
	    temp = temp.east
	    self.headnode = temp
	    
	    for y in range(self.dimensions[1] - 1):
		tempDelete.east = None
		temp.west = None
		
		tempDelete = tempDelete.south
		temp = temp.south
	
	elif colIndex == (self.dimensions[0] - 1):
	    temp = self.headnode
	    
	    for x in range(self.dimensions[0] - 1):
		temp = temp.east
	    
	    tempDelete = temp
	    temp = temp.west
	    
	    for y in range(self.dimensions[1]):
		tempDelete.west = None
		temp.east = None
		
		tempDelete = tempDelete.south
		temp = temp.south
	
	elif colIndex < (self.dimensions[0] - 1) and colIndex != 0:
	    temp = self.headnode
	    
	    for x in range(colIndex):
		temp = temp.east	    
        
	    tempDelete = temp
	    tempWest = temp.west
	    tempEast = temp.east
	    
	    for y in range(self.dimensions[1]):
		tempDelete.west = None
		tempDelete.east = None
		
		tempWest.east = tempEast
		tempEast.west = tempWest
		
		tempDelete = tempDelete.south
		tempWest = tempWest.south
		tempEast = tempEast.south
	    
        self.columns -= 1
        self.dimensions = (self.columns, self.rows)    
    