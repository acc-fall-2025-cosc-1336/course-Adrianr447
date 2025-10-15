from src.homework.d_repetition.repetition import get_factorial, sum_odd_numbers

def main():
    while True:
        print("\nHomework 4 Menu")
        print("1-Factorial")
        print("2-Sum odd numbers")
        print("3-Exit")
        choice = input("Select an option: ")
        if choice == '1':
            while True:
                try:
                    n = int(input("Enter a number (1-9): "))
                    if 1 <= n < 10:
                        print(f"Factorial of {n} is {get_factorial(n)}")
                        break
                    else:
                        print("Number must be between 1 and 9.")
                except ValueError:
                    print("Invalid input. Enter an integer.")
        elif choice == '2':
            while True:
                try:
                    n = int(input("Enter a number (1-99): "))
                    if 1 <= n < 100:
                        print(f"Sum of odd numbers up to {n} is {sum_odd_numbers(n)}")
                        break
                    else:
                        print("Number must be between 1 and 99.")
                except ValueError:
                    print("Invalid input. Enter an integer.")
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()