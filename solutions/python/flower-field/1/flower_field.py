def annotate(garden):
    if not garden:
        return []
    # Function body starts here
    new_garden = []
    length_i = len(garden)
    length_j = len(garden[0])
    for row in garden:
        if len(row) != length_j:
            raise ValueError("The board is invalid with current input.")
    #this does up and down
    for i in range(length_i):
        row_builder = ""
        #this does left and right
        for j in range(length_j):
            new_value = 0
            #check diagonals
            if garden[i][j] == " ":
                if i-1 >= 0 and j-1 >= 0:
                    if check(garden, i-1, j-1):
                        new_value += 1
                if i-1 >= 0 and j+1 < length_j:
                    if check(garden, i-1, j+1):
                        new_value += 1
                if i+1 < length_i and j-1 >= 0:
                    if check(garden, i+1, j-1):
                        new_value += 1
                if i+1 < length_i and j+1 < length_j:
                    if check(garden, i+1, j+1):
                        new_value += 1
                if i-1 >= 0:
                    if check(garden, i-1, j):
                        new_value += 1
                if i+1 < length_i:
                    if check(garden, i+1, j):
                        new_value += 1
                if j-1 >= 0:
                    if check(garden, i, j-1):
                        new_value += 1
                if j+1 < length_j:
                    if check(garden, i, j+1):
                        new_value += 1
                
                if new_value == 0:
                    row_builder += " "
                else:
                    row_builder += str(new_value)
            elif garden[i][j] == "*":
                row_builder += "*"
            else:
                raise ValueError("The board is invalid with current input.")
        new_garden.append(row_builder)
    return new_garden

def check(garden, i, j):
    if garden[i][j] == "*":
        return True
    return False