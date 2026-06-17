# Circular Linked List - Round Robin Tournament

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Create nodes
team1 = Node("Team A")
team2 = Node("Team B")
team3 = Node("Team C")

# Connect nodes
team1.next = team2
team2.next = team3
team3.next = team1  # Circular Link

# Display first 6 turns
temp = team1

print("Tournament Turns:")

for i in range(6):
    print(temp.data, end=" -> ")
    temp = temp.next