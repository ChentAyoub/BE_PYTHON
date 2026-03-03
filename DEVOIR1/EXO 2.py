contacts = []
print("Welconme to your contact book")
while True:
    print("1 Add a contact")
    print("2 View contacts")
    print("3 Exit")

    Choice = input("Enter your choice: ")
    Choice = int(Choice)

    if Choice == 1:
        new_contact = input("Enter the name of the contact: ")
        contacts.append(new_contact)
        print ("Contact added successfully")
    elif Choice == 2:
        print("Your contacts: ")
        for index, contact in enumerate(contacts, start=1):
            print(f"{index}. {contact}")
    elif Choice == 3:
        print("Exiting the contact book goodbye")
        break
    else:
        print("Invalid choice please try 1, 2 or 3 as a choice")