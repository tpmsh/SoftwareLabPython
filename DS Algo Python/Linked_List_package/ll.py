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

    def insertEnd(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
        else:
            temp = self.head
            while temp.link is not None:
                temp = temp.link
            temp.link = newNode

    

    def traverse(self):
        temp = self.head
        while temp is not None:
            print(temp.data, end = ', ')
            temp = temp.link
