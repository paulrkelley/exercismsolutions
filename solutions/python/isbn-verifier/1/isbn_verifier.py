def is_valid(isbn):
    #remove white space and dashes
    isbn = isbn.replace("-", "").replace(" ", "")
    #if the length is longer than 10 it is not ISBN-10
    if len(isbn) != 10: 
        return False
    #if the digits before 10 aren't numbers than it is not ISBN-10
    if not isbn[:9].isdigit():
        return False
    #the last one is special it can be 'X' if it is not a number or X it is not ISBN-10
    if not (isbn[-1].isdigit() or isbn[-1] == "X"): 
        return False
    #convert first 9 numbers to list of int
    digits = [int(character) for character in isbn[:9]]
    #append either 10 or the number to the list
    if isbn[-1] == "X": 
        digits.append(10)
    else: 
        digits.append(int(isbn[-1]))
    #calculate the formula sum(d_i * 10-i) for i in range 0 -> 10
    total = sum(digit * weight for digit, weight in zip(digits, range(10, 0, -1)))
    #calculate and return the final result
    return total % 11 == 0
        
    
