

class CombatEncounter:
    def __init__(self, name, encounter_score, player_weapon, positioning):
        self.ID = name
        self.en_score = encounter_score
        self.player_weapon = player_weapon
        self.position = positioning
        self.player_acted = False
