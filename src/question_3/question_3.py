def get_most_likely_ancestor_consensus(dna_string1, dna_string2):
    """
    Returns all 1-based starting positions where dna_string2 occurs in dna_string1.
    Returned as multiple Python values (tuple), e.g. (2, 4, 10)
    """
    s = dna_string1
    t = dna_string2
    positions = []

    start = 0
    while True:
        idx = s.find(t, start)
        if idx == -1:
            break
        positions.append(idx + 1)     # 1-based position
        start = idx + 1               # +1 allows overlaps

    return tuple(positions)


def main():
    while True:
        dna1 = input("Enter DNA string (9-16 chars): ").strip()
        while not (9 <= len(dna1) <= 16):
            dna1 = input("Invalid. Enter DNA string (9-16 chars): ").strip()

        dna2 = input("Enter DNA substring (exactly 4 chars): ").strip()
        while len(dna2) != 4:
            dna2 = input("Invalid. Enter DNA substring (exactly 4 chars): ").strip()

        result = get_most_likely_ancestor_consensus(dna1, dna2)
        if result:
            print(*result)   # prints like: 2 4 10
        else:
            print("No matches found.")

        choice = input("\nPress Enter to run again, or type Q to quit: ").strip().lower()
        if choice == "q":
            break


if __name__ == "__main__":
    main()
