class Node:
    def __init__(self,x,y = None):
        self.value = x
        self.next = y

class SinglyLinkedList:
    def __init__(self):
        self.top = None

    def insert(self,n,x):
        if n == 0 or not self.top:
            self.top = Node(x,self.top)
        else:
            obj = self.top
            while obj.next:
                n -= 1
                if n == 0:
                    break
                obj = obj.next
            objNew = Node(x,obj.next)
            obj.next = objNew