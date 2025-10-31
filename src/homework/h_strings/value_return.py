def get_hamming_distance(dna1: str, dna2: str) -> int:
    """
    Return the Hamming distance between two equal-length DNA strings.
    Loops only; no slicing.
    """
    if len(dna1) != len(dna2):
        raise ValueError("DNA strings must be the same length")

    distance = 0
    # compare character by character
    for i in range(len(dna1)):
        if dna1[i] != dna2[i]:
            distance += 1
    return distance


def get_dna_complement(dna: str) -> str:
    """
    Return the reverse complement of a DNA string using loops only.
    Reverse (with a loop), then complement each base (A<->T, C<->G).
    """
    # 1) reverse with a loop (no slicing)
    reversed_dna = ""
    for i in range(len(dna) - 1, -1, -1):
        reversed_dna += dna[i]

    # 2) complement with a loop (if/elif to avoid built-ins)
    complement = ""
    for i in range(len(reversed_dna)):
        ch = reversed_dna[i].upper()
        if ch == "A":
            complement += "T"
        elif ch == "T":
            complement += "A"
        elif ch == "C":
            complement += "G"
        elif ch == "G":
            complement += "C"
        else:
            # If your instructor wants to ignore/raise on bad chars, you can change this.
            raise ValueError("Invalid DNA symbol: " + ch)
    return complement
