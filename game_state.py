from syscommands import text_commands as txt, graphic_commands as gfx, game_commands as gcomm
from syscommands.complex_encounters import final_encounter as endgame
from worldvar import world_variables as wv
from time import sleep

def game_input():
    # Initialise the basic game input menu
    if wv.switch_final_encounter is True:
        endgame.final_encounter()
    else:
        sleep(0.5)
        txt.describe_location(wv.pos_y, wv.pos_x, "north")
        gfx.draw_immediate(wv.pos_y, wv.pos_x)
        sleep(0.1)
        wv.outdoor = True
        # txt.slow_print("You are at x%d/y%g" % (wv.pos_x, wv.pos_y))
        txt.show_game_commands()
        txt.slow_print("Type N to move North, S to move South, W to move West, or E to move East.")
        txt.slow_print("Move toward buildings/people to interact with them. Type \'Quit\' to exit the game.")
        sleep(0.2)
        gcomm.input_action(input("Input: "))

