'''
done in vid: 

1. create list
2. len
3. append
4. print
5. indexing
6. pop
7. clear
8. find
9. insert
10. delete
11. remove

'''
'''
left as hw:

sort/min/max/sum/extend
negative indexing
slicing
merge
'''
import ctypes
# Making List in Python using DS of C

class MyList:
    def __init__(self):
        self.size = 1 #Total size
        self.n = 0 #No. of inputs

        self.A = self.make_array(self.size)
    
    def make_array(self, capacity):
        # creates a C type array (static, referential) with size capacity
        return (capacity*ctypes.py_object)()

    def __len__(self):
        return self.n
    
    def __str__(self):
        result = ''
        for i in range(self.n):
            result += str(self.A[i]) + ','
        
        return f'[{result.rstrip(",")}]'
    
    def __getitem__(self,index):
        if 0<=index<self.n:
            return self.A[index]
        else:
            return 'IndexError - Index out of Range'
    
    def __delitem__(self, pos):
        if 0<= pos < self.n:
            for i in range(pos, self.n-1):
                self.A[i] = self.A[i+1]

            self.n -=1 


    def append(self,item):
        if self.n == self.size:
            self.__resize(self.size*2)
        self.A[self.n] = item
        self.n +=1
    
    def __resize(self, new_capacity):
        B = self.make_array(new_capacity)
        self.size = new_capacity

        for i in range(self.n):
            B[i] = self.A[i]

        self.A = B
    
    def pop(self):
        if self.n == 0:
            return 'Empty List'
        else:
            print(self.A[self.n-1])
            self.n -= 1
    
    def clear(self):
        self.n = 0
        self.size = 1
    
    def find(self, item):
        for i in range(self.n):
            if self.A[i] == item:
                return i
        
        return 'ValueError, Not in List'

    def insert(self,pos,item):
        
        if self.n == self.size:
            self.__resize(self.size*2)
        
        for i in range(self.n, pos, -1):
            self.A[i] = self.A[i-1]
        self.A[pos] = item
        self.n +=1
    
    def remove(self,item):
        pos = self.find(item)

        if type(pos) == int:
            self.__delitem__(pos)
        else:
            return pos

        
    

L = MyList()

print(len(L))
L.append(2)
L.append(3)
L.append(4)
L.append(5)
print(L)
print(L.find(2))

L.insert(0,'Hello')
print(L)


