from src.homework.g_lists_and_tuples.lists import (
    get_lowest_list_value,
    get_highest_list_value,
)

def prompt_for_numbers():
    numbers = []
    while True:
        try:
            num = float(input("Enter a list value: ").strip())
        except ValueError:
            print("Please enter a valid number.")
            continue
        numbers.append(num)

        if len(numbers) >= 3:
            cont = input("Do you want to enter another value? (y/n): ").strip().lower()
            if cont and cont[0] == "n":
                break
    return numbers

def main():
    while True:
        print("\n1 - Show the list low/high values")
        print("2 - Exit")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            numbers = prompt_for_numbers()
            low = get_lowest_list_value(numbers)
            high = get_highest_list_value(numbers)
            if low is None or high is None:
                print("No values provided.")
            else:
                print(f"\nLowest value: {low}")
                print(f"Highest value: {high}")
        elif choice == "2":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()