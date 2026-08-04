def rebase(input_base, digits, output_base):
    #the formula can be understood sum(digits[i]*input_base^(len(digits)-1)) for i in range 0 -> len digits for converting to base 10
    
    #in the instructions we are told to give value errors this means we will have to test input
    #looking at the tests it appears that our inputs are input_base(int), digits(list), output_base(int)

    #input tests
    if input_base < 2: raise ValueError('input base must be >= 2')
    if output_base < 2: raise ValueError('output base must be >= 2')
    if any(digit < 0 or digit >= input_base for digit in digits): raise ValueError("all digits must satisfy 0 <= d < input base")

    #math
    output_digits = [0]
    for digit in digits:
        carry = digit
        for index in range(len(output_digits) - 1, -1, -1):
            value = output_digits[index] * input_base + carry
            output_digits[index] = value % output_base
            carry = value // output_base
        while carry > 0:
            output_digits.insert(0, carry % output_base)
            carry //= output_base
    while len(output_digits) > 1 and output_digits[0] == 0:
        output_digits.pop(0)
    return output_digits