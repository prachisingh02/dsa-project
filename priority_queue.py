import heapq

# Create Priority Queue
patients = []

# Add patients (negative priority for max priority)
heapq.heappush(patients, (-1, "Fever"))
heapq.heappush(patients, (-10, "Heart Attack"))
heapq.heappush(patients, (-2, "Cold"))

print("Treatment Order:")

while patients:
    priority, patient = heapq.heappop(patients)
    print(patient)