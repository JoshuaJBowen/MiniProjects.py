#Linked List
#Josh Bowen
#April 1st, 2022

class Node():

    def __init__(self, data=None):
        self.data = data
        self.next = None

    def next(self, Node_n):
        self.next = Node_n

    def get_next(self):
        if self.next != None:
            return self.next
        else:
            return "oops"

        
class LinkedList():

    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def append(self, data):
        newNode = Node(data)
        if self.tail:
            self.tail.next = newNode
            self.tail = newNode
        else:
            self.head = newNode
            self.tail = newNode
        self.count += 1

    def iterate(self):
        current = self.head
        while current:
            value = current.data
            current = current.next
            yield value

    def search_item(self, search_value):
        for val in self.iterate():
            if val == search_value:
                return True
        return False
        


LL = LinkedList()
LL.append(0)
LL.append(1)
LL.append(2)
LL.append(3)
    
print("Size of Linked List : " + str(LL.count))

print(LL.search_item(4))


    





    


