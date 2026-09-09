def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero")
    return x / y

def main():
    while True:
        print("\n Simple Calculator - Calculator.py:17")
        print("1. Addition - Calculator.py:18")
        print("2. Subtraction - Calculator.py:19")
        print("3. Multiplication - Calculator.py:20")
        print("4. Division - Calculator.py:21")
        print("5. Quit - Calculator.py:22")

        choice = input("Choose an operation (1-5): ")

        if choice == "5":
            print("Goodbye! - Calculator.py:27")
            break

        if choice in ["1", "2", "3", "4"]:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == "1":
                print(f"Result: {num1} + {num2} = {add(num1, num2)} - Calculator.py:35")
            elif choice == "2":
                print(f"Result: {num1}  {num2} = {subtract(num1, num2)} - Calculator.py:37")
            elif choice == "3":
                print(f"Result: {num1} * {num2} = {multiply(num1, num2)} - Calculator.py:39")
            elif choice == "4":
                try:
                    print(f"Result: {num1} / {num2} = {divide(num1, num2)} - Calculator.py:42")
                except ValueError as e:
                    print(e)
        else:
            print("Invalid choice. Please choose a number from 1 to 5. - Calculator.py:46")

if __name__ == "__main__":
    main()