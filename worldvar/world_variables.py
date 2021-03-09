
from worldvar.catalogues import player_inventory
from worldvar.catalogues import player_journal

# -----
# Default variables set by start
# -----

pos_x = 5           # Where is the player on the x axis
pos_y = 5           # Where is the player on the y axis

inventory = []      # Player list of equipment
journal = []        # Player journal entries

outdoor = True      # Is the player outside? default True
ARMED_REMOVE_ME = False       # Does the player have a weapon? default False - this can now be superceded by inventory

# ------
# Quest variables, set to 0 initially
# ------

village_affair_knowledge = 0
village_noise = 0
children_mentioned = 0
leave_the_village = 0
death_counter = 0
death_stink = 0

test_counter = 0
secret_cow_level = 0

variables_that_influence_final_score = ["village_affair_knowledge",
                                        "village_noise",
                                        "children_mentioned",
                                        "leave_the_village"
                                        ]
switches_that_influence_final_score = ["switch_village_affair_public",
                                       "switch_village_cacophony",
                                       "switch_children_gone",
                                       "switch_leave_the_village"
                                       ]

# ------
# Dialogue lists to prevent NPCs progressing quests by repeated chatting
# ------

call007_list, call008_list, call009_list, leave_village_list = [], [], [], []

# ------
# Quest switches from dialogue/items; most are set false initially, changed by chatting with NPCs/exploring buildings
# ------

switch_TestGVar = False

switch_BladeSpotted = False
switch_CWife_Smith = False
switch_Carp_Leaving = True
switch_not_Carp_Leaving = False
switch_Villager_Leaving = True
switch_not_Villager_Leaving = False
switch_Fisherman_Leaving = True
switch_not_Fisherman_Leaving = False
switch_Smith_Friendly = False
switch_Smith_CWife = False
switch_affair_rumours = False
switch_village_affair_public = False
switch_village_noise = False
switch_village_cacophony = False
switch_children_missing = False
switch_children_gone = False
switch_leave_the_village = False
switch_basket_weaver_books = False
switch_angry_carpenter = False
switch_angry_farmer = False
switch_question_priest = False
switch_back_room_permission_church = False
switch_priest_memory_problems = False

switch_children_seen = False    # Switch for if player sees children in random events
switch_heard_noise = False      # Switch for if player hears noise in random events
switch_outdoor_death = False    # Switch for if someone is dead outside
switch_village_death = False    # Switch for if player finds a dead body
switch_villager_rut = False     # Switch for if player finds out lots of villagers want to leave but can't
switch_elders = False           # Switch for if the player is pointed toward the older villagers
switch_final_encounter = False  # Switch for if the player progresses to the end state

banshee_name = "clawed woman"   # Identifier/name of the banshee
