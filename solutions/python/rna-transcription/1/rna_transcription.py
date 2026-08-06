def to_rna(dna_strand):
    #G -> C | C -> G | T -> A  | A -> U
    new_string = ""
    for ch in dna_strand:
        if ch == "G":
            new_string += "C"
        if ch == "C":
            new_string += "G"
        if ch == "T":
            new_string += "A"
        if ch == "A":
            new_string += "U"
    return new_string