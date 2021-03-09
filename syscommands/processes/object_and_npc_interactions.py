
from syscommands import text_commands as txt, game_commands as gcomm
from syscommands.processes import script_calls as call
from worldvar import world_variables as wv, constants as constant
from worldvar.catalogues import object_descriptions as desc, npc_dialogue, key_dictionaries as id_key
import game_state
import re


# THIS FUNCTION IDENTIFIES THE NPC SPEAKING IN CONVERSATIONS
def identify_speaker(conversation_key):
    for i in id_key.convo_key_dict:
        if i == conversation_key:
            return id_key.convo_key_dict[i]


# THIS FUNCTION IS THE PARENT FUNCTION FOR CONVERSATION CONTROL
def begin_conversation(conversation_key, speaker):
    txt.show_game_commands()
    print(), txt.slow_print("What would you like to talk about?")
    print("Conversation topics:", end=" ")
    # Initialise validation list for conversation topics
    convo_validation_list = conversation_topics(conversation_key)
    # Ask player for input on what conversation topic they want to discuss
    conversation_input(input("Input: "), conversation_key, speaker, convo_validation_list)


# THIS FUNCTION RETURNS A LIST TO VALIDATE INPUT AGAINST AND PRINTS VALID TOPICS OF CONVERSATION FOR THE PLAYER
def conversation_topics(conversation_key):
    topic_validation_list = []
    # prints list of conversation topics and populates list of topics to validate input against
    for i in getattr(npc_dialogue, conversation_key):
        # check if the conversation option has a WorldVar prerequisite to be fulfilled, and if so, is it True
        if i[3] is None or getattr(wv, "switch_" + i[3]) is True:
            topic_validation_list.append(i[0])
    # sort conversation, populate list, return validation list
    topic_validation_list.sort()
    for i in topic_validation_list[:-1]:
        print(i, end=", ")
    txt.slow_print(topic_validation_list[-1] + ". ")
    txt.slow_print("Type Q to stop talking.")
    return topic_validation_list


# THIS FUNCTION ASKS PLAYER FOR INPUT AND THEN VALIDATES THAT INPUT
def conversation_input(convo_input, conversation_key, speaker, valid_list):
    # asks player for input
    print()
    # CHECK FOR JOURNAL/INVENTORY ACTIONS
    if convo_input.lower() in constant.special_actions:
        gcomm.process_special_command(convo_input.lower())
    if convo_input.upper() == "Q":
        print("You walk away from the conversation.")
        # If we're outdoors, resume the village map, if we're indoors we should loop back to previous
        if wv.outdoor is True:
            game_state.game_input()
    elif convo_input.upper() in valid_list:
        # loop until we find the conversation option requested by player input
        for i in getattr(npc_dialogue, conversation_key):
            if i[0] == convo_input.upper():
                # print the speaker's response
                print(speaker, end=" ")
                txt.slow_print(i[1])
                print()
                # check if the conversation has any specific script function
                if i[2] is not None:
                    call.master_script_list_dialogue(i[2])
        # once done, resume conversation
        begin_conversation(conversation_key, speaker)
    else:
        # if input is incorrect, resume conversation
        if convo_input.lower() not in constant.special_actions:
            print("\rIncorrect input! Try again.")
        begin_conversation(conversation_key, speaker)


# FUNCTIONS ABOVE THESE LINES DEAL WITH NPC CONVERSATIONS
"""
---------------------------------------------------------------------------------------------------
"""
# FUNCTIONS BELOW THESE LINES DEAL WITH BUILDINGS


# THIS FUNCTION IS THE PARENT FUNCTION FOR BUILDING FLOW
def enter_home(home_key):
    wv.outdoor = False
    print()
    # prints initial entering/description of the room
    txt.slow_print("."), txt.slow_print(".."), txt.slow_print("...")
    txt.slow_print(id_key.building_key_dict.get(home_key)[1]), print()
    txt.call_random_event()
    home_description(home_key)


# THIS FUNCTION DESCRIBES WHAT IS IN THE ROOM AND ALLOWS THE PLAYER TO INTERACT WITH THOSE ITEMS
def home_description(home_key):
    txt.show_game_commands()
    txt.slow_print("You are in the " + id_key.building_key_dict.get(home_key)[0] + ".")
    # describes to the player what is in the room
    room_write_appearance(home_key + "_entries", "appearance")
    # gives the player a list of things to interact with
    entry_validation_list = room_write_appearance(home_key + "_entries", "name")
    print("(Type Q to leave the building.)")
    examination_input(input("Input: "), home_key, entry_validation_list)


# THIS FUNCTION TELLS THE PLAYER WHAT THEY SEE OF INTEREST/CAN INTERACT WITH
def room_write_appearance(populate_entries, requirement):
    # check if list is empty else write preamble
    viewing_list = []
    if len(getattr(desc, populate_entries)) < 1:
        return None
    elif requirement == "appearance":
        print("You see", end=" ")
    elif requirement == "name":
        print(), print(), print("What would you like to examine? \nType:", end=" ")

    # print according to whether element is last element in list or not/the call requirement
    for entry in (getattr(desc, populate_entries)):
        if requirement == "appearance":
            viewing_list.append(entry.appearance)
        elif requirement == "name":
            viewing_list.append(entry.name)
    viewing_list.sort()
    for i in viewing_list[:-1]:
        print (i, end=", ")
    if requirement == "appearance":
        print("and " + viewing_list[-1], end=".")
    elif requirement == "name":
        print("or " + viewing_list[-1], end=". ")
    if requirement == "name":
        return viewing_list


# THIS FUNCTION VALIDATES AND EXECUTES PLAYER INPUT INSIDE ROOMS
def examination_input(examine_input, home_key, validation_list):
    print()
    # CHECK FOR JOURNAL/INVENTORY ACTIONS
    if examine_input.lower() in constant.special_actions:
        gcomm.process_special_command(examine_input.lower())

    # If Q, leave the building
    if examine_input.upper() == "Q":
        print("You leave the building.")
        game_state.game_input()
    # Make sure input is in the validation list
    elif examine_input.upper() in validation_list:
        for i in getattr(desc, home_key + "_entries"):
            if i.name == examine_input.upper():
                txt.slow_print(i.desc)
                print()
                # Execute any script calls attached to the object
                if i.update is not None:
                    execute_script_call(i.update)
                home_description(home_key)
    else:
        if examine_input.lower() not in constant.special_actions:
            print("\rIncorrect input! Try again.")
        print()
        home_description(home_key)


# Pass us over to script calls before returning
def execute_script_call(update_code):
    if re.match(r"^Talk", update_code):
        txt.slow_print("Would you like to start a conversation?")
        if txt.confirm_action() is True:
            begin_conversation(update_code[5:], identify_speaker(update_code[5:]))
    elif re.match(r"^Call", update_code):
        call.master_script_list_item(update_code[5:])
    elif re.match(r"^dead", update_code):
        txt.slow_print("You go to investigate the dead body, only to find yourself distracted by something else.")
        txt.slow_print("As you realise this you try to turn back, only for your mind to become muddled once more.")
        txt.slow_print("Each time you approach the body you fail to spend more than a moment near it.")
        txt.slow_print("Some part of you is forgetting about the dead body, though it lays right in front of you.")
        wv.switch_village_death = True

