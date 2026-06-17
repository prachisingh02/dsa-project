# Doubly Linked List - Browser History

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

# Create pages
google = Node("Google")
youtube = Node("YouTube")
github = Node("GitHub")

# Connect pages
google.next = youtube

youtube.prev = google
youtube.next = github

github.prev = youtube

# Forward Traversal
print("Forward Navigation:")
temp = google

while temp:
    print(temp.data, end=" -> ")
    temp = temp.next

print("None")

# Backward Traversal
print("\nBackward Navigation:")
temp = github

while temp:
    print(temp.data, end=" -> ")
    temp = temp.prev

print("None")