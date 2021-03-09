
import re
from time import sleep
from random import randint
from worldgen import generation_dict as bgen
from worldvar import world_variables as wv
from syscommands.processes import random_event_list as wrel


def slow_print(printing_text):
    for i in printing_text.split():
        sleep(0.05)
        print(i, end=' ')
    print()


def confirm_action():
    ask_for_input = False
    while ask_for_input is False:
        slow_print("Please type Y or N.")
        confirmation = input("Input: ")
        if confirmation.lower() == "y" or confirmation.lower() == "n":
            ask_for_input = True
    if confirmation.lower() == "y":
        return True
    elif confirmation.lower() == "n":
        return False


def show_game_commands():
    show_equipment_list()
    show_journal_list()
    print()


def show_equipment_list():
    if len(wv.inventory) == 1:
        print("INVENTORY:", end=" ")
        print(wv.inventory[0].name)
    if len(wv.inventory) > 1:
        print("Inventory:", end=" ")
        for i in wv.inventory[:-1]:
            print(i.name, end=", ")
        print(wv.inventory[-1].name)


def show_journal_list():
    if len(wv.journal) == 1:
        print("ACTIVE TASKS:", end=" ")
        print(wv.journal[0].name)
    if len(wv.journal) > 1:
        print("Inventory:", end=" ")
        for i in wv.journal[:-1]:
            print(i.name, end=", ")
        print(wv.journal[-1].name)


def call_random_event():
    if wv.outdoor is True:
        is_random = randint(1, 4)
        if is_random == 4:
            is_random = randint(0, 9)
            print(wrel.walking_events_outdoor[is_random][0])
            random_event_identifier = wrel.walking_events_outdoor[is_random][1]
            if random_event_identifier is not None and random_event_identifier not in wrel.completed_events:
                getattr(wrel, "rel_script_" + str(random_event_identifier))
            if len(wrel.walking_events_outdoor) > 10:
                wrel.walking_events_outdoor.pop(is_random)
    else:
        is_random = randint(1, 5)
        if is_random == 3:
            is_random = randint(0,9)
            print(wrel.walking_events_indoor[is_random][0])
            random_event_identifier = wrel.walking_events_indoor[is_random][1]
            if random_event_identifier is not None and random_event_identifier not in wrel.completed_events:
                getattr(wrel, "rel_script_" + str(random_event_identifier))


def describe_location(pos_x, pos_y, direction):
    # check descriptions of objects immediately N/E/S/W

    if direction == "north":
        dict_key = str(pos_x-1) + ", " + str(pos_y)
        try:
            print("To the north there is", bgen.world_gen_dict.get(dict_key)[2])
        except TypeError:
            pass
        direction = "west"
    if direction == "west":
        dict_key = str(pos_x) + ", " + str(pos_y-1)
        try:
            print("To the west there is", bgen.world_gen_dict.get(dict_key)[2])
        except TypeError:
            pass
        direction = "south"
    if direction == "south":
        dict_key = str(pos_x+1) + ", " + str(pos_y)
        try:
            print("To the south there is", bgen.world_gen_dict.get(dict_key)[2])
        except TypeError:
            pass
        direction = "east"
    if direction == "east":
        dict_key = str(pos_x) + ", " + str(pos_y+1)
        try:
            print("To the east there is", bgen.world_gen_dict.get(dict_key)[2])
        except TypeError:
            pass
    print()

# --------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------
# KEEPING RANDOMISED DIALOGUE TABLES BELOW THIS POINT, OUTSIDE OF SCOPE
# ----------------------------------------------------------------------------
# ------------------------------------------------------------


def word_replacer(string_given, replace_this, replace_with):
    # This func exists to clunkily shoehorn in print.format functionality with my slot_print function.
    string_split = string_given.split()
    for i in string_split:
        if string_split[i] == replace_this:
            string_split[i] = replace_with
    return " ".join(string_split)


"""def randomise_dialogue(table_id):
    return table_id[randint(0,5)]"""


attack_the_banshee = ["You attack with your weapon",
                         "",
                         "",
                         "",
                         "",
                         ""]