class Node:
    def __init__(self, key,value):
        self.key = key
        self.value = value
        self.next = None



class LinkedList:

    def __init__(self):
        self.head = None #Condition for empty list
        self.n = 0
    
    def __len__(self):
        return self.n

    
    def append(self,key,value):
        if self.head == None:
            self.head = Node(key, value)
            return
        
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = Node(key,value)

        self.n +=1
    
    def delete_head(self):
        if self.head == None:
            return 'Empty Linked List'
        self.head = self.head.next
        self.n -=1
    
    def remove(self,key):
        if self.head == None:
            return 'Empty LL'
        
        curr = self.head

        if curr.key == key:
            return self.delete_head()
        
        while curr.next:
            if curr.next.key == key:
                break
            curr = curr.next
        if curr.next == None:
            return 'Not Found'    
        curr.next = curr.next.next
        self.n -=1

    def search(self,key):
        curr = self.head
        pos = 0
        while curr:
            if curr.key == key:
                return pos
            pos+=1
            curr = curr.next
        return -1
    
    def get_node_at_index(self,index):
        temp = self.head
        counter = 0

        while temp:
            if counter == index:
                return temp
            temp = temp.next
            counter +=1
    

    def traverse(self):
        curr = self.head
        while curr:
            print(curr.key, '-->', curr.value, " ", end=" ")
            curr = curr.next


class Dictionary:
    
    def __init__(self,capacity):
        self.capacity = capacity
        self.size = 0

        #create array of LL
        self.buckets = self.make_array(self.capacity)
    
    def make_array(self,capacity):
        L = []
        for i in range(capacity):
            L.append(LinkedList())
        return L
    
    def put(self,key,value):

        bucket_index = self.hash_function(key)
        
        node_index = self.get_node_index(bucket_index,key)

        if node_index == -1:
            #insert 
            self.buckets[bucket_index].append(key,value)
            self.size +=1

        else:
            #update
            node = self.buckets[bucket_index].get_node_at_index(node_index)
            node.value = value

    def get_node_index(self,bucket_index, key):
        node_index = self.buckets[bucket_index].search(key)
        return node_index
    def hash_function(self,key):
        return abs(hash(key))% self.capacity





