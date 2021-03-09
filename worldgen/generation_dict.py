
# REWRITE WORLD_GEN_DICT TO REFERENCE WORLD_TABLE OBJECTS
# (e.g. value is the name of the correct variable)

world_gen_dict = {

    # FENCING SURROUNDING PLAY AREA

    "1, 1": ["NW FENCE", "fence", "a fence denoting the village boundary."],
    "0, 2": ["N FENCE", "fence", "a fence denoting the village boundary."],
    "0, 3": ["N FENCE", "fence", "a fence denoting the village boundary."],
    "0, 4": ["N FENCE", "fence", "a fence denoting the village boundary."],
    "0, 5": ["N FENCE", "fence", "a fence denoting the village boundary."],
    "0, 6": ["N FENCE", "fence", "a fence denoting the village boundary."],
    "0, 7": ["N FENCE", "fence", "a fence denoting the village boundary."],
    "0, 8": ["N FENCE", "fence", "a fence denoting the village boundary."],
    "1, 9": ["NE FENCE", "fence", "a fence denoting the village boundary."],
    "2, 1": ["W FENCE", "fence", "a fence denoting the village boundary."],
    "2, 9": ["E FENCE", "fence", "a fence denoting the village boundary."],
    "3, 1": ["W FENCE", "fence", "a fence denoting the village boundary."],
    "3, 9": ["E FENCE", "fence", "a fence denoting the village boundary."],
    "4, 1": ["W FENCE", "fence", "a fence denoting the village boundary."],
    "4, 9": ["E FENCE", "fence", "a fence denoting the village boundary."],
    "5, 1": ["W FENCE", "fence", "a fence denoting the village boundary."],
    "5, 9": ["E FENCE", "fence", "a fence denoting the village boundary."],
    "6, 1": ["W FENCE", "fence", "a fence denoting the village boundary."],
    "6, 9": ["E FENCE", "fence", "a fence denoting the village boundary."],
    "7, 1": ["W FENCE", "fence", "a fence denoting the village boundary."],
    "7, 9": ["E FENCE", "fence", "a fence denoting the village boundary."],
    "8, 1": ["W FENCE", "fence", "a fence denoting the village boundary."],
    "8, 9": ["E FENCE", "fence", "a fence denoting the village boundary."],
    "9, 1": ["SW FENCE", "fence", "a fence denoting the village boundary."],
    "9, 2": ["S FENCE", "fence", "a fence denoting the village boundary."],
    "9, 3": ["S FENCE", "fence", "a fence denoting the village boundary."],
    "9, 4": ["S FENCE", "fence", "a fence denoting the village boundary."],
    "9, 5": ["S FENCE", "fence", "a fence denoting the village boundary."],
    "9, 6": ["S FENCE", "fence", "a fence denoting the village boundary."],
    "9, 7": ["S FENCE", "fence", "a fence denoting the village boundary."],
    "9, 8": ["S FENCE", "fence", "a fence denoting the village boundary."],
    "9, 9": ["SE FENCE", "fence", "a fence denoting the village boundary."],

    # HOUSING AND VILLAGE OBJECTS

    "2, 2": ["SMALL HOUSE", "house1", "a small village home. \nThe sign outside suggests it is a blacksmith's."],
    "4, 3": ["SMALL HOUSE", "house2", "a small village home. \nA fish rack sits outside the home."],
    "4, 6": ["SMALL HOUSE", "house3", "a small village home. \nThe sign outside depicts a basket weaver at work."],
    "8, 4": ["SMALL HOUSE", "house4", "a small village home. \nThe tracks outside suggest it is a farmer's home."],
    "2, 8": ["SMALL HOUSE", "house5", "a small village home. \nThe cattle nearby suggest it is a farmer's home."],
    "8, 8": ["SMALL HOUSE", "house6", "a small village home. \nThe sign outside marks it as a carpenter's shop."],

    "6, 6": ["LARGE HOUSE", "house7", "a large village home, larger than all others in the village"],
    "6, 7": ["LARGE HOUSE", "house7", "a large village home, larger than all others in the village"],
    "7, 6": ["LARGE HOUSE", "house7", "a large village home, larger than all others in the village"],
    "7, 7": ["LARGE HOUSE", "house7", "a large village home, larger than all others in the village"],

    "3, 4": ["CHURCH", "church", "a rustic village church."],
    "3, 5": ["CHURCH", "church", "a rustic village church."],
    "2, 5": ["STEEPLE", "church steeple", "a rustic village church."],

    "6, 4": ["LAMP", "lamppost", "an unlit lamp."],

    # VILLAGERS

    "4, 4": ["WOMAN", "woman1", "a woman in an unkempt shawl."],
    "8, 2": ["MAN", "man1", "a man in a ragged jacket."],
    "3, 6": ["MAN", "man2", "a man with a haughty sneer."],
    "1, 3": ["WOMAN", "woman2", "a young woman fiddling with her hair."],
    "3, 8": ["MAN", "man3", "an elderly man with a welcoming smile."],
    "4, 8": ["WOMAN", "woman3", "an elderly woman with a vacant gaze."],

}