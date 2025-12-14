from src.homework.i_dictionaries_sets.dictionary import (
	inventory_dictionary,
	add_inventory,
	remove_inventory_widget,
)


def prompt_for_int(prompt):
	while True:
		try:
			return int(input(prompt).strip())
		except ValueError:
			print("Please enter a valid integer.")


def main():
	while True:
		print("\nInventory Menu")
		print("1-Add or Update Item")
		print("2-Delete Item")
		print("3-Exit")
		choice = input("Select an option: ").strip()

		if choice == "1":
			name = input("Enter item name: ").strip()
			qty = prompt_for_int("Enter quantity to add (use negative to subtract): ")
			add_inventory(inventory_dictionary, name, qty)
			print(f"Item '{name}' updated. New quantity: {inventory_dictionary.get(name)}")

		elif choice == "2":
			name = input("Enter item name to delete: ").strip()
			result = remove_inventory_widget(name)
			print(result)

		elif choice == "3":
			print("Goodbye.")
			break

		else:
			print("Invalid choice. Try again.")


if __name__ == "__main__":
	main()
