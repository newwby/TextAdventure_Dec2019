import game_state
import re
from random import randint
from time import sleep
from worldvar import world_variables as wv, constants as constant
from worldvar.catalogues import player_journal as journal
from worldgen import generation_dict as bgen
from syscommands.processes import object_and_npc_interactions as interaction
from syscommands import text_commands as txt


def process_special_command(inputted_command):
    # if wv.journal is not None and inputted_command == "j" or "journal":

    # Accessing the player's inventory
    if inputted_command == "quit":
        quit_game()
    # Accessing the player's journal
    elif len(wv.journal) >= 1 and inputted_command in ["j", "journal"]:
        print("\nINFORMATION OF INTEREST:")
        for i in wv.journal:
            if i.completion is False:
                print("\n" + str(i.name).upper() + ": " + i.desc)
            if i.completion is True:
                print("\n" + str(i.name + " (COMPLETE!)").upper() + ": " + i.desc)
    # Accessing the player's inventory
    elif len(wv.inventory) >= 1 and inputted_command in ["i", "inventory"]:
        print("\nITEMS IN YOUR INVENTORY:")
        for i in wv.inventory:
            print("\n" + str(i.name).upper() + ": " + i.desc)
    else:
        print("Incorrect input! Try again.")


def quit_game():
    # non-recursive
    print(), txt.slow_print("Are you sure you want to quit?")
    # SAVE COMMAND HERE WOULD BE NICE, CHOICE TO SAVE OR QUIT WITHOUT SAVING
    if txt.confirm_action() is True:
        print(), txt.slow_print("Thanks for playing! Goodbye!")
        sleep(0.5)
        quit()
    else:
        resume_play()


def input_action(input_command):
    # CHECK FOR MAIN QUEST TRIGGER
    if journal.dead_bodies not in wv.journal and wv.switch_village_death is True:
        print("\nSomething strange is going on. I should talk to the village alderman.\n")
        wv.journal.append(journal.dead_bodies)
        journal.main_quest.state = 2
        journal.main_quest.desc = "I need to speak with the village alderman. He lives at the big house."
    # CHECK FOR JOURNAL/INVENTORY ACTIONS
    if input_command.lower() in constant.special_actions:
        process_special_command(input_command.lower())
        resume_play()
    # DEFAULT ACTION INPUT, CHECK FOR QUIT/MOVEMENT/INCORRECT INPUT
    elif input_command.lower() in constant.move_actions:
        move_action(input_command)
    else:
        if input_command.lower() not in constant.special_actions:
            print("\rIncorrect input! Try again.")
        print()
        resume_play()


def random_smell_string():
    death_smell_table = ["A rotten scent lingers on the air.",
                         "Something smells foul.",
                         "What is that stench?",
                         "You nearly lose your lunch as you take in a deep breath.",
                         "Something nearby doesn't smell very nice.",
                         "The village is pungent with the smell of death.",
                         "How can anyone stand that stink on the air?",
                         "You're not sure what that smell is, but you don't like it."]
    wv.death_stink = 0
    return death_smell_table[randint(0,7)]


def move_action(move_command):
    # HERE WE CHECK WHAT DIRECTION WE ARE MOVING IN AND ASSIGN MOVEMENT VALUES/STRINGS
    # (Make multiple input movement command that processes movement strings?)
    if move_command.lower() == 'n':
        mod_y, mod_x, direction = -1, 0, "north"
    elif move_command.lower() == 'w':
        mod_y, mod_x, direction = 0, -1, "west"
    elif move_command.lower() == 's':
        mod_y, mod_x, direction = 1, 0, "south"
    elif move_command.lower() == 'e':
        mod_y, mod_x, direction = 0, 1, "east"

    # HERE WE PROCESS THE MOVEMENT AND CHECK IF THE MOVEMENT IS VALID
    dict_key = str(wv.pos_y+mod_y) + ", " + str(wv.pos_x+mod_x)

    if bgen.world_gen_dict.get(dict_key) is None:
        print("You travel to the " + direction + ".\n")

        # HERE WE CALL RANDOM WALKING EVENTS AND SMELL EVENTS
        txt.call_random_event()

        if wv.death_counter > 1 and wv.death_stink < 2:
            wv.death_stink += 1
        else:
            print()
            txt.slow_print(random_smell_string())
        print()

        # HERE WE MODIFY PLAYER LOCATION AND REDRAW THE WORLD
        wv.pos_x, wv.pos_y = wv.pos_x+mod_x, wv.pos_y+mod_y
        game_state.game_input()
    else:
        # HERE WE CHECK IF THE MOVEMENT IS INTO A BUILDING, NPC, OR INVALID TILE
        obstacle, domicile_home, non_player_character = bgen.world_gen_dict.get(dict_key)[1], r"^house", r"man[0-9]$"

        if re.match(domicile_home, obstacle) or obstacle == "church":
            txt.slow_print("To your " + direction + " is " + bgen.world_gen_dict.get(dict_key)[2])
            txt.slow_print("Do you wish to go inside?")
            if txt.confirm_action() is True:
                # Angry villagers won't let you into their homes
                if bgen.world_gen_dict.get(dict_key)[1] == "house6" and wv.switch_angry_carpenter is True:
                    txt.slow_print("The angry carpenter prevents you from entering his home.")
                    resume_play()
                elif bgen.world_gen_dict.get(dict_key)[1] == "house5" and wv.switch_angry_farmer is True:
                    txt.slow_print("The angry farmer prevents you from entering his home.")
                    resume_play()
                else:
                    interaction.enter_home(bgen.world_gen_dict.get(dict_key)[1])
            else:
                resume_play()
        elif obstacle == "church steeple":
            print("The church grounds block your way, the steeple looming high.")
            input_action(input("Input: "))

        elif obstacle == "lamppost":
            txt.slow_print("An unlit lamp post sits in your way.")
            txt.slow_print("It's getting dark. The village lamplighter should have been by.\n")
            input_action(input("Input: "))

        elif re.match(r"^corpse", obstacle):
            txt.slow_print("As you approach the corpse you find yourself distracted.")
            txt.slow_print("No matter how many times you try, something inside you steers you away from the body.")
            txt.slow_print("To approach the dead is to forget the dead, long enough to end back where you started.")
            txt.slow_print("The smell of death is overpowering.")
            txt.slow_print("You cannot go that way.")
            wv.switch_village_death = True
            input_action(input("Input: "))

        elif re.search(non_player_character, obstacle):
            txt.slow_print("To your " + direction + " is " + bgen.world_gen_dict.get(dict_key)[2])
            txt.slow_print("Do you wish to start a conversation? (Type Y or N)")
            if txt.confirm_action() is True:
                speaker = interaction.identify_speaker(bgen.world_gen_dict.get(dict_key)[1])
                interaction.begin_conversation(bgen.world_gen_dict.get(dict_key)[1], speaker)
            else:
                resume_play()
        else:
            print("You cannot go that way.")
            input_action(input("Input: "))


def resume_play():
    txt.slow_print("Type N to move North, S to move South, W to move West, or E to move East.")
    txt.slow_print("Move toward buildings/people to interact with them. Type \'Quit\' to exit the game.")
    input_action(input("Input: "))

