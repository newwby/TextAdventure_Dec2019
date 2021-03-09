
from worldgen import generation_dict as bgen
from worldvar import constants as constant

# would it be worth redoing this using positioning commands to make it look better?


def draw_immediate(pos_x, pos_y):

    # draw_immediate draws a fixed 5x5 range centered around the player

    draw_range = constant.draw_range
    for i in range(pos_x-draw_range-1, pos_x+draw_range):
        for j in range(pos_y-draw_range-1, pos_y+draw_range):
            draw_space(i+1, j+1, pos_x, pos_y)
        print()
    print()


def draw_space(loc_x, loc_y, pos_x, pos_y):

    # draw_space determines the correct text graphic to draw, and where the player is

    if loc_x == pos_x and loc_y == pos_y:
        print("옷", end=' ')
    else:
        dict_key = str(loc_x) + ", " + str(loc_y)
        try:
            print (decipher_gfx(bgen.world_gen_dict.get(dict_key)[0]), end=' ')
        except TypeError:
            print (decipher_gfx(bgen.world_gen_dict.get(dict_key)), end=' ')


def decipher_gfx(gfx_key):
    # First we check for world boundaries (fences)

    if gfx_key is None:
        return " "
    elif gfx_key == "NW FENCE":
        return "|"
    elif gfx_key == "NE FENCE":
        return "|"
    elif gfx_key == "N FENCE":
        return "_"
    elif gfx_key == "W FENCE" or gfx_key == "E FENCE":
        return "|"
    elif gfx_key == "SW FENCE":
        return "|_"
    elif gfx_key == "S FENCE":
        return "_"
    elif gfx_key == "SE FENCE":
        return "_|"

    # next we check for buildings and outdoor objects

    elif gfx_key == "SMALL HOUSE" or gfx_key == "CHURCH" or gfx_key == "LARGE HOUSE":
        return "█"
    elif gfx_key == "STEEPLE":
        return "┼"
    elif gfx_key == "LAMP":
        return "¡"

    # next we check for characters
    # Which could be rebuilt as objects untied to specific locations, so that they can move
    # (or just adjust dict entries?)

    elif gfx_key == "MAN":
        return "♂"
    elif gfx_key == "WOMAN":
        return "♀"
    elif gfx_key == "CORPSE":
        return "X"
