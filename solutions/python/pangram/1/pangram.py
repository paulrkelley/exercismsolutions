def is_pangram(sentence):
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    sentence = sentence.upper()
    for letter in letters:
        if letter not in sentence:
            return False
    return True