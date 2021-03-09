
from colorama import Fore, Style
from syscommands import text_commands as txt
from syscommands.processes import object_and_npc_interactions as interaction
from worldvar import world_variables as wv
from worldvar.catalogues import npc_dialogue, object_descriptions as desc, player_inventory as inv, player_journal as quest
from random import randint
import game_state
import re

# Note: It probably would have been worth reformatting this all as some kind of database

ds11_list = []

# --------------------------------------------
# MASTER LIST FOR DIALOGUE CALLS BELOW
# ----------------------


# Master list to redirect a callID to the correct function
def master_script_list_dialogue(id_code):
    if id_code == "Dialogue_CallID_000":    (d_script000())
    elif re.search(r"001$", id_code):  (d_script001())
    elif re.search(r"002$", id_code):  (d_script002())
    elif re.search(r"003$", id_code):  (d_script003())
    elif re.search(r"004$", id_code):  (d_script004())
    elif re.search(r"005$", id_code):  (d_script005())
    elif re.search(r"006$", id_code):  (d_script006())
    elif re.search(r"007.$", id_code): (d_script007(id_code[:-4]))
    elif re.search(r"008.$", id_code): (d_script008(id_code[:-4]))
    elif re.search(r"009.$", id_code): (d_script009(id_code[:-4]))
    elif id_code == "Dialogue_CallID_Cow":    (d_script_cow())
    elif re.search(r"010.$", id_code): (d_script010(id_code[:-4]))
    elif re.search(r"011.$", id_code): (d_script011(id_code[:-4]))
    elif re.search(r"012$", id_code):  (d_script012())
    elif re.search(r"013$", id_code):  (d_script013())
    elif re.search(r"014$", id_code):  (d_script014())


# Test function call
def d_script000():
    print("Hey you hit the dialogue_test function!")


# Dialogue_CallID_001 - knowledge of the smith/carpenter's wife affair from the carpenter's wife
def d_script001():
    if wv.switch_CWife_Smith is False:
        wv.village_affair_knowledge += 1
    if wv.village_affair_knowledge > 1:
        wv.switch_affair_rumours = True
    if wv.player_journal.village_affair not in wv.journal:
        wv.journal.append(wv.player_journal.village_affair)
    wv.switch_CWife_Smith = True


# Dialogue_CallID_002 - carpenter has a slip of the tongue
def d_script002():
    wv.switch_Carp_Leaving, wv.switch_not_Carp_Leaving = False, True
    d_script002_003_004_catch("carp")


def d_script002_003_004_catch(call_sign):
    if call_sign not in wv.leave_village_list:
        wv.leave_village_list.append(call_sign)
        wv.leave_the_village += 1
    if wv.player_journal.cannot_leave not in wv.journal:
        wv.journal.append(wv.player_journal.cannot_leave)
    if wv.leave_the_village > 1:
        wv.switch_leave_the_village = True


# Dialogue_CallID_003 - random villager is confused
def d_script003():
    wv.switch_Villager_Leaving, wv.switch_not_Villager_Leaving = False, True
    d_script002_003_004_catch("villager")


# Dialogue_CallID_004 - fisherman forgets what he's talking about
def d_script004():
    wv.switch_Fisherman_Leaving, wv.switch_not_Fisherman_Leaving = False, True
    d_script002_003_004_catch("fisherman")


# Dialogue_CallID_005 - blacksmith opens up
def d_script005():
    wv.switch_Smith_Friendly = True


# Dialogue_CallID_006 - blacksmith lets something slip
def d_script006():
    if wv.switch_Smith_CWife is False:
        wv.village_affair_knowledge += 1
    if wv.village_affair_knowledge > 1:
        wv.switch_affair_rumours = True
    if wv.player_journal.village_affair not in wv.journal:
        wv.journal.append(wv.player_journal.village_affair)
    wv.switch_Smith_CWife = True


# Dialogue_CallID_007 - affair knowledge builds up
def d_script007(call_sign):
    if call_sign not in wv.call007_list:
        wv.village_affair_knowledge += 1
        wv.call007_list.append(call_sign)
    if wv.village_affair_knowledge > 3 and wv.player_journal.village_affair.state < 2:
        wv.village_affair_public = True
        wv.player_journal.village_affair.state = 2
        wv.player_journal.village_affair.desc = \
            "The carpenter's wife and the blacksmith are having an affair."
        for i in npc_dialogue.woman6:
            if i[0] == "SMITH":
                npc_dialogue.woman6.remove(i)


# Dialogue_CallID_008 - people are hearing things
def d_script008(call_sign):
    if call_sign not in wv.call008_list:
        wv.village_noise += 1
        wv.call008_list.append(call_sign)
        quest_strange_noise()


# Dialogue_CallID_009 - people chatting about children
def d_script009(call_sign):
    if call_sign not in wv.call009_list:
        wv.children_mentioned =+ 1
        wv.call009_list.append(call_sign)
        quest_missing_children()


# Easter egg for if player talks to cow a lot
def d_script_cow():
    cow_response = [
        "\"WHY ARE YOU TALKING TO THIS COW SO MUCH!?\"",
        "\"PLEASE STOP TALKING TO THE COW.\"",
        "\"IT PAINS ME THAT YOU'RE SPENDING SO MUCH TIME DOING THIS.\"",
        "\"WHAT INTERESTS YOU SO MUCH ABOUT THE COW?\"",
        "\"THERE IS NO POINT TO TALKING TO THIS COW.\"",
    ]
    wv.secret_cow_level += 1
    if wv.secret_cow_level > 10:

        random_response = str(cow_response[randint(0, len(cow_response)-1)])
        print("\n . \n .. \n ...")
        print(Fore.GREEN + "\n [Fourth Wall Opens]")
        print(Fore.BLUE + "\n Developer: %s" % random_response)
        print(Fore.GREEN + "\n[Fourth Wall Closes]")
        print(Style.RESET_ALL)


# Dialogue_CallID_010 - people trying to leave the village
def d_script010(call_sign):
  # added type conversion to catch TypeError I can't track down in 2021 test
    if list(call_sign) not in wv.leave_the_village:
        wv.leave_the_village =+ 1
        wv.leave_the_village.append(call_sign)
        quest_leaving_the_village()


# Dialogue_CallID_011 - village elders know more
def d_script011(call_sign):
    if call_sign not in ds11_list:
        wv.ds11_list.append(call_sign)
        wv.switch_elders = True
        if wv.player_journal.elders not in wv.journal:
            wv.journal.append(wv.player_journal.elders)


# Dialogue_CallID_012 - the basket weaver has books
def d_script012():
    wv.switch_basket_weaver_books = True


# Dialogue_CallID_013 - priest having memory problems
def d_script013():
    wv.switch_priest_memory_problems = True


# Dialogue_CallID_014 - the priest gives permission to go to the back room
def d_script014():
    wv.switch_back_room_permission_church = True

# ------------------------------------------
# FUNCTIONS FOR PROCESSING QUESTS
# ------------------------------------------


# update function for the strange noise quest, one of the investigation triggers
def quest_strange_noise():
    if wv.player_journal.peculiar_noise not in wv.journal:
        wv.journal.append(wv.player_journal.peculiar_noise)
    # If multiple sources of noise complaints, progress the quest.
    if wv.village_noise > 2 and wv.player_journal.peculiar_noise.state < 2:
        wv.switch_village_noise = True
        wv.player_journal.peculiar_noise.state = 2
        wv.player_journal.peculiar_noise.desc =\
            "Various villagers have complained of strange noises. I still can't hear anything."
    # If many sources of noise complaints, finish the quest.
    if wv.village_noise > 4 and wv.player_journal.peculiar_noise.state < 3:
        wv.switch_village_cacophony = True
        wv.player_journal.peculiar_noise.state = 3
        wv.player_journal.peculiar_noise.desc =\
            "There's definitely a strange noise in the village, but I can't hear it. I should ask the Alderman."
        wv.player_journal.peculiar_noise.completion = True
    if wv.player_journal.peculiar_noise.state == 1 and wv.switch_heard_noise is True:
        wv.player_journal.peculiar_noise.desc =\
            "There have been a couple of strange noises in the village."
    elif wv.player_journal.peculiar_noise.state == 2 and wv.switch_heard_noise is True:
        wv.player_journal.peculiar_noise.desc =\
            "Various villagers have complained of strange noises. I've heard the same'."
    elif wv.player_journal.peculiar_noise.state == 3 and wv.switch_heard_noise is True:
        wv.player_journal.peculiar_noise.desc =\
            "Strange noises are everywhere in the village. I should ask the Alderman about them."


# update function for the strange noise quest, one of the investigation triggers
def quest_missing_children():
    if wv.player_journal.missing_children not in wv.journal:
        wv.journal.append(wv.player_journal.missing_children)
    # If multiple people mention lack of children then option to chat to everyone opens up.
    if wv.children_mentioned > 2 and wv.player_journal.missing_children.state < 2:
        wv.switch_children_missing = True
        wv.player_journal.missing_children.state = 2
        wv.player_journal.missing_children.desc =\
            "Multiple people have reported that the village children are missing."
    # If enough people mention it, final option pops up.
    if wv.children_mentioned > 4 and wv.player_journal.missing_children.state < 3:
        wv.switch_children_gone = True
        wv.player_journal.missing_children.state = 3
        wv.player_journal.missing_children.desc =\
            "Where have all the children gone? Nobody seems to know."
    if wv.children_mentioned > 4 and wv.switch_children_seen and wv.player_journal.missing_children.state < 4:
        wv.switch_children_gone = True
        wv.player_journal.missing_children.state = 4
        wv.player_journal.missing_children.desc =\
            "Where have all the children gone? I'm sure I've seen some, but where?"


def quest_leaving_the_village():
    if wv.player_journal.cannot_leave not in wv.journal:
        wv.journal.append(wv.player_journal.cannot_leave)
    if wv.leave_the_village > 3:
        wv.switch_villager_rut = True
        wv.player_journal.cannot_leave.state = 2
        wv.player_journal.cannot_leave.desc =\
            "Multiple villagers confessed to being compelled to stay in the village. I should alert the alderman."


# FUNCTION CALLS ABOVE THESE LINES DEAL WITH NPC CONVERSATIONS
"""
---------------------------------------------------------------------------------------------------
"""
# FUNCTION CALLS BELOW THESE LINES DEAL WITH BUILDINGS


# Call_SeenBlacksmithBlade
def i_script000():
    desc.house1_forge.update = None
    desc.house1_blade.state = 1
    desc.house1_entries.append(desc.house1_blade)
    wv.switch_BladeSpotted = True


# Call_TakeBlacksmithBlade
def i_script001():
    txt.slow_print("Would you like to take the blade?")
    if txt.confirm_action() is True:
        if desc.house1_blacksmith.state > 0 and wv.switch_village_affair_public is False:
            txt.slow_print("The blacksmith stops you from taking the blade.")
            txt.slow_print("\"That's not finished, and its already paid for.\"")
            print()
        elif desc.house1_blacksmith.state > 0 and wv.switch_village_affair_public is True:
            txt.slow_print("The blacksmith begrudgingly lets you take the blade")
            print()
            i_script001_execute()
        else:
            i_script001_execute()


def i_script001_execute():
    desc.house1_forge.desc("A smith's forge, with a smelter and anvil.")
    desc.house1_blade.state = 0
    desc.house1_blade.update = None
    desc.house1_entries.remove(desc.house1_blade)
    wv.inventory.append(inv.blacksmith_blade)
    print("\nYou add the unfinished blade to your inventory.\n")


def i_script002():
    print("Do you want to take the fishing pole?")
    if txt.confirm_action() is True:
        if desc.house2_fisherman.state > 0:
            i_script002_execute()
        else:
            print("The fisherman stops you and asks \"what are you doing?\".")
            print("Ask if you can take the fishing pole?")
            if txt.confirm_action() is True:
                print("He looks at you strangely. \"I'm not sure why you'd want it, it's broken, but okay.\".")
                i_script002_execute()


def i_script002_execute():
    desc.house2_fishing_pole.state = 0
    desc.house2_entries.remove(desc.house2_fishing_pole)
    wv.inventory.append(inv.broken_fishing_pole)
    print("\nYou add a broken fishing pole to your inventory.\n")


def i_script003():
    if wv.switch_basket_weaver_books is True:
        print("Do you want to take the old diary?")
        if txt.confirm_action() is True:
            desc.house3_books.state = 0
            desc.house3_entries.remove(desc.house3_books)
            wv.inventory.append(inv.old_diary)
            wv.switch_question_priest = True
            if wv.player_journal.elders not in wv.journal:
                wv.journal.append(wv.player_journal.elders)
            if wv.player_journal.elders.state <= 2:
                wv.player_journal.elders.state = 3
                wv.player_journal.elders.desc =\
                    "The basket weaver's journal mentions that the priest might know more."


# Dialogue_CallID_009 - people chatting about children
def i_script004():
    print("Clearly this is a child's bed, but you've not seen any children about here.")
    if "i_script4" not in wv.call009_list:
        wv.children_mentioned =+ 1
        wv.call009_list.append("i_script4")
        quest_missing_children()


def i_script005():
    if desc.house6_carpenter.state == 0:
        print("Do you want to take the axe?")
        if txt.confirm_action() is True:
            i_script005_execute()
            txt.slow_print("You add the axe to your inventory.")
    else:
        print("Do you want to try to steal the axe?")
        if txt.confirm_action() is True:
            rand_1_in_3 = randint(1,3)
            if rand_1_in_3 == 3:
                # success, you get the axe!
                i_script005_execute()
                txt.slow_print("You slyly take the axe, somehow doing so without being noticed.")
            else:
                # failure, and angry carpenter
                txt.slow_print("The carpenter notices what you're doing.")
                print("Carpenter: \"Oi!\"")
                txt.slow_print("You try to protest your innocence but fail.")
                txt.slow_print("The carpenter kicks you out of his home.")
                txt.slow_print("You are now outside of the building.")
                game_state.game_input()
                wv.switch_angry_carpenter = True


def i_script005_execute():
    desc.house6_axe.state = 0
    desc.house6_entries.remove(desc.house6_axe)
    wv.inventory.append(inv.carpenter_axe)


def i_script006(farmer_tool):
    if desc.house5_farmer.state == 0:
        print("Do you want to take the %s?" % farmer_tool.lower())
        if txt.confirm_action() is True:
            i_script006_execute(farmer_tool)
            txt.slow_print("You add the %s to your inventory." % farmer_tool.lower())
    else:
        print("Do you want to try to steal the %s?" % farmer_tool.lower())
        if txt.confirm_action() is True:
            rand_1_in_3 = randint(1, 3)
            if rand_1_in_3 == 3:
                # success, you get the item!
                i_script006_execute(farmer_tool)
                txt.slow_print("You successfully steal the %s without being noticed." % farmer_tool.lower())
            else:
                # failure, and angry farmer
                txt.slow_print("The farmer notices what you're doing.")
                print("Farmer: \"What on god's green-\"")
                txt.slow_print("You try to apologise but he isn't listening.")
                txt.slow_print("The farmer kicks you out of his home.")
                txt.slow_print("You are now outside of the building.")
                game_state.game_input()
                wv.switch_angry_farmer = True


def i_script006_execute(farmer_tool):
    if farmer_tool == "Shovel":
        desc.house5_shovel.state = 0
        desc.house5_entries.remove(desc.house5_shovel)
        wv.inventory.append(inv.farmer_shovel)
    elif farmer_tool == "Hoe":
        desc.house5_hoe.state = 0
        desc.house5_entries.remove(desc.house5_hoe)
        wv.inventory.append(inv.farmer_hoe)


def i_script007():
    if desc.church_pews.state < 2:
        txt.slow_print("As you explore the pews you notice some are quite damaged.")
        txt.slow_print("A broken wooden sliver lays between two pews, larger than other shards.")
        txt.slow_print("In a pinch it might make a passable weapon.")
        txt.slow_print("Do you wish to take the wooden stake?")
        if txt.confirm_action() is True:
            desc.church_pews.state = 2
            desc.church_pews.desc = "Long wooden pews run in parallel along the church."
            txt.slow_print("You add the wooden stake to your inventory.")
            wv.inventory.append(inv.church_stake)


def i_script008():
    if desc.church_windows.state < 2:
        txt.slow_print("At the foot of one of the far windows you notice a great deal more broken glass.")
        txt.slow_print("One of the broken glass shards is larger than the others")
        txt.slow_print("In a pinch it might make a passable weapon.")
        txt.slow_print("Do you wish to take the glass shard?")
        if txt.confirm_action() is True:
            desc.church_windows.state = 2
            desc.church_windows.desc = "Instead of windows there are gaps in the stone walls."
            txt.slow_print("You add the glass shard to your inventory.")
            wv.inventory.append(inv.church_glass)


def i_script009(direction):
    if desc.church_priest.state > 0:
        if wv.switch_back_room_permission_church is True:
            i_script009_execute(direction)
        else:
            print("Priest:", end=" ")
            txt.slow_print("\"I'm afraid that room is private.\"")
    else:
        i_script009_execute(direction)


def i_script009_execute(direction):
    # script for travelling between rooms in church
    txt.slow_print("A heavy wooden door stands ahead of you.")
    if desc.church_priest.state == 0 or wv.switch_back_room_permission_church is True:
        txt.slow_print("Do you wish to " + direction + "?")
        if txt.confirm_action() is True:
            if direction == "go inside":
                if desc.church_priest.state > 0:
                    txt.slow_print("The priest accompanies you as you walk.")
                else:
                    i_script009_check_backroom()
                interaction.enter_home("church_b")
            elif direction == "leave the room":
                if desc.church_priest.state > 0:
                    txt.slow_print("The priest accompanies you as you walk.")
                else:
                    i_script009_check_backroom()
                interaction.enter_home("church")
    else:
        txt.slow_print("It is locked.")


def i_script009_check_backroom():
    # Need to make sure there aren't two corpses in the church
    if desc.church_priest.state == 0:
        if desc.church_priest in desc.church_entries and desc.church_priest in desc.church_b_entries:
            rand_1_in_2 = randint(1,2)
            if rand_1_in_2 == 1:
                desc.church_b_entries.remove(desc.church_priest)
            elif rand_1_in_2 == 2:
                desc.church_entries.remove(desc.church_priest)


def i_script010():
    txt.slow_print("You pour over the books and tomes, looking for something of relevance.")
    if desc.church_priest.state > 0:
        txt.slow_print("The priest helps you as best as he can.")
    if wv.banshee_name == "banshee":
        txt.slow_print("You have already read these books.\nRead again?")
        if txt.confirm_action() is True:
            i_script010_execute(wv.switch_back_room_permission_church, wv.switch_children_gone, wv.switch_village_cacophony)
    else:
        i_script010_execute(wv.switch_back_room_permission_church, wv.switch_children_gone, wv.switch_village_cacophony)


def i_script010_execute(final_check1, final_check2, final_check3):
    if final_check1 is True or final_check2 is True or final_check3 is True:
        # Player has done enough to reach the end of the game
        txt.slow_print("You find the unsettling tale of a nearby village.")
        txt.slow_print("A creature of some kind, a 'false banshee', descended upon the village.")
        txt.slow_print("It screamed and sung a bewitching song that tortured the villagers.")
        txt.slow_print("Whilst it sang they were unable to remember the simplest of things.")
        txt.slow_print("Whilst it sang they were unable or unwilling to leave their village.")
        txt.slow_print("It sapped their minds and tore through their flesh, hunting the smallest first.")
        txt.slow_print("Only when it stopped to feed did its beguiling song cease.")
        if wv.banshee_name == "banshee":
            txt.slow_print("You notice something you missed the first time.")
            txt.slow_print("A short passage makes mention of a false banshee's vulnerability to salt...")
        else:
            txt.slow_print("\n.\n..\n...\nYou hear... nothing. As though a sound you weren't aware of just stopped.")
        wv.banshee_name = "banshee"
        wv.switch_final_encounter = True
    else:
        txt.slow_print("You do not find anything helpful.")
        txt.slow_print("When you have more of an idea of what to look for it might be helpful to try again.")

# ----------------------
# MASTER LIST FOR BUILDING ITEMS BELOW
# --------------------------------------------


# Master list to redirect a callID to the correct function
def master_script_list_item(id_code):

    if id_code == "SeenBlacksmithBlade": (i_script000())
    elif id_code == "TakeBlacksmithBlade": (i_script001())
    elif id_code == "BrokenFishingPole": (i_script002())
    elif id_code == "TakeOldDiary": (i_script003())
    elif id_code == "PileOfHay": (i_script004())
    elif id_code == "TakeCarpenterAxe": (i_script005())
    elif id_code == "TakeFarmerShovel": (i_script006("Shovel"))
    elif id_code == "TakeFarmerHoe": (i_script006("Hoe"))
    elif id_code == "BreakPews": (i_script007())
    elif id_code == "CheckWindows": (i_script008())
    elif id_code == "church_door_to_private": (i_script009("go inside"))
    elif id_code == "church_door_to_main": (i_script009("leave the room"))
    elif id_code == "Priest_Books": (i_script010())

