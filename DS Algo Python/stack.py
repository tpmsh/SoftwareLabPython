class Stack:
    def __init__(self):
        self.stack = []

    def push(self, ele):
        self.stack.append(ele)

    def pop(self):
        self.stack.pop()

    def traverse(self):
        for ele in self.stack:
            print(ele, end = ', ')

s = Stack()

while(True):
    print("\n1 - Push\n2 - Pop\n3 - Traverse\n4 - Exit")
    choice = (input("Enter Choice : ")).lower()
    if(choice == 'push'):
        num = int(input("Enter a Number : "))
        s.push(num)
    if(choice == 'pop'):
        s.pop()
    if(choice == 'traverse'):
        s.traverse()
    if(choice == 'quit'):
        break

print("-------Thankyou for using Stack----------")
