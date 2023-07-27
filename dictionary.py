#Done using Linear Probing
class Dictionary:

    def __init__(self,size):
        self.size = size
        self.slots = [None]*self.size #Keys
        self.data = [None]*self.size #Values
    
    def put(self,key,value):
        hash_value = self.hash_function(key)

        if self.slots[hash_value] == None:
            self.slots[hash_value] = key
            self.data[hash_value] = value
        else:
            if self.slots[hash_value] == key:
                #Key exists already
                #Update value
                self.data[hash_value] = value
            else:
                # Something else exists here
                new_hash_value = self.rehash(hash_value)
                
                while self.slots[new_hash_value] != None and self.slots[new_hash_value] != key:
                    new_hash_value = self.rehash(new_hash_value)
                
                if self.slots[new_hash_value] == None:
                    self.slots[new_hash_value] = key
                    self.data[new_hash_value] = value
                else:
                    self.data[new_hash_value] = value

    def get(self,key):
        start_position = abs(hash(key)) % self.size
        curr = start_position

        while self.slots[curr] != None:
            if self.slots[curr] == key:
                return self.data[curr]
            
            curr = self.rehash(curr)

            if curr == start_position:
                return 'Not Found'
        return 'Not Found'
    
    def __setitem__(self, key, value):
        self.put(key,value)
    
    def __getitem__(self,key):
        return self.get(key)
    
    def __str__(self):
        for i in range(self.size):
            if self.slots[i] != None:
                print(self.slots[i],":",self.data[i], end=" ")
        return ''
                
    
    def rehash(self,old_hash,count=0):
        #Linear Probing
        return (old_hash + 1) % self.size
        #Quadratic Probing
        count +=1
        return (old_hash + (count-1) **2)%self.size
    

    def hash_function(self,key):
        return abs(hash(key)) % self.size

d1 = Dictionary(3)
d1['python'] = 80
print(d1.slots)
print(d1.data)

print(d1)