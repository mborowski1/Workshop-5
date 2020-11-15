def dice(dice_code):
    '''
    Dice simulator.
    :param dice_code: code representing dice roll information:
    xDy+z, where x - how many times do you /n want to roll the die, y - number of face of die, z - modifier.
    :return: Die/dice rolling result.
    '''
    import random

    list_dice_code = list(dice_code)
    try:
        index_D = list_dice_code.index("D")
    except ValueError:
        print("Enter information in accordance with the following formula: xDy+z, where x - how many times do you /n want to roll the die, y - number of face of die, z - modifier.")
        return None

    aux_list_2 = []

    x = 1
    y = 0
    z = 0

    if index_D > 0:
        try:
            x = int("".join(list_dice_code[:index_D]))
        except ValueError:
            print("Enter information in accordance with the following formula: xDy+z, where x - how many times do you /n want to roll the die, y - number of face of die, z - modifier.")
            return None


    if "+" in list_dice_code:
        aux_y_1 = "".join(list_dice_code[index_D+1:])
        aux_y_2 = "".join(list_dice_code[list_dice_code.index("+"):])
        if aux_y_2 in aux_y_1:
            try:
                y = int(aux_y_1.replace(aux_y_2, ""))
            except ValueError:
                print("Enter information in accordance with the following formula: xDy+z, where x - how many times do you /n want to roll the die, y - number of face of die, z - modifier.")
                return None
        try:
            z = int("".join(list_dice_code[list_dice_code.index("+"):]))
        except ValueError:
            print("Enter information in accordance with the following formula: xDy+z, where x - how many times do you /n want to roll the die, y - number of face of die, z - modifier.")
            return None
    elif "-" in list_dice_code:
        aux_y_1 = "".join(list_dice_code[index_D+1:])
        aux_y_2 = "".join(list_dice_code[list_dice_code.index("-"):])
        if aux_y_2 in aux_y_1:
            y = int(aux_y_1.replace(aux_y_2, ""))
        try:
            z = int("".join(list_dice_code[list_dice_code.index("-"):]))
        except ValueError:
            print("Enter information in accordance with the following formula: xDy+z, where x - how many times do you /n want to roll the die, y - number of face of die, z - modifier.")
            return None
    else:
        try:
            y = int("".join(list_dice_code[(index_D + 1):]))
        except ValueError:
            print("Enter information in accordance with the following formula: xDy+z, where x - how many times do you /n want to roll the die, y - number of face of die, z - modifier.")
            return None






    if y == 3:

        while x >= 1:
            aux_list_2.append(random.randint(1, 3))
            x -= 1

    elif y == 4:

        while x >= 1:
            aux_list_2.append(random.randint(1, 4))
            x -= 1

    elif y == 6:

        while x >= 1:
            aux_list_2.append(random.randint(1, 6))
            x -= 1


    elif y == 8:

        while x >= 1:
            aux_list_2.append(random.randint(1, 8))
            x -= 1

    elif y == 10:

        while x >= 1:
            aux_list_2.append(random.randint(1, 10))
            x -= 1


    elif y == 12:

        while x >= 1:
            aux_list_2.append(random.randint(1, 12))
            x -= 1


    elif y == 20:

        while x >= 1:
            aux_list_2.append(random.randint(1, 20))
            x -= 1


    elif y == 100:

        while x >= 1:
            aux_list_2.append(random.randint(1, 100))
            x -= 1

    else:
        print("You cannot select die with this amount of faces.")
        return None


    result = sum(aux_list_2) + z

    return result



print(dice("5D10+2"))



































