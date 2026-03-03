while True:
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        break
    except ValueError:
        print("Invalid input please enter a number")

print("Choose the operation:")
print("1: addition")
print("2: subtraction")
print("3: multiplication")
print("4: division")

choice = input("Your choice (1, 2, 3, or 4): ")

if choice == '1':
    print(f"result= {num1 + num2}")
    
elif choice == '2':
    print(f"result= {num1 - num2}")
    
elif choice == '3':
    print(f"result= {num1 * num2}")
    
elif choice == '4':

    if num2 == 0:
        print("Error: Division by zero")
    else:
        print(f"result= {num1 / num2}")
        
else:
    print("Invalid choice. Please type 1, 2, 3, or 4.")