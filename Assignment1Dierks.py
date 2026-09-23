#Program Name:Assignment1.py
#Course: IT3883/Section 01
#Student Name: Erica Dierks
#Assignment Number: Assignment 1
#Due Date: 09/22/2026
#Purpose: This program creates a menu that allows the user to add,
#clear, or display text that is stored in an input buffer

input_buffer = ""

while True:
    print("\nMenu")
    print("1. Append data to the input buffer")
    print("2. Clear the input buffer")
    print("3. Display the input buffer")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        text = input("Enter a string: ")
        input_buffer += text
        print("Data added to the input buffer.")

    elif choice == "2":
        input_buffer = ""
        print("Input buffer cleared.")

    elif choice == "3":
        print("Input buffer:", input_buffer)

    elif choice == "4":
        print("Exiting program.")
        break

    else:
        print("Invalid choice. Please enter 1, 2, 3, or 4.")
