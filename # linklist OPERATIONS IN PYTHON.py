#print("Invalid Choice!")
# Linked List Example - Train Coaches

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Creating nodes
coach1 = Node("Coach1")
coach2 = Node("Coach2")
coach3 = Node("Coach3")

# Linking nodes
coach1.next = coach2
coach2.next = coach3

# Display linked list
temp = coach1

print("Train Coaches:")

while temp:
    print(temp.data, end=" -> ")
    temp = temp.next

print("None")