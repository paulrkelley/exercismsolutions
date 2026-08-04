def score(x, y):
    """
    This function takes in a set of coordinates and returns the score for the arrow shot

    Input:
    x (int): x coordinate
    y (int): y coordinate

    Output:
    Score for shot (int)
    """
    # A point is in a circle if (x-c_x)^2 + (y-c_y)^2 <= r^2 where c is the center of the circle
    radius_circle_one = 1
    radius_circle_two = 5
    radius_circle_three = 10
    
    is_inside_circle_one = True if (x)**2 + (y)**2 <= radius_circle_one ** 2 else False
    is_inside_circle_two = True if (x)**2 + (y)**2 <= radius_circle_two ** 2  else False
    is_inside_circle_three = True if (x)**2 + (y)**2 <= radius_circle_three ** 2 else False

    if not is_inside_circle_three and not is_inside_circle_two and not is_inside_circle_one:
        return 0
    if is_inside_circle_three and not (is_inside_circle_two or is_inside_circle_one):
        return 1
    if is_inside_circle_two and not is_inside_circle_one:
        return 5
    if is_inside_circle_one:
        return 10