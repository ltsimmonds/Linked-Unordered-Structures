"""Originally created in Spring of 2018
Recently revised (10/28/2022) to improve pop() functionality"""

#Node class for use in LinkedList
class Node:
    
    def __init__(self, data):
        self.data = data
        self.next = None
        
    def __str__(self):
        return self.data
   
    
class LinkedList:
    
    #Includes a length attribute for ease of knowing the size.
    def __init__(self):
        self.head = None
        self.length = 0
        
        
    def is_empty(self):
        if self.head == None:
            return True
        else:
            return False
        
        
    def size(self):
        return self.length
    
    #Adds a Node to the beginning of the linked list.
    #Increases size by 1.
    def add(self, item):
        node = Node(item)
        node.next = self.head
        self.head = node
        self.length += 1
    
    #Overriding iteration so linked lists can be used in loops.
    def __iter__(self):
        current = self.head
        while current is not None:
            yield current
            current = current.next

    #Adds a Node to the end of the linked list
    #If linked list is empty, new Node becomes list's head
    #If linked list is not empty, new Node becomes last element.
    #Increase size by 1.
    def append(self, item):
        if self.head == None:
            self.head = Node(item)
            self.length += 1
        else:
            current = self.head
            stop = False
            while current != None and not stop:
                if current.next == None:
                    current.next = Node(item)
                    self.length += 1
                    stop = True   
                current = current.next
    
    #Removes and Returns any Node in the list by position, like Python's array-based pop().
    #Default position is None, which "pops" off the last node in the linked list.
    #Decreases size by 1.
    def pop(self, pos = None):
        current = self.head
        prev_node = None
        count = 0

        #Rudimentary error-catching.
        if pos == None:                                 #Sets final index to pop
            pos = self.length-1
        elif type(pos) != int:                          #If index to pop isn't an integer, return None.
            return None
        elif self.length == 0:                          #If linked list is empty, there's nothing to pop.
            return None
        elif pos < 0 or pos > (self.length - 1):        #If index to pop is outside the linked lists size, there's nothing to pop.
            return None
        
        #Case for if the linked list to pop from contains only ONE Node.
        if self.length == 1:
            temp = self.head
            self.head = None
            self.length -= 1
            return temp
        
        #If the linked list contains more than one Node: iterate up UNTIL the last Node.   
        while count <= pos and current.next != None:
            
            if count == pos and prev_node == None:      #if index is found and is the list's head,
                self.head = current.next()              #pop and decrease size.
                temp = current.data
                current = None
                self.length -= 1
                return temp
            elif count == pos and prev_node != None:    #if index is found and is in the "middle" of the list,
                prev_node.next = current.next()         #pop and decrease size.
                temp = current.data
                current = None
                self.length -= 1
                return temp
            else:                                       #if index is not found yet, move onto next Node.
                count += 1
                prev_node = current
                current = current.next
                
        if current.next == None:                        #If nothing was returned in the prior loop because index was not found,
            temp = current.data                         #pop the last Node in the linked list
            prev_node.next = None                       #as the pop-position and index values should theoretically match, after error catching
            self.length -= 1
            return temp
    
    #Checks if a given data value is present as a Node's data in the linked list
    #Returns True, if value is present, False if not.
    def search(self, item):
        current = self.head
        if self.head == None:
            return False
        while current != None:
            if current.data == item:
                return True
            elif current.data != item and current.next != None:
                current = current.next
            else:
                return False
            
    #Removes an Item in the list by data value and breaks loop.
    #Decreases size by 1 and returns nothing.
    #However, if the data to remove does NOT exist, "None" is returned.        
    def remove(self, item):
        current = self.head
        prev_node = None
        stop = False
        while current != None or stop != True:
            if current.data == item:
                if prev_node != None:
                    prev_node.next = current.next
                    self.length -= 1
                    stop = True
                else:
                    self.head = current.next
                    self.length -= 1
                    stop = True
            if current.data != item and current.next == None:
                return None #item is not in the list
            prev_node = current
            current = current.next
