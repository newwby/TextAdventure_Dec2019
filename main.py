
import game_state
import syscommands.processes.script_calls as scall, syscommands.processes.random_event_list as prel
from worldvar import world_variables as wv

# interactions.begin_conversation("test_conversation", speaker="NPC: ")
# interactions.enter_home(home_key="house1")
# prel.random_event_death(1000)

"""print()
txt.slow_print("You are in a very small village.")
print()
txt.slow_print("You cannot remember how long you have been here.")
print()
txt.slow_print("Leaving... leaving doesn't seem like a good idea, but you don't know why.")
print()
txt.slow_print("Maybe somebody else knows why?")
for i in range(2):
    print()
wv.journal.append(wv.player_journal.main_quest)
"""

game_state.game_input()