from src.homework.g_lists_and_tuples.lists import (
    get_lowest_list_value,
    get_highest_list_value,
    get_p_distance_matrix,
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

def read_matrix_from_keyboard():
    while True:
        try:
            n = int(input("How many DNA strings (n ≤ 10)? ").strip())
            if n <= 0 or n > 10:
                print("Please enter a number between 1 and 10.")
                continue
            break
        except ValueError:
            print("Please enter a valid integer.")

    dna_lists = []
    length = None

    for i in range(n):
        s = input(f"Enter DNA string #{i+1}: ").strip().upper()
        if length is None:
            if len(s) == 0:
                print("String cannot be empty.")
                return None
            length = len(s)
        else:
            if len(s) != length:
                print("All DNA strings must be the same length.")
                return None
        dna_lists.append([ch for ch in s])

    return dna_lists

def display_matrix(matrix):
    for row in matrix:
        print(" ".join(f"{val:.5f}" for val in row))

def main():
    while True:
        print("\nHomework 8 Menu")
        print("1 - Get p distance matrix")
        print("2 - Exit")
        choice = input("Select an option: ").strip()

        if choice == "1":
            data = read_matrix_from_keyboard()
            if data is None:
                continue
            try:
                matrix = get_p_distance_matrix(data)
            except ValueError as e:
                print(f"Error: {e}")
                continue
            print("\nResulting p-distance matrix:")
            display_matrix(matrix)

        elif choice == "2":
            print("Goodbye.")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()