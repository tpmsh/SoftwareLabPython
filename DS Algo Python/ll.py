class Node:
    def __init__(self, data):
        self.data = data
        self.link = None

class List:
    def __init__(self):
        self.head = None

n1 = List()

n2 = Node(5)

n3 = Node(7)

n1.head = n2

n2.link = n3

print(n2.data, n2.link, n3.data, n3.link)

temp = n1.head

while temp is not None:
    print(temp.data, end = ", ")
    temp = temp.link
