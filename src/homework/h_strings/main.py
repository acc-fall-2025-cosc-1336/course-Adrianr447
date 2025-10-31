# --- allow running this file directly (python src/homework/h_strings/main.py) ---
import os, sys
if __package__ is None or __package__ == "":
	repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
	if repo_root not in sys.path:
		sys.path.insert(0, repo_root)

from src.homework.h_strings.value_return import get_hamming_distance, get_dna_complement


def menu():
	print("\n1-Hamming Distance")
	print("2-Dna Complement")
	print("3-Exit")


def do_hamming():
	# Hamming distance needs TWO equal-length strings
	dna1 = input("Enter first DNA string: ").strip()
	dna2 = input("Enter second DNA string (same length): ").strip()
	try:
		result = get_hamming_distance(dna1, dna2)
		print("Hamming distance:", result)
	except ValueError as e:
		print("Error:", e)


def do_complement():
	dna = input("Enter DNA string: ").strip()
	try:
		result = get_dna_complement(dna)
		print("Reverse complement:", result)
	except ValueError as e:
		print("Error:", e)


def main():
	while True:
		menu()
		choice = input("Choose an option: ").strip()
		if choice == "1":
			do_hamming()
		elif choice == "2":
			do_complement()
		elif choice == "3":
			print("Goodbye.")
			break
		else:
			print("Invalid option. Please choose 1, 2, or 3.")


if __name__ == "__main__":
	main()