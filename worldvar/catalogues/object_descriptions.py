
# --------------------------
# Building item/entry descriptions below
# --------------------------


class Entry:
    def __init__(self, owner, name, state, update, appearance, desc):
        self.owner = owner
        self.name = name
        self.state = state
        self.update = update
        self.appearance = appearance
        self.desc = desc


# --------------------------------
# Default Entries for house1
# --------------------------------

# "This building is sweltering, a wall of heat hitting you as you step across the threshold."

house1_blacksmith = Entry\
    ("house1", "BLACKSMITH", 1, "Talk_man4", "the blacksmith",
     "The blacksmith is a gruff-looking sort wearing a muck-covered apron.")

house1_fireplace = Entry\
    ("house1", "FIREPLACE", 1, None, "a fireplace and chimney on the far wall",
     "The chimney is stained with years of smoke and soot.")

house1_forge = Entry\
    ("house1", "FORGE", 1, "Call_SeenBlacksmithBlade", "a blacksmith's forge",
     "A smith's forge, with a smelter and anvil. An unfinished BLADE lays upon it.")

house1_blade = Entry\
    ("house1", "BLADE", 0, "Call_TakeBlacksmithBlade", "an unattended blade",
     "A sharp piece of metal, an unfinished weapon of some sort. It could be useful in a pinch.")

house1_entries = [house1_blacksmith, house1_fireplace, house1_forge]

# --------------------------------
# Default Entries for fisherman's home
# --------------------------------

# "Some of the fish in this room are clearly a little old. The smell is barely bearable."

house2_fisherman = Entry\
    ("house2", "FISHERMAN", 1, "Talk_man5", "the fisherman",
     "The fisherman appears to be missing most of his teeth, but is not short of a smile.")

house2_fish_rack = Entry\
    ("house2", "FISH RACK", 1, None, "a rack of hanging fish",
     "Fish are strung up on a rack at the far side of the room. Most look a bit too old to eat.")

house2_fishing_pole = Entry\
    ("house2", "BROKEN POLE", 1, "Call_BrokenFishingPole", "a broken fishing pole",
     "One half of an old fishing pole is balanced against the wall. It looks like it has seen better days.")

house2_nets = Entry\
    ("house2", "FISHING NETS", 1, None, "a pile of fishing nets",
     "Fishing nets occupy most of the floor space in this small home.")

house2_entries = [house2_fisherman, house2_fish_rack, house2_fishing_pole, house2_nets]

# --------------------------------
# Default Entries for basket weaver's home
# --------------------------------

# "Scattered knick-knacks and junk abound in this tiny home."

house3_basket_weaver = Entry\
    ("house3", "BASKET WEAVER", 1, "Talk_woman4", "the basket weaver",
     "The basket weaver is an elderly woman sitting on a small carpet in the middle of the room.")

house3_baskets = Entry\
    ("house3", "BASKETS", 1, None, "a basket",
     "A collection of woven reed baskets sit at the edge of the room.")

house3_reeds = Entry\
    ("house3", "REEDS", 1, None, "the pile of reeds",
     "A neatly piled stack of reeds sits beside the basket weaver, waiting to be worked on.")

house3_books = Entry\
    ("house3", "BOOKS", 1, "Call_TakeOldDiary", "a stack of old books",
     "Some old books are piled up in the corner of the room.")

house3_entries = [house3_reeds, house3_basket_weaver, house3_baskets, house3_books]

# --------------------------------
# Default Entries for farmer couple's home
# --------------------------------

# "On one side of the room sits a strong oaken bed, on the other a pile of hay that looks well slept-in."

house4_farmer = Entry\
    ("house4", "FARMER", 1, "Talk_man6", "the farmer",
     "The farmer looks at you with suspicion. You have a feeling strangers are quite strange in these parts.")

house4_farmer_wife = Entry\
    ("house4", "FARMER'S WIFE", 1, "Talk_woman5", "the farmer's wife",
     "The farmer's wife is busy sweeping the floors and cleaning up in what appears to be an immaculate home.")

house4_oaken_bed = Entry\
    ("house4", "BED", 1, None, "an oaken bed",
     "Upon the bed lays a pile of neatly-arranged blankets.")

house4_pile_of_hay = Entry\
    ("house4", "HAY", 1, "Call_PileOfHay", "a pile of hay",
     "It looks well slept in. A child's doll lays nearby.")

house4_entries = [house4_farmer, house4_farmer_wife]

# --------------------------------
# Default Entries for solo farmer's home
# --------------------------------

# "The smell of animal dung is overpowering. Apparently this room is home to more than just humans."

house5_farmer = Entry\
    ("house5", "FARMER", 1, "Talk_man7", "the farmer",
     "The farmer is an angry-looking sort, and despite his small stature he tries to stand taller as you approach.")

house5_cow = Entry\
    ("house5", "COW", 1, "Talk_cow", "two cows",
     "A pair of cows regard you with disinterest.")

house5_dung = Entry\
    ("house5", "DUNG", 1, None, "animal dung",
     "A pile of animal dung. Daisies it ain't.")

house5_hoe = Entry\
    ("house5", "HOE", 1, "Call_TakeFarmerHoe", "a hoe",
     "Great for hoeing around the land. You've no time for that right now.")

house5_shovel = Entry\
    ("house5", "SHOVEL", 1, "Call_TakeFarmerShovel", "a shovel",
     "A well-used farmer's shovel.")

house5_entries = [house5_farmer, house5_cow, house5_dung, house5_hoe, house5_shovel]

# --------------------------------
# Default Entries for carpenter's home
# --------------------------------

# "Stacks of lumber abound inside, kept well out of the rain."

house6_carpenter = Entry\
    ("house6", "CARPENTER", 1, "Talk_man8", "the carpenter",
     "The carpenter barely seems to notice you, rustling around his home looking for something.")

house6_carpenter_wife = Entry\
    ("house6", "CARPENTER'S WIFE", 1, "Talk_woman6", "the carpenter's wife",
     "The carpenter's wife smiles at you politely and waits for you to speak.")

house6_sawbench = Entry\
    ("house6", "SAWBENCH", 1, None, "a sawbench",
     "A large sawbench occupies the wall closest to the door.")

house6_lumber = Entry\
    ("house6", "LUMBER", 1, None, "lumber",
     "The majority of the house is taken up by piles of dry lumber.")

house6_axe = Entry\
    ("house6", "AXE", 1, "Call_TakeCarpenterAxe", "a woodcutter's axe",
     "A woodsman's axe, useful for felling trees.")

house6_cooking_pot = Entry\
    ("house6", "COOKING POT", 1, None, "a cooking pot",
     "A cooking pot, simmering with a pleasant smell.")

house6_entries = [house6_carpenter, house6_carpenter_wife, house6_axe, house6_lumber, house6_sawbench, house6_cooking_pot]

# --------------------------------
# Default Entries for alderman's home
# --------------------------------

# "Much grander than the rest of the village, this large home features a separate private room."

house7_alderman = Entry\
    ("house7", "ALDERMAN", 1, "Talk_man10", "the alderman",
     "The alderman, a plump fellow in his middle age, does not stand to greet you.")

house7_alderman_wife = Entry\
    ("house7", "ALDERMAN'S WIFE", 1, "Talk_woman7", "the alderman's wife",
     "The alderman's wife glares at you, with barely hidden disdain.")

house7_bedroom_door = Entry\
    ("house7", "DOOR", 1, "alderman_door", "a door to a private room",
     "A door that leads to the alderman's private bedroom.")

house7_seating = Entry\
    ("house7", "CHAIRS", 1, None, "public seating",
     "Many chairs are scattered around the alderman's foyer, allowing councils to be held.")

house7_entries = [house7_alderman, house7_alderman_wife, house7_bedroom_door, house7_seating]

# --------------------------------
# Default Entries for alderman's bedroom
# --------------------------------

# "Inside this small private room lies a fancifully carved bed covered in fine garments.

house7b_main_door = Entry\
    ("house7", "DOOR", 1, "alderman_door_2", "a door leading back out",
     "A door that leads outside of the alderman's private bedroom.")

house7b_entries = [house7_alderman, house7b_main_door]

# --------------------------------
# Default Entries for church
# --------------------------------

# "Long wooden pews decorate this deep stone hall. Gaps in the walls lay where windows should sit

church_priest = Entry\
    ("church", "PRIEST", 1, "Talk_man9", "the priest",
     "The priest of the village church is an old man with a fresh scar upon his forehead.")

church_pews = Entry\
    ("church", "PEWS", 1, "Call_BreakPews", "church pews",
     "Long wooden pews run in parallel along the church. At least a few are splintering.")

church_windows = Entry\
    ("church", "WINDOWS", 1, "Call_CheckWindows", "empty windows",
     "Instead of windows there are gaps in the stone walls. Small glass shards sit beneath one of the gaps.")

church_private_door = Entry\
    ("church", "DOOR", 1, "Call_church_door_to_private", "a door to a private room",
     "A door that leads to a small room within the church.")

church_entries = [church_priest, church_pews, church_windows, church_private_door]

# --------------------------------
# Default Entries for priest's room in church
# --------------------------------

# "A humble room fit for only a small sleeping patch and a bucket."

church_b_private_door = Entry\
    ("church_b", "DOOR", 1, "Call_church_door_to_main", "a door leading out of the back room",
     "A door that leads to the main halls of the church.")

church_b_bucket = Entry\
    ("church_b", "BUCKET", 1, None, "empty bucket",
     "A bucket, for private ablutions and relief.")

church_b_pile_of_hay = Entry\
    ("church_b", "HAY", 1, None, "a pile of hay",
     "A small pile of hay that looks well slept-upon.")

church_b_stacks_of_books = Entry\
    ("church_b", "BOOKS", 1, "Call_Priest_Books", "stacks of books everywhere",
     "Books and notes cover every spare inch of this room.")

church_b_entries = [church_priest, church_b_private_door, church_b_bucket, church_b_pile_of_hay]

# --------------------------------
# --------------------------------
