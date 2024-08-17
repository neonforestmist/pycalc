import math

# Define mathematical operations
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def exponentiate(base, exp):
    return base ** exp

def square_root(x):
    return math.sqrt(x)

# Display options
def show_menu():
    print("\nSelect operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exponentiate (base then exponent number)")
    print("6. Square Root")


def main():
    while True:
        show_menu()
        choice = input("Enter choice (1-6): ")

        if choice in ('1', '2', '3', '4', '5', '6'):
            if choice == '6':  # Square Root
                num = float(input("Enter number: "))
                print(f"√{num} = {square_root(num)}")
            elif choice in ('5'):  # Exponent
                base = float(input("Base number: "))
                exp = float(input("Exponent: "))
                print(f"{base}^{exp} = {exponentiate(base, exp)}")
            else:
                num1 = float(input("First number: "))
                num2 = float(input("Second number: "))

                if choice == '1':
                    print(f"{num1} + {num2} = {add(num1, num2)}")
                elif choice == '2':
                    print(f"{num1} - {num2} = {subtract(num1, num2)}")
                elif choice == '3':
                    print(f"{num1} * {num2} = {multiply(num1, num2)}")
                elif choice == '4':
                    if num2 != 0:
                        print(f"{num1} / {num2} = {divide(num1, num2)}")
                    else:
                        print("Error: Division by zero is not allowed.")

        else:
            print("Invalid input. Please select a valid operation.")

        # Checks if user wants to do another calculation
        continue_calculating = input("Do you want to do another calculation? (yes/no): ").strip().lower()
        if continue_calculating != "yes":
            print("Bye.")
            break

if __name__ == "__main__":
    main()
