from colorama import Fore, Style
from time import sleep
from random import randint
from worldvar import world_variables as wv
from worldvar.catalogues import player_inventory as inv
from syscommands import text_commands as txt
from syscommands.complex_encounters import encounter_objects as enc_obj

# Note to self: this code (tidied) could serve as the basis for a basic combat system if project is expanded

# Important attributes for combat are player weapon (instance of another class),
# positioning, and encounter score (a measure of how well it is going)
# To easily manage these we use an object here
combat = enc_obj.CombatEncounter("banshee_battle", 0, None, None)

# starts at final encounter intro funcs (1 & 2) then gets into loop of banshee_combat sub-funcs

# ---------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------

# THESE FUNCTIONS CREATE THE MAIN COMBAT LOOP AND HANDLE COMMAND PROCESSING


def banshee_combat():
    # This function will loop until the banshee is dead/gone or you are dead.
    # It is the main function involved in the final encounter.
    while wv.switch_final_encounter is True:
        print_banshee_positioning()         # cleaner to move positioning/text to functions (below)
        print_banshee_command_options()
        txt.slow_print("(Type FIGHT, ITEM, or MOVE!)")
        banshee_combat_command_processing(input("Input: "))
        if combat.player_acted is True:
            combat.player_acted = False
            banshee_action()
        banshee_combat()


def banshee_combat_command_processing(inputted_command):
    if inputted_command.lower() == "fight":
        banshee_combat_command_fight()
    elif inputted_command.lower() == "item":
        banshee_combat_command_item()
    elif inputted_command.lower() == "move":
        banshee_combat_command_move()
    else:
        txt.slow_print("Incorrect input! (Please type FIGHT, ITEM, or MOVE!)")
        sleep(0.2)
        banshee_combat_command_processing(input("Input: "))


def banshee_combat_command_fight():
    # DOES CODE NEED FINISHING HERE?
    if combat.position == "far":
        combat.position = "near"
        print("You charge forward, but the %s has time to react before you!" % wv.banshee_name)
        combat.player_acted = True
        combat.en_score -= 10
    else:
        if combat.en_score + encounter_score_weapon_bonus() >= 50:
            print("The {0} is taken by surprise.\n"
                  "You drive your {1} into it.\n".format(wv.banshee_name, combat.player_weapon.name))
            wv.switch_final_encounter = False
            final_encounter_over(True, True)  # Player is victor (true), loser is dead (true)
        else:
            combat.player_acted = True
            if combat.en_score > 25:
                print("The {0} narrowly dodges the attack with your {1}.\n"
                      "\n".format(wv.banshee_name, combat.player_weapon.name))
            else:
                print("The {0} dodges the attack with your {1}.\n"
                      "\n".format(wv.banshee_name, combat.player_weapon.name))
            combat.en_score += 10


def banshee_combat_command_item():
    if wv.inventory is not None:
        print("In your inventory you have:", end=" ")
        item_name_list = []
        # If the player has an inventory go through create a menu of options from items in said inventory.
        for item in wv.inventory[-1]:
            item_name = item.name.split()
            print(item_name[-1], end=", ")
            item_name_list.append(item_name[-1].upper())
        item_name = wv.inventory[-1].name.split()
        print(item_name[-1], end=".\n")
        item_name_list.append(item_name[-1].upper())
        #text
    else:
        print("You have nothing in your inventory!\n")
        txt.slow_print("(Please type FIGHT, ITEM, or MOVE!)")


def movement_option_and_input_lists():
    if combat.position == "close":
        return ["break the grapple and move further away"]
    elif combat.position == "near" or combat.position == "distress":
        return ["move closer", "move further away"]
    elif combat.position == "far":
        return ["move closer", "attempt to flee"]


def banshee_combat_command_move():
    movement_options, movement_input = [], ["nowhere"]
    # Different text and options based on the position of the enemy
    if combat.position == "close":
        txt.slow_print("You are grappling with the {0}!".format(wv.banshee_name))
    elif combat.position == "near" or combat.position == "distress":
        txt.slow_print("You are near the {0}.".format(wv.banshee_name))
    elif combat.position == "far":
        txt.slow_print("You are standing away from the {0}.".format(wv.banshee_name))

    # We get the options for movement based on combat position and display hem
    txt.slow_print("\nWhere would you like to move?")
    print("You can ", end=" ")
    print(" or ".join(movement_option_and_input_lists()))
    print(".")
    print("Type one of the following movement commands:", end=" ")
    valid_option_list, valid_inputs = movement_option_and_input_lists(), []
    for i in valid_option_list:
        valid_inputs.append(i[-1].upper())

    """input("or type \"nowhere\" if you don't wish to move.")
    
    # FINISH THIS
    combat.player_acted = False  # change this to true once this function works
    print("Move command not yet implemented, you should return to the start of the combat loop.\n")
    sleep(0.2)"""


# ---------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------

    # THESE FUNCTIONS RELATE TO THE INITIAL FUNCTION IN THE COMBAT LOOP (final_encounter_intro())


def final_encounter_intro():
    # This function begins the fight, tallies initial 'encounter score' (metric for winning/losing)
    # It also allows for an opening option to influence the start of the fight.
    # Victory will be largely based off of any weapons found, but doing tasks around the village

    # Player gains bonuses on this encounter based on how much they did in the game
    combat.en_score += get_final_quest_score()

    # We check what the best weapon the player has is, so we can later award bonuses based on it
    combat.player_weapon = is_armed()

    # Introductory text
    txt.slow_print("A haggard-looking woman in torn rags approaches you as you step outside...")
    txt.slow_print("From a distance you almost mistake her for human,"
                   "until you notice the long claws where her hands should be..")
    if wv.banshee_name == "banshee":
        print("The drawings were crude but the likeness is almost exact."
              "\n A false banshee stands before you.")
        combat.en_score += 10
        final_encounter_intro_p2()
    else:
        # Approaching the banshee is a bad idea
        txt.slow_print("\nDo you wish to greet her?")
        if txt.confirm_action() is True:
            combat.en_score -= 5
            txt.slow_print("You walk up to the {0}...".format(wv.banshee_name))
            print("As you approach she lunges at you!")
            combat.position = "close"
            # we begin combat here!
            banshee_combat()
        else:
            combat.en_score += 5
            final_encounter_intro_p2()


def final_encounter_intro_p2():
    print("You eye the {0} from a distance.".format(wv.banshee_name))
    txt.slow_print("She seems to be studying you.")
    txt.slow_print("You notice a feral, dangerous, look upon her face.")
    print()
    txt.slow_print("Do you wish to approach slowly?")
    if txt.confirm_action() is True:
        print("You step towards the {0} as carefully as you can.".format(wv.banshee_name))
        print("She attacks!")
        txt.slow_print("You barely manage to avoid her claws as she swings at you.")
        print()
        if combat.player_weapon is not None:
            txt.slow_print("You are armed. Do you want to fight back?")
            if txt.confirm_action() is True:
                combat.position = "far"
                # we begin combat here!
                banshee_combat()
            else:
                print("Given the opportunity the {0} quickly lunges at you.".format(wv.banshee_name))
                combat.position = "close"
                banshee_combat()
        else:
            print("Without a weapon to fight back she quickly lunges at you!")
            # removed bonus at this stage as positions can change in next stage
            # encounter_score += weapon.close_score
            # we begin combat here!
            combat.position = "close"
            banshee_combat()
    else:
        print("As you stand, watching the {0}, a pain begins to build in your skull.".format(wv.banshee_name))
        txt.slow_print("Your vision blurs and for a moment, just a moment, you lose concentration.")
        print("By the time your focus returns the {0} has covered incredible distance.".format(wv.banshee_name))
        print("The {0} lunges at you!".format(wv.banshee_name))


def is_armed():
    # THIS FUNCTION IS TO GRADE THE EFFECTIVENESS OF THE PLAYER'S WEAPON IN THEIR CURRENT SITUATION
    class WeaponStats:
        def __init__(self, name, long_score, close_score):
            self.name = name
            self.long_score = long_score
            self.close_score = close_score

    if inv.blacksmith_blade in wv.player_inventory:
        return WeaponStats("blade", 30, 30)
    elif inv.carpenter_axe in wv.player_inventory:
        return WeaponStats("axe", 30, 20)
    elif inv.church_stake in wv.player_inventory:
        return WeaponStats("stake", 0, 20)
    elif inv.farmer_shovel in wv.player_inventory:
        return WeaponStats("shovel", 20, 10)
    elif inv.church_glass in wv.player_inventory:
        return WeaponStats("glass", 0, 20)
    elif inv.farmer_hoe in wv.player_inventory:
        return WeaponStats("hoe", 20, 10)
    elif inv.broken_fishing_pole in wv.player_inventory:
        return WeaponStats("pole", 10, 10)
    else:
        return None


def get_final_quest_score():
    # Quest progress directly influences your success chance at the end of the game
    # written in this manner so variables/switches can be added/removed without breaking anything
    quest_score_tally = 0
    # int variables add their value
    for item in wv.variables_that_influence_final_score:
        quest_score_tally += getattr(wv, item)
    # 'switches' (bool variables really) add a flat 3 if true
    for item in wv.switches_that_influence_final_score:
        if getattr(wv, item) is True:
            quest_score_tally += 3
    # this tally becomes the 'encounter score' in the main function, an important metric
    return quest_score_tally


# ---------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------

# THESE FUNCTIONS ARE RELATED TO BANSHEE ACTIONS INSIDE THE BANSHEE COMBAT


def banshee_action():
    if combat.position == "distress":
        banshee_action_attack(0,50,
                              "The banshee_name is distressed!"
                              "The banshee_name is no longer in distress!",
                              "The banshee_name continues to be distressed and is unable to act.")
    elif combat.position == "close":
        banshee_action_attack(20,40,
                              "Trapped in a frantic melee with the banshee_name, you try to protect yourself."
                              "The banshee_name impales you in the stomach with one of its long claws!",
                              "You successfully push back against the banshee_name and stop it from harming you.")
    elif combat.position == "near":
        banshee_action_attack(5,25,
                              "The banshee_name attempts to close the distance between you!."
                              "The banshee_name rushes forward and cuts you with one of its claws!",
                              "The banshee_name tries to close the distance but you manage to keep it away.")
    elif combat.position == "far":
        banshee_action_attack(1,10,
                              "Trapped in a frantic melee with the banshee_name, you try to protect yourself."
                              "The banshee_name sprints forward with incredible speed - its claws rake you!",
                              "The banshee_name does not do anything.")


def banshee_action_attack(rand1, rand2, banshee_attack_string, banshee_success_string, banshee_failure_string):
    banshee_attack_string = txt.word_replacer(banshee_attack_string, "banshee_name", wv.banshee_name)
    banshee_success_string = txt.word_replacer(banshee_success_string, "banshee_name", wv.banshee_name)
    banshee_failure_string = txt.word_replacer(banshee_failure_string, "banshee_name", wv.banshee_name)
    txt.slow_print(banshee_attack_string)
    if (combat.en_score + encounter_score_weapon_bonus()) - randint(rand1, rand2) < 0:
        txt.slow_print("!!!!!")
        print(banshee_success_string)
        if combat.position == "close":
            wv.switch_final_encounter = False
            final_encounter_over(False, True)  # Player is victor (false), loser is dead (true)
        else:
            if combat.position == "near":
                combat.en_score -= 20
            elif combat.position == "distress":
                combat.position = "near"
                combat.en_score -= 35
                txt.slow_print("The {0} gathers its focus once more and shrieks in your direction.".format(wv.banshee_name))
            else:
                combat.en_score -= 10
            txt.slow_print("You are wounded and grappled. Your chances of survival just dropped considerably.")
            combat.position = "close"
    else:
        txt.slow_print(banshee_failure_string)
        combat.en_score += 5


# ---------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------

# THESE FUNCTIONS ARE RELATED TO PLAYER ACTIONS INSIDE THE BANSHEE COMBAT


def print_banshee_positioning():
    # Different text based on the position of the enemy
    if combat.position == "close":  txt.slow_print("The %s is grappling with you, attempting to kill you." % wv.banshee_name)
    elif combat.position == "near":  txt.slow_print("The %s is circling you, watching you unblinkingly." % wv.banshee_name)
    elif combat.position == "distress":   txt.slow_print("The %s is nearby, but in distress and ignoring you." % wv.banshee_name)
    elif combat.position == "far":  txt.slow_print("The %s is studying you from a distance." % wv.banshee_name)


def print_banshee_command_options():
    if combat.player_weapon is not None:
        txt.slow_print("You are armed with a %s.\n" % combat.player_weapon.name)
    txt.slow_print("What do you do?")
    print(Fore.RED + "[FIGHT]", end=" ")
    print(Fore.GREEN + "[ITEM]", end=" ")
    print(Fore.BLUE + "[MOVE], end=")
    print(Style.RESET_ALL)


# adds a bonus to encounter score based on your weapon and position
def encounter_score_weapon_bonus():
    if combat.player_weapon is not None:
        if combat.position == "close":
            return combat.player_weapon.close_score
        elif combat.position == "near" or "distress":
            return combat.player_weapon.long_score
        else:
            return 0
    else:
        return -10


# this func checks your inventory and asks you what item you want to use
def in_combat_item_use_ask(item_name_list):
    txt.slow_print("Which item do you wish to use? Type 'NONE' to return.")
    ask_for_input = input("Input: ")
    if ask_for_input.lower() == "none":
        txt.slow_print("(Please type FIGHT, ITEM, or MOVE!)")
        sleep(0.2)
        banshee_combat_command_processing(input("Input: "))
    elif ask_for_input.lower() not in item_name_list:
        txt.slow_print("Input is not an item in your inventory!")
        sleep(0.2)
        banshee_combat_command_processing("item")
    else:
        in_combat_item_use_activate(ask_for_input.lower(), item_name_list)


# this function activates the item passed from above func
def in_combat_item_use_activate(item_used, item_name_list):
    if item_used == "test":
        txt.slow_print("How did you get this item what the heck")
        txt.slow_print("Quitting application.")
        quit()

    # Functional item branches
    elif item_used == "diary":
        print("An old diary obtained from the basket weaver!")
        # re-read? glean info?
        in_combat_item_use_ask(item_name_list)
    elif item_used == "salt":
        print("A pinch of salt!")
        if combat.position != "far":
            txt.slow_print("You are {0} to the {1}. Do you wish to throw the salt at the {1}?"
                           .format(combat.position, wv.banshee_name))
            if txt.confirm_action() is True:
                combat.player_acted = True
                txt.slow_print("You throw the salt at the {0}!".format(wv.banshee_name))
                wv.inventory.remove(inv.handful_of_salt)
                if combat.position == "close" or combat.position == "near" and combat.en_score + randint(1,30) > 25:
                    txt.slow_print("...")
                    print("The {0} is covered in salt!".format(wv.banshee_name))
                    txt.slow_print("The {0} screeches and tries to shake the salt off."
                                   " The {0} is clearly distressed, keeping a distance from you.".format(wv.banshee_name))
                    combat.en_score += 25
                else:
                    txt.slow_print("!!!")
                    print("The {0} avoids the salt!".format(wv.banshee_name))
            else:
                in_combat_item_use_ask(item_name_list)

    # Weapon equipping/changing branches
    elif item_used == "blade":
        if equip_weapon("blade", item_name_list) is True:
            combat.player_weapon = is_armed().WeaponStats("blade", 30, 30)

    elif item_used == "pole":
        if equip_weapon("pole", item_name_list) is True:
            combat.player_weapon = is_armed().WeaponStats("pole", 10, 10)

    elif item_used == "axe":
        if equip_weapon("axe", item_name_list) is True:
            combat.player_weapon = is_armed().WeaponStats("axe", 30, 20)

    elif item_used == "stake":
        if equip_weapon("stake", item_name_list) is True:
            combat.player_weapon = is_armed().WeaponStats("stake", 0, 20)

    elif item_used == "shovel":
        if equip_weapon("shovel", item_name_list) is True:
            combat.player_weapon = is_armed().WeaponStats("shovel", 20, 10)

    elif item_used == "glass":
        if equip_weapon("glass", item_name_list) is True:
            combat.player_weapon = is_armed().WeaponStats("glass", 0, 20)

    elif item_used == "hoe":
        if equip_weapon("hoe", item_name_list) is True:
            combat.player_weapon = is_armed().WeaponStats("hoe", 20, 10)

    # Catch all
    else:
        combat.player_acted = False
        txt.slow_print("That item has no function in combat.")

        def equip_weapon(item_id_passed, item_name_list):
            if combat.player_weapon.name != item_id_passed:
                combat.player_acted = True
                txt.slow_print("Do you wish to equip the {0}?".format(item_id_passed))
                if txt.confirm_action() is True:
                    txt.slow_print("You put away your {0} and instead equip the {1}.".format(combat.player_weapon.name,
                                                                                             item_id_passed))
                    return True
                else:
                    return False
            else:
                combat.player_acted = False
                txt.slow_print("The {0} is your equipped weapon.".format(combat.player_weapon.name))
                in_combat_item_use_ask(item_name_list)
                return False


# ---------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------

# THIS IS THE ENDING FUNCTION


def final_encounter_over(victory_state, death_state):
    if victory_state is True and death_state is True:
        # you won and the banshee died
        pass
    elif victory_state is True and death_state is False:
        # you won, sort of. The banshee fled.
        pass
    elif victory_state is False and death_state is False:
        # you lost, but at least you lived. The village might not be so lucky.
        pass
    elif victory_state is False and death_state is True:
        # you lost, another victim of the false banshee.
        pass




# ---------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------

# ORIGINAL NOTES KEPT FOR POSTERITY

# NOTES # NOTES # NOTES # NOTES # NOTES # NOTES # NOTES # NOTES # NOTES # NOTES # NOTES # NOTES
# NOTES # NOTES # NOTES # NOTES # NOTES # NOTES # NOTES # NOTES # NOTES # NOTES # NOTES # NOTES
# NOTES # NOTES # NOTES # NOTES # NOTES # NOTES # NOTES # NOTES # NOTES # NOTES # NOTES # NOTES

    # Original notes kept for posterity

    # Choose action, modifies combat state, returns to this function
    # Run (impossible unless far, banshee identified, and high encounter score)
    # Attack
    # Move closer
    # Move further away

    # write lists for different paths/responses
    # threat
    # positions - close, near, far

    # Encounter score at 40 means automatic win(?)
    # Negative encounter score means automatic loss (randint?)
    # Scaling chance of victory every turn + entropic scale of loss every turn

    # ---------------------------------------------------------------------------------------------------
    # ---------------------------------------------------------------------------------------------------
    # ---------------------------------------------------------------------------------------------------