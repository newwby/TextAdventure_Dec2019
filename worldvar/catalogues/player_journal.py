
class JournalQuest:
    def __init__(self, journal_id, name, state, description):
        self.ID = journal_id
        self.name = name
        self.state = state
        self.desc = description
        self.completion = False


test_quest = JournalQuest(0, "Test", 1, "A test thing.")

village_affair = JournalQuest(1, "An Affair", 1,
                              "There's something going on between the carpenter's wife and the blacksmith.")

peculiar_noise = JournalQuest(2, "Strange Noises", 1,
                              "A villager has complained of a strange noise. I can't hear anything.")

missing_children = JournalQuest(3, "Missing Children", 1,
                                "A villager mentioned they haven't seen their children recently.")

cannot_leave = JournalQuest(4, "Stuck in a Rut", 1,
                            "Other people seem to want to leave, but can't.")

dead_bodies = JournalQuest(5, "Death Abounds", 1,
                           "People are dying, and nobody seems to care. I should see the alderman.")

main_quest = JournalQuest(6, "The Strange Village", 1,
                          "I awoke here, and my mind is muddled. I should ask around.")

elders = JournalQuest(99, "Village Elders", 1,
                      "I should speak with the older people in the village about the mysterious happenings.")
# state 2 = go to priest or basket weaver
# "The Alderman mentions asking the older inhabitants of the village, the priest or basket weaver"
# state 3 = go to priest
# "The basket weaver's journal mentions that the priest might know more."

quite_hungry = JournalQuest(99, "Test", 1, "A test thing.")
