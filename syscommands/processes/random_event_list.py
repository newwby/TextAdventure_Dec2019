
from worldgen import generation_dict as wgen
from worldvar import world_variables as wv
from worldvar.catalogues import object_descriptions as obj_d
from syscommands import text_commands as txt
from syscommands.processes import script_calls as call
from random import randint
import re

completed_events = []

walking_events_outdoor = [
    ["You step in cow manure and groan, scraping it off as you continue.", None],
    ["The wind picks up, to your aggravation.", None],
    ["A wild animal howls in the distance.", None],
    ["A group of small children run past, yelling and screaming. They are gone before you can react.", 1000],
    ["Your stomach grumbles.", None],
    ["The beginnings of a stitch in your side irritates you.", None],
    ["You're sure you just heard something, but you can put your finger on what.", 1001],
    ["... where are you going? You're sure you just forgot something important, but you can't remember what.", None],
    ["You sigh.", None],
    ["The smell of manure is making it difficult to breathe freely.", None],
    ["Someone laughs, though you're not sure from where. Hopefully it wasn't at you.", None],
    ["Someone is singing, though you can't tell who.", 1002],
    ["You hear a child laugh, but you cannot see any children nearby.", 1003],
    ["You stub your toe against a rock and curse.", None],
    ["A stale smell hangs on the wind.", None],
    ["Somebody nearby yells in surprise.", 1004],
    ["You step in what you hope is cow manure.", None],
    ["Your mind wanders and you forget what you're doing for a moment.", None],
    ["Somebody in the village shrieks out! What was that?", 1005],
    ["A cow lets out a low moo.", None],
    ["For a moment you are sure you hear... what was that? Whatever it was is over now.", 1006],
    ["The sun dips behind a cloud and the village darkens.", None],
    ["A sickening crunch echoes out across the village.", 1007],
    ["You spot a pleasant-looking flower nearby.", None],
    ["Suddenly you hear nothing, as though something you weren't aware of just ceased.", 1008],
    ["The wind blusters", None],
    ["Someone... someone was singing?", 1009],
]

walking_events_indoor = [
    ["Some child has left their toy on the floor here.", None],
    ["It is dustier than you'd like.", None],
    ["The air hangs cold inside.", None],
    ["You scrape your shoes against the door frame.", None],
    ["A single candle is all that keeps the room lit.", None],
    ["Outside the home shingles and thatch are scattered, but there is no debris inside.", None],
    ["A well-tended plant sits by your side.", None],
    ["The smell of freshly cooked food permeates throughout.", None],
    ["Your eyes take a moment to adjust to the darkness inside this home.", None],
    ["You sneeze as you enter the building.", None],

]


# redirect functions
def rel_script_1000():  random_event_seen_children(1000)
def rel_script_1001():  random_event_heard_noise(1001)
def rel_script_1002():  random_event_heard_noise(1002)
def rel_script_1003():  random_event_seen_children(1003)
def rel_script_1004():  random_event_death(1004)
def rel_script_1005():  random_event_death(1005)
def rel_script_1006():  random_event_death(1006)
def rel_script_1007():  random_event_death(1007)
def rel_script_1008():  random_event_death(1008)
def rel_script_1009():  random_event_death(1009)
# functions that exist only to call other functions


def random_event_heard_noise(event_identifier):
    if event_identifier not in completed_events:
        # event runs here
        completed_events.append(event_identifier)
        wv.village_noise += 1
        wv.switch_heard_noise = True
        call.quest_strange_noise()


def random_event_seen_children(event_identifier):
    if event_identifier not in completed_events:
        completed_events.append(event_identifier)
        # set switch that player has personally seen missing children
        wv.switch_children_seen = True
        wv.children_mentioned += 1
        call.quest_missing_children()


def random_event_death(event_identifier):
    # this function is called with a unique identifier,
    # which is then passed to a list to check if this function has already been called with that identifier
    if event_identifier not in completed_events:
        completed_events.append(event_identifier)

    # this script randomly chooses an npc set (either a solo npc (in/out) or both occupants of a house) to die

        # this list is for deciding who dies
        deletion_list = ["house1", "house2", "house3", "house4", "house5", "house6", "church",
                             "woman1", "woman2", "woman3", "man1", "man2", "man3"]

        dict_kill_npc_outdoor = {
                "house1": ["house1_blacksmith"],
                "house2": ["house2_fisherman"],
                "house3": ["house3_basket_weaver"],
                "house4": ["house4_farmer", "house4_farmer_wife"],
                "house5": ["house5_farmer"],
                "house6": ["house6_carpenter", "house6_carpenter_wife"],
                "church": ["church_priest"],
            }

        # this dictionary is filled with slightly modified death descriptions to be used later on
        death_descriptions = {
                "m1" : "a middle-aged man, wearing a ragged jacket, sprawled face-down across the ground.",
                "m2": "the partial-remains of a man. His legs and left arm are missing.",
                "m3": "an elderly man with a bloody gash across his chest. His eyes are closed and he isn't breathing.",
                "w1": "a dead woman in a long dress and shawl, the latter of which is torn by what looks like claw marks.",
                "w2": "a young woman, dead, laying on the ground. Her neck is torn open and a pool of blood is beneath her.",
                "w3": "a murdered elderly woman, pieces of which are scattered in several directions.",
                "house1_blacksmith" : "The dead body of the stout blacksmith lays before you.",
                "house2_fisherman" : "The fisherman is dead. His head is no longer attached to his body",
                "house3_basket_weaver" : "Someone has violently murdered the elderly basket weaver.",
                "house4_farmer" : "The farmer and his wife are slouched together, dead."
                                  "His body lays atop hers, in some futile attempt to shield her",
                "house4_farmer_wife" : "The farmer and his wife are slouched together, dead."
                                       "The wife's body is beneath the farmer, her neck savaged and torn.",
                "house5_farmer" : "The farmer in this house is dead. The animals don't seem to care.",
                "house6_carpenter" : "The carpenter is splayed across the floor, dead, his throat slashed and bleeding.",
                "house6_carpenter_wife" : "A deep cut is etched across the carpenter's wife's face, mutilating her.",
                "church_priest" : "The priest is dead, and stinks of death. His face is partially chewed."
            }

        # CODE BELOW
        # who is the target to die?
        target_npc = randint(0, len(deletion_list))

        try:
            if deletion_list[target_npc] in dict_kill_npc_outdoor:
                # is it an indoor NPC?
                for i in dict_kill_npc_outdoor[deletion_list[target_npc]]:
                    # we modify the object entry to a dead body
                    getattr(obj_d, i).state = 0
                    getattr(obj_d, i).update = "dead_" + i.lower()
                    getattr(obj_d, i).appearance = "the dead body of " + getattr(obj_d, i).appearance
                    getattr(obj_d, i).desc = death_descriptions[i]

            else:
                # is it an outdoor NPC? if so we need to go through worldgen and remove it
                for i in wgen.world_gen_dict:
                    if wgen.world_gen_dict[i][1] == deletion_list[target_npc]:
                        # we modify the worldgen dictionary entry to a dead body
                        wgen.world_gen_dict[i][0] = "CORPSE"
                        wgen.world_gen_dict[i][1] = "corpse_" + deletion_list[target_npc][0] + \
                                                    deletion_list[target_npc][-1]
                        # using identifiers from the selected npc we pick a description from the death_desc dictionary
                        wgen.world_gen_dict[i][2] = death_descriptions[
                            deletion_list[target_npc][0] + deletion_list[target_npc][-1]]
                        # then we remove entry from deletion list
                wv.switch_outdoor_death = True
            deletion_list.pop(target_npc)
            wv.death_counter += 1
            if wv.death_counter > 5:
                txt.slow_print("\n.\n..\n...\nYou hear an unsettling, almost feral, cry... and then nothing...")
                txt.slow_print("As though a noise you weren't aware of just stopped.")
                wv.switch_final_encounter = True

        except IndexError:
            pass
