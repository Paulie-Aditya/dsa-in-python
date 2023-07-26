'''
Node
Create a LL
len
insert from head
traverse/print
insert from tail (append)
insert in middle (insert)

clear
delete from head
delete from tail(pop)
delete by value(remove)

search by value (find)
delete by index -> del L[0]
search by index (indexing)
'''

class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

a = Node(1)
b = Node(2)
c = Node(3)

a.next = b
b.next = c

#Linked List has been created

class LinkedList:

    def __init__(self):
        self.head = None #Condition for empty list
        self.n = 0
    
    def __len__(self):
        return self.n
    
    #Insert
    def insert_head(self,value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node    
        self.n +=1
    
    def append(self,value):
        if self.head == None:
            self.head = Node(value)
            return
        
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = Node(value)

        self.n +=1
    
    def insert_after(self,after,value):
        #after represents after which node do we need to insert

        new_node = Node(value)
        curr = self.head
        while curr:
            if curr.data == after:
                break
            curr = curr.next
        
        if curr == None:
            return 'Item not Found'
        
        new_node.next = curr.next
        curr.next = new_node 

        self.n +=1


    #Delete

    def clear(self):
        self.head = None
        self.n = 0
    
    def delete_head(self):
        if self.head == None:
            return 'Empty Linked List'
        self.head = self.head.next
        self.n -=1
    
    def pop(self):
        curr = self.head
        if self.head == None:
            return 'Empty Linked List'
        
        elif self.head.next == None:
            return self.delete_head()

        while curr.next.next:
            curr = curr.next
        
        curr.next = None
        self.n -=1
    
    def remove(self,value):
        if self.head == None:
            return 'Empty LL'
        
        curr = self.head

        if curr.data == value:
            return self.delete_head()
        
        while curr.next:
            if curr.next.data == value:
                break
            curr = curr.next
        if curr.next == None:
            return 'Not Found'    
        curr.next = curr.next.next
        self.n -=1
    
    def del_by_index(self,index):
        pos = 0
        curr = self.head
        if curr == None:
            return 'Empty LL'
        if curr.next == None:
            if index in [0,1]:
                if index == 0:
                    return self.delete_head()
                elif index == 1:
                    curr.next = None
                    return 
                self.n -=1
        if index == 0:
            return self.delete_head()
        while curr.next.next:
            if pos+1 == index:
                break
            pos+=1
            curr = curr.next
        
        if curr == None:
            return 'IndexError'
        
        curr.next = curr.next.next
        self.n -=1
        return
    
    #Searching

    def search(self,item):
        curr = self.head
        pos = 0
        while curr:
            if curr.data == item:
                return pos
            pos+=1
            curr = curr.next
        return 'Not Found'
    
    def __getitem__(self, index):
        curr = self.head
        pos = 0
        while curr:
            if pos == index:
                return curr.data
            pos +=1
            curr = curr.next
        return 'IndexError'

    def __str__(self):
        curr = self.head
        result = ''
        while curr:
            result += str(curr.data) + "->"
            curr = curr.next
        return f'{result.rstrip("->")}' 
    
    def reverse(self):
        #in-place
        prev_node = None
        curr_node = self.head
        while curr_node:
            next_node = curr_node.next
            curr_node.next = prev_node

            #shifting both nodes
            prev_node = curr_node
            curr_node = next_node

        self.head = prev_node
    





        