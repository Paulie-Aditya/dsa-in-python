# Queue using 2 stacks

'''
1 stack for enqueing
1 stack for dequeing
'''

'''
if enqueue:
    s1.push(item)
else:
    is s2 empty:
        if s1 empty:
            empty
        else:
            push all to s2, dequeue
    else:
        s2.pop()
'''
from . import stacks
s1 = stacks.Stack()
s2 = stacks.Stack()

def enqueue(self,value):
    s1.push(value)

def dequeue(self):
    if s2.isEmpty():
        if s1.isEmpty():
            return 'Empty Queue'
        else:
            for i in range(s1.size()):
                s2.push(s1.pop())
            s2.pop()
    else:
        s2.pop()