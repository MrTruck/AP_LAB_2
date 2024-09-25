print("Select operation:")
print("+ Add")
print("- Subtract")
print("* Multiply")
print("/ Divide")

while True:
    choice = input("Enter choice (+, -, *, /): ")

    if choice in ('+', '-', '*', '/'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '+':
            result = num1 + num2
            print(f"{num1} + {num2} = {result}")
        elif choice == '-':
            result = num1 - num2
            print(f"{num1} - {num2} = {result}")
        elif choice == '*':
            result = num1 * num2
            print(f"{num1} * {num2} = {result}")
        elif choice == '/':
            if num2 == 0:
                print("Error! Division by zero.")
            else:
                result = num1 / num2
                print(f"{num1} / {num2} = {result}")
    else:
        print("Invalid input. Please enter a valid operator (+, -, *, /).")

    next_calculation = input("Do you want to perform another calculation? (yes/no): ")
    if next_calculation.lower() != 'yes':
        print("Goodbye :)")
        break
    