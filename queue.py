from collections import deque

# Create Queue
queue = deque()

# Enqueue customers
queue.append("Rahul")
queue.append("Priya")
queue.append("Aman")
queue.append("Neha")

print("Customers in Queue:")
print(list(queue))

# Dequeue customer
served = queue.popleft()

print("\nCustomer Served:", served)

print("\nRemaining Queue:")
print(list(queue))