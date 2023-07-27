# Stacks implemented using Linked List

class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

class Stack: 
    def __init__(self):
        self.top = None
    
    def isEmpty(self):
        return self.top == None 
    
    def push(self,value):

        #Basically insertion at head

        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
    
    def traverse(self):
        temp = self.top

        while temp:
            print(temp.data)
            temp = temp.next
    
    def peek(self):
        if (self.isEmpty()):
            return 'Stack Empty'
        else:
            return self.top.data
    
    def pop(self):

        #Basically deletion at head

        if (self.isEmpty()):
            return 'Stack Empty'
        else:
            data = self.top.data
            self.top = self.top.next
            return data

    
    def size(self):
        size = 0
        if self.isEmpty():
            return size
        
        temp = self.top
        while temp:
            size +=1
            temp = temp.next
        return size

#String Reversal using Stacks
def reverse_string(text):
    s = Stack()
    for i in text:
        s.push(i)
    result = ""
    while (not s.isEmpty()):
        result += s.pop()
    
    print(result)

#Text Editor (Undo - Redo)
## Use Two Stacks
def text_editor(text,pattern):

    u = Stack()
    for char in text:
        u.push(char)
    
    r = Stack()
    for to_do in pattern:
        if to_do == 'u':
            r.push(u.pop())
        elif to_do == 'r':
            u.push(r.pop())
    result =""
    while (not u.isEmpty()):
        result = u.pop()+ result
    
    print(result)

#Balanced Paranthesis
def bal_bracket(pattern):
    s = Stack()
    for char in pattern:
        if char in ['(','{','[']:
            s.push(char)
        else:
            if char == ')':
                if s.pop() == '(':
                    pass
                else:
                    return False
            elif char == '}':
                if s.pop() == '{':
                    pass
                else:
                    return False
            elif char == ']':
                if s.pop() == '[':
                    pass
                else:
                    return False
    return s.isEmpty()
                

# Celebrity Problem
#https://youtu.be/f9Aje_cN_CY?t=21191

# A celeb is someone whom everyone knows, but he doesn't know any of the others
def find_the_celeb(L):
    s = Stack()

    for i in range(L):
        s.push(i)
    
    while s.size()>=2:
         i = s.pop()
         j = s.pop()

         if L[i][j] == 0:
             #j is not a celeb
             s.push(i)
         else:
             #i is not a celeb
             s.push(j)
    celeb = s.pop()
    for i in range(len(L)):

        if i != celeb:
            if L[i][celeb] == 0 or L[celeb][i]:
                return 'No one is a celebrity'
    
    return f'The celebrity is: {celeb}'
