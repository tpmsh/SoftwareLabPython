class Node:
    def __init__(self, data):
        self.data = data
        self.link = None

class List:
    def __init__(self):
        self.head = None

    def insertBeg(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
        else:
            newNode.link = self.head
            self.head = newNode

    def traverse(self):
        temp = self.head
        while temp is not None:
            print(temp.data, end = ', ')
            temp = temp.link

l = List()
l.insertBeg(5)
l.insertBeg(7)
l.insertBeg(9)
l.traverse()
