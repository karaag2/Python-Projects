def add(a: int, b: int)->int:
    return a + b

def subtract(a: int, b: int)->int:
    return a-b

def multiply(a: int, b: int)->int:
    return a*b

def divide(a: int, b: int)->float:
    try:
        return a/b
    except ZeroDivisionError:
        return 0
def displayMenu():
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")
def main():
    while True:
        print("Enter two numbers: ")
        try:
            a = int(input("a:"))
            b = int(input("b:"))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            return 0
        while True:
            displayMenu()
            choice = input("Enter your choice: ")
            if choice == "1":
                print(f"The result is: {add(a, b)}")
            elif choice == "2":
                print(f"The result is: {subtract(a, b)}")
            elif choice == "3":
                print(f"The result is: {multiply(a, b)}")
            elif choice == "4":
                print(f"The result is: {divide(a, b) if divide(a, b) != 0 else 'Cannot divide by zero'}")
            elif choice == "5":
                print("Thank you for using the calculator!")
                return
            else:
                print("Invalid choice. Please try again.")
main()