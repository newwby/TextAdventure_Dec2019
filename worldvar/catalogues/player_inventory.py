
class InventoryItem:
    def __init__(self, name, weight, description):
        self.name = name
        self.weight = weight
        self.desc = description


blacksmith_blade = InventoryItem("Unfinished Blade", 1,
                                 "An unfinished metal blade that could be a useful in a pinch.")

broken_fishing_pole = InventoryItem("Broken Pole", 1,
                                    "A broken fishing pole. Why are you carrying this around?")

old_diary = InventoryItem("Basket Weaver's Diary", 1,
                          "A page from years ago describes a similar situation happening in the priest's last village.")

carpenter_axe = InventoryItem("Woodcutter's Axe", 1,
                              "A hefty axe, good for chopping down wood.")

farmer_hoe = InventoryItem("Farming Hoe", 1,
                           "A short stick with a metal hoe/axe-head attached.")

farmer_shovel = InventoryItem("Shovel", 1,
                              "A heavy shovel used for digging up the earth.")

church_stake = InventoryItem("Wooden Stake", 1,
                             "A broken sliver of wood taken from a church pew.")

church_glass = InventoryItem("Glass Shard", 1,
                             "A large shard of glass taken from an old church window.")

handful_of_salt = InventoryItem("Pinch of Salt", 1,
                                "Salt used for seasoning, and warding off evil.")

test_item = InventoryItem("Test", 1, "A test thing.")
