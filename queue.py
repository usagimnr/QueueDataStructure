########################################
#                                      
# This is a programmed queue data structure which follow the order
# First In First Out (FIFO) meaning the first data item store is the
# first accessed.             
#  
########################################

class Node:
    def __init__(self, value):
        self.value = value  
        self.next = None 
    
    def __str__(self):
        return "Node({})".format(self.value) 

    __repr__ = __str__
                        
                          
class Queue:

    def __init__(self): 
        self.head=None
        self.tail=None
        self.count = 0

    def __str__(self):
        temp=self.head
        out=[]
        while temp:
            out.append(str(temp.value))
            temp=temp.next
        out=' '.join(out)
        return ('Head:{}\nTail:{}\nQueue:{}'.format(self.head,self.tail,out))

    __repr__=__str__

    def isEmpty(self):
        if self.head == None:
            return True
        else:
            return False

    def __len__(self):
        return self.count

    def enqueue(self, value):
        if self.head == None:
            nn = Node(value)
            self.tail = nn
            self.head = nn 
            self.count += 1
        else: 
            nn = Node(value)
            self.tail.next = nn
            self.tail = nn
            self.count += 1

    def dequeue(self):
        if self.count == 0:
            return 'Queue is empty'
        elif self.count == 1:
            x = self.head.value
            self.head = None
            self.tail = None
            self.count -= 1
            return x
        else:
            x = self.head.value
            self.head = self.head.next
            self.count -= 1
            return x

