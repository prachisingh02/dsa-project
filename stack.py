# Stack Example - Music Player

stack = []

# Push songs
stack.append("Believer")
stack.append("Faded")
stack.append("Alone")

print("Songs in Stack:")
print(stack)

# Pop song
previous_song = stack.pop()

print("\nPrevious Song:", previous_song)

print("\nRemaining Songs:")
print(stack)