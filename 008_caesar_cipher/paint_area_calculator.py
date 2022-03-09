def paint_calc(height, width, cover):
    '''
    Calculates the required amount of paint to paint a wall.
    '''
    import math
    num_cans = math.ceil((height * width) / cover)
    print(f"You'll need {num_cans} cans of paint.")


test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
