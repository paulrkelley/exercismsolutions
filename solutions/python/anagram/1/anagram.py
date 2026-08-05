def find_anagrams(word, candidates):
    anagrams = []
    for candidate in candidates:
        if sorted(word.upper()) == sorted(candidate.upper()):
            if candidate.upper() != word.upper():
                anagrams.append(candidate)
    return anagrams
