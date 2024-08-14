names = []
contact_numbers = []

def add_contact(name, number):
    names.append(name)
    contact_numbers.append(number)
    print(f"Contact {name} added successfully!")

def display_contacts():
    print("\nName\t\tContact Number")
    for i in range(len(names)):
        print(f"{names[i]}\t\t{contact_numbers[i]}")

def search_contact(search_term):
    if search_term in names:
        index = names.index(search_term)
        print(f"Name: {search_term}, Phone Number: {contact_numbers[index]}")
    else:
        print("No records found.")

# Main program loop
while True:
    print("\nContact Book Menu:")
    print("1. Add Contact")
    print("2. Display Contacts")
    print("3. Search Contact")
    print("4. Exit")
    
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        name = input("Enter name: ")
        number = input("Enter contact number: ")
        add_contact(name, number)
    elif choice == 2:
        display_contacts()
    elif choice == 3:
        search_term = input("Enter name to search: ")
        search_contact(search_term)
    elif choice == 4:
        print("Exiting Contact Book. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
