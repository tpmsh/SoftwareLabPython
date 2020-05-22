from array import *

arr = array('i', [10,20,40,50,60,70,80,90]) # integer array
bytearr = array('b')
unsignedByteArr = array('B')

#charArr = array('C', ['c','h','a','r']) ##doesn't work

unsignedIntArr = array('I')
float4byteArr = array('f')
float8byteArr = array('d')

print(arr)
# Insertion
arr.insert(2,30)
print(arr)
# Deletion
arr.remove(30)
print(arr)

print("Array Index = ",arr.index(70))

arr[3] = 55
print(arr)

# Traversal
for ele in arr:
    print(ele, end = ', ')
