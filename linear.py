# Linear Search Example

students = ["Rahul", "Aman", "Neha", "Prachi", "Riya"]

target = "Prachi"

found = False

for i in range(len(students)):
    if students[i] == target:
        print(f"{target} found at position {i+1}")
        found = True
        break

if not found:
    print("Student not found")