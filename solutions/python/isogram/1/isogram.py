def is_isogram(phrase):
    phrase = phrase.replace("-", "").replace(" ", "").upper()
    for ch in phrase:
        if phrase.count(ch) > 1:
            return False
    return True