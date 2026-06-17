# Circular Queue Example - Traffic Signal

signals = ["Red", "Yellow", "Green"]

print("Traffic Signal Cycle:")

for i in range(9):
    print(signals[i % 3])