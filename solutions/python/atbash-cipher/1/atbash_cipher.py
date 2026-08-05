letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "1234567890"

def encode(plain_text):
    new_string = ""
    for letter in plain_text:
        if letter.upper() in letters:
            new_string += get_pair(letter.lower())
        if letter in numbers:
            new_string += letter
    
    groups = [new_string[index:index + 5] for index in range(0, len(new_string), 5)]
    return " ".join(groups)

def decode(ciphered_text):
    new_string = ""
    for letter in ciphered_text:
        if letter.upper() in letters:
            new_string += get_pair(letter.lower())
        if letter in numbers:
            new_string += letter
    return new_string
    
def get_pair(letter):
    pairs = {"a":"z","b":"y","c":"x","d":"w","e":"v","f":"u","g":"t","h":"s","i":"r","j":"q","k":"p","l":"o","m":"n","n":"m","o":"l","p":"k","q":"j","r":"i","s":"h","t":"g","u":"f","v":"e","w":"d","x":"c","y":"b","z":"a"}
    return pairs[letter]