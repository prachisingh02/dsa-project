# ARRAY OPERATIONS IN PYTHON

# Initial array (Student Marks)
marks = [80, 75, 92, 88, 70]

while True:
    print("\n===== ARRAY OPERATIONS =====")
    print("1. Display Array")
    print("2. Insert Element")
    print("3. Delete Element")
    print("4. Search Element")
    print("5. Update Element")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("Array Elements:", marks)

    elif choice == 2:
        value = int(input("Enter element to insert: "))
        marks.append(value)
        print("Updated Array:", marks)

    elif choice == 3:
        value = int(input("Enter element to delete: "))

        if value in marks:
            marks.remove(value)
            print("Updated Array:", marks)
        else:
            print("Element not found!")

    elif choice == 4:
        value = int(input("Enter element to search: "))

        if value in marks:
            index = marks.index(value)
            print(f"Element found at index {index}")
        else:
            print("Element not found!")

    elif choice == 5:
        index = int(input("Enter index to update: "))
        new_value = int(input("Enter new value: "))

        if 0 <= index < len(marks):
            marks[index] = new_value
            print("Updated Array:", marks)
        else:
            print("Invalid Index!")

    elif choice == 6:
        print("Program Ended.")
        break

    else:
        print("Invalid Choice!")