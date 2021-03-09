
# --------------------------
# Code below
# --------------------------

pass

# --------------------------
# Conversation Lists Below
# --------------------------

# NOTE: Is it possible to write these as txt files then load them into dictionaries?

man1 = [  # Villager
    ["LEAVING", "\"Leaving is impossible. Stop trying.\"", "Dialogue_CallID_003", "Villager_Leaving"],
    ["FENCE", "\"The fence is for our own safety, the alderman sees to that.\"", None, None],
    ["LEAVE THE VILLAGE", "\"Hmm? Yes you can. What do you mean I said otherwise?\"", None, "not_Villager_Leaving"],
    ["PROFESSION", "\"I'm a professional minder of my own business, go away.\"", None, None],
    ["CHILDREN", "\"No I don't have any. Hardly see any about either.\"", "Dialogue_CallID_009a", "children_missing"],
    ["MISSING CHILDREN", "\"I can't recall the last place I saw any.\"", None, "children_gone"],
    ["STUCK IN THE VILLAGE", "\"Something is...\" He stops talking and looks at you with a blank face.",
     "Dialogue_CallID_010b", "leave_the_village"]
]

man2 = [  # Villager
    ["LEAVING", "\"You're welcome to leave... I think. I'm not going to. I can't.\"", "Dialogue_CallID_010a", None],
    ["QUIET", "\"Yes I suppose it is quite quiet here. It often is.\"", None, None],
    ["NOISE", "\"Sometimes I just can't concentrate, it's so LOUD!\"", "Dialogue_CallID_008a", None],
    ["VILLAGE", "\"The village? It's just the village. Full of people.\"", None, None],
    ["MEMORY", "\"You know, I find myself getting muddled lately.\"", None, None],
    ["CHILDREN", "\"What about them? There aren't any, right?\"", "Dialogue_CallID_009b", "children_missing"],
    ["MISSING CHILDREN", "\"You're telling me there *were* children??\"", None, "children_gone"],
    ["STUCK IN THE VILLAGE", "\"You can't go you can't you can't you can't...\"",
     "Dialogue_CallID_010c", "leave_the_village"]
]

man3 = [  # Villager
    ["LEAVING", "\"Sometimes people ask about that.\"", None, None],
    ["VILLAGE NAME", "\"Well this is... Huh. I don't remember. How funny!\"", None, None],
    ["PROFESSION", "\"Well I am a... wait, what am I?\"", None, None],
    ["NOISE", "\"If we keep pretending we can't hear it, maybe it'll stop?\"", "Dialogue_CallID_008i", "village_noise"],
    ["CHILDREN", "\"I saw some just the other day, I'm not sure what you mean..\"", "Dialogue_CallID_009c", "children_missing"],
    ["MISSING CHILDREN", "\"...They seem to be here sometimes, and then they're not.\"", None, "children_gone"],
    ["STUCK IN THE VILLAGE", "\"Stop... stop talking about that...\"",
     "Dialogue_CallID_010d", "leave_the_village"],
    ["PECULIAR HAPPENINGS", "\"Peculiar what now? Who? When? Leave me be youngster.\"",
     None, "elders"],
]

man4 = [  # Blacksmith
    ["AFFAIR", "\"... keep it to yourself and we'll be good friends.\"", None, "village_affair_public"],
    ["LEAVING", "\"Can't see why you'd want to. I certainly don't want to.\"", None, None],
    ["CARPENTER", "\"Can't say I know the man.\"", None, "CWife_Smith"],
    ["CARPENTER'S WIFE", "\"The carpenter's wife? She's friendly enough.\"", None, "CWife_Smith"],
    ["BLADE", "\"What? No you can't have it. That's paid for.\"", None, "BladeSpotted"],
    ["WORK", "\"I've got just enough for myself right now, don't need help nor more work.\"", None, None],
    ["VILLAGE", "\"I can't be bothered to remember the people here. Only one or two.\"", "Dialogue_CallID_005", None],
    ["VILLAGERS", "\"Not going to talk about my private business.\"", "Dialogue_CallID_006", "Smith_Friendly"],
    ["STUCK IN THE VILLAGE", "\"I'm not stuck. I can... I can go... can't I?\"",
     "Dialogue_CallID_010e", "leave_the_village"]
]

man5 = [  # Fisherman
    ["LEAVING", "\"Between you and me...\" He abruptly stops talking.", "Dialogue_CallID_004", "Fisherman_Leaving"],
    ["FISHING", "\"The solitude of the line is a peace quite unlike any other.\"", None, None],
    ["SMELL", "\"Yes, I might have misplaced something. My memory isn't what it used to be.\"", None, None],
    ["LEAVE THE VILLAGE", "\"No I don't remember you asking me any such thing.\"", None, "not_Fisherman_Leaving"],
    ["NOISE", "\"Oh... You hear it too?\"", "Dialogue_CallID_008h", None],
    ["CHILDREN", "\"Kids... yes I'm sure this village used to be full of children.\"",
     "Dialogue_CallID_009d", "children_missing"],
    ["MISSING CHILDREN", "\"Children disappearing? That can't be true.\"", None, "children_gone"],
    ["STUCK IN THE VILLAGE", "\"The village is where we live. The village is home... I can't change that.\"",
     "Dialogue_CallID_010f", "leave_the_village"]
]

man6 = [  # Farmer w/Wife
    ["LEAVING", "\"It's the funniest thing but I'm sure I've heard others saying the same.\"", None, None],
    ["FOOD", "\"Have you eaten? It is getting a bit late, I think.\"", None, None],
    ["FARM", "\"Yes, the majority of the lands outside the village fall to us.\"", None, None],
    ["CHILDREN", "\"Kids? I'm not sure I have kids..\"", "Dialogue_CallID_009e", None],
    ["AFFAIR", "\"Blasphemers. I've no time for what they're doing.\"", "Dialogue_CallID_007a", "affair_rumours"],
    ["NOISE", "\"Now that you mention it... Maybe?\"", "Dialogue_CallID_008c", "village_noise"],
    ["MISSING CHILDREN", "\"Now I'm sure. I definitely have children. Somewhere.\"", None, "children_gone"],
    ["STUCK IN THE VILLAGE", "\"For better or worse, we're stuck here.\"",
     "Dialogue_CallID_010g", "leave_the_village"]
]

man7 = [  # Farmer w/o Wife
    ["LEAVING", "\"Yes, go.\"", None, None],
    ["PRIVACY", "\"You'd do to mind yourself, barging into people's homes like this.\"", None, None],
    ["ANIMALS", "\"Better company than most people.\"", None, None],
    ["FARM", "\"I've got a plot outside the fences, and a few animals inside.\"", None, None],
    ["AFFAIR", "\"That man isn't worth her time. She should come see me.\"", "Dialogue_CallID_007b", "affair_rumours"],
    ["NOISE", "\"Yes, I hear it. Gets on me'bloody nerves it does.\"", "Dialogue_CallID_008d", "village_noise"],
    ["CHILDREN", "\"I have a son, though I'm not sure where he is...\"", "Dialogue_CallID_009f", "children_missing"],
    ["MISSING CHILDREN", "\"I don't care about the rest, just about my son. Where is he?\"", None, "children_gone"],
    ["STUCK IN THE VILLAGE", "\"Something... something is wrong. I can't leave my home.\"",
     "Dialogue_CallID_010h", "leave_the_village"]
]

man8 = [  # Carpenter
    ["LEAVING", "\"There's no point trying to leave the village. I've tried.\"", "Dialogue_CallID_002", "Carp_Leaving"],
    ["WOOD", "\"Not much in the way of trees out here. I have to import most of mine.\"", None, None],
    ["LEAVE THE VILLAGE", "\"What? Leave? Why would I want to do that?.\"", None, "not_Carp_Leaving"],
    ["SMITH", "\"Hmm? We've worked on building jobs together before.\"", None, "Smith_CWife"],
    ["MISSING CHILDREN", "\"My boys? I...\" He suddenly stops, seemingly forgetting he was speaking to you.",
     None, "children_gone"],
    ["STUCK IN THE VILLAGE", "\"The village closed the gates. The village has always been closed.\"",
     "Dialogue_CallID_010i", "leave_the_village"]
]

man9 = [  # Priest
    ["LEAVING", "\"We all leave this earthly coil at some point.\"", None, None],
    ["BLESSINGS", "\"Greetings my child, have you the comfort of faith in your heart?\"", None, None],
    ["AFFAIR", "\"Sinful. Dreadful. But yes, it's a poorly kept secret.\"", "Dialogue_CallID_007c", "affair_rumours"],
    ["NOISE", "\"It is but the buzzing of an idle sinful  mind my child.\"", "Dialogue_CallID_008e", "village_noise"],
    ["CHILDREN", "\"We're all god's children.\"", None, None],
    ["MISSING CHILDREN", "\"Oh dear. I'll pray for them.\"", None, "children_gone"],
    ["STUCK IN THE VILLAGE", "He leans close to whisper. \"Something wicked keeps us here.\"",
     "Dialogue_CallID_011a", "leave_the_village"],
    ["PECULIAR HAPPENINGS",
     "\"...I...I remember something. It's at the edge of my mind but for some reason, I can't quite remember it...\"",
     "Dialogue_CallID_013", "elders"],
    ["MEMORY PROBLEMS",
     "\"In the church's private room. I write things down...I keep books... Let us look there.\"",
     "Dialogue_CallID_013", "priest_memory_problems"],
    ["OTHER VILLAGE",
     "\"What a horrifying tale... I can only hope it fiction.\"",
     None, "final_encounter"],
]

man10 = [  # Alderman
    ["LEAVING", "\"Oh it would be such a shame, but if you don't wish to settle...\"", None, None],
    ["GREETING", "\"Hello, I am the village alderman. I manage disputes and collect our lord's taxes.\"", None, None],
    ["ALDERMAN", "\"A bureaucratic position, mostly, but I do enjoy a certain amount of privilege.\"", None, None],
    ["WIFE", "\"Oh yes, she's lovely. Do talk with her.\"", None, None],
]

woman1 = [  # Villager
    ["LEAVING", "\"You can't leave. What do you mean \'why\'? You just can't. \"", None, None],
    ["WEATHER", "\"It's a bit murky out today.\"", None, None],
    ["AFFAIR", "\"The carpenter's wife and...? One terribly kept secret.\"", "Dialogue_CallID_007d", "affair_rumours"],
    ["MISSING CHILDREN", "\"You'd think people would be more worried about this.\"", None, "children_gone"],
    ["STUCK IN THE VILLAGE", "\"Nobody ever leaves. Nobody wants to. Nobody can.\"",
     "Dialogue_CallID_010j", "leave_the_village"]
]

woman2 = [  # Villager
    ["LEAVING", "\"Why would you want to leave? Nobody should.\"", None, None],
    ["NOISE", "\"Can you hear that? There's a faint buzzing in the air.\"", "Dialogue_CallID_008b", None],
    ["CHILDREN", "\"I know I haven't seen my daughter in a few days... I'm sure she'll turn up.\"",
     "Dialogue_CallID_009d", "children_missing"],
    ["MISSING CHILDREN", "\"*All* the children are missing? How is that possible?\"", None, "children_gone"],
    ["STUCK IN THE VILLAGE", "\"It's so lovely here. I wouldn't leave if I could.\"",
     "Dialogue_CallID_010k", "leave_the_village"]
]

woman3 = [  # Villager
    ["LEAVING", "\"I'm sure you'll change your mind about that, we all do.\"", None, None],
    ["ANIMALS", "\"I'd sure love to get a dog or something.\"", None, None],
    ["NOISE", "\"Sometimes. I don't know where it's coming from though.\"", "Dialogue_CallID_008g", "village_noise"],
    ["CHILDREN", "\"My friend confided in me she hasn't seen her children lately. She didn't seem worried.\"",
     "Dialogue_CallID_009h", None],
    ["STUCK IN THE VILLAGE", "\"Don't try. You'll just find yourself back here.\"",
     "Dialogue_CallID_010l", "leave_the_village"],
    ["PECULIAR HAPPENINGS", "\"Hmm? I don't know anything about these going-ons.\"",
     None, "elders"],
]

woman4 = [  # Basket Weaver
    ["LEAVING", "\"Leave? No I don't think I could, not at my age.\"", None, None],
    ["FAMILY", "\"No I haven't anyone, bit of a spinster I'm afraid.\"", None, None],
    ["AFFAIR", "\"I try not to pay attention to those sorts of rumours.\"", None, "affair_rumours"],
    ["CHILDREN", "\"I have grandchildren but I haven't seen them in a while.\"",
     "Dialogue_CallID_009h", None],
    ["STUCK IN THE VILLAGE", "\"Hmm? No... you're right. This has... this has happened somewhere before....\"",
     "Dialogue_CallID_011b", "leave_the_village"],
    ["PECULIAR HAPPENINGS", "\"...I'm sorry, I can't think... I have books somewhere, just take them...\"",
     "Dialogue_CallID_012", "elders"],
    ["BOOKS", "\"My diary... I... wrote something in my diary...\"",
     None, "basket_weaver_books"]
]

woman5 = [  # Farmer's Wife
    ["LEAVING", "\"You're welcome to leave whenever you like.\"", None, None],
    ["COOKING", "\"If you get in the way I'll clap you round the head with my wooden spoon!\"", None, None],
    ["CHILDREN", "\"They're somewhere around here.\"", None, None],
    ["AFFAIR", "\"Oh, the smith and HER? Yes. I know.\"", "Dialogue_CallID_007e", "affair_rumours"],
    ["STUCK IN THE VILLAGE", "\"Everyone talks of leaving now and again. Nobody can. Nobody does.\"",
     "Dialogue_CallID_010m", "leave_the_village"]
]

woman6 = [  # Carpenter's Wife
    ["LEAVING", "\"What do you mean you can't leave? That doesn't make sense.\"", None, None],
    ["CHILDREN", "\"I haven't seen my children all day. They're always off playing somewhere.\"",
     "Dialogue_CallID_009g", None],
    ["HUSBAND", "\"My husband built most of the homes here, I'm very proud of him.\"", None, None],
    ["INTERESTS", "\"I'm a bit of a charcoal drawer myself, when I have the time and supplies.'\"", None, None],
    ["VILLAGERS", "\"Some are friendly, some less so. Have you met the smith?.\"", "Dialogue_CallID_001", None],
    ["SMITH", "\"Oh, he's quite friendly. I'm sure he'll be able to help you.\"", None, "CWife_Smith"],
    ["AFFAIR", "\"Please go away.\"", "Dialogue_CallID_007f", "affair_rumours"],
    ["STUCK IN THE VILLAGE", "\"There's nothing outside the village for us. We can't go.\"",
     "Dialogue_CallID_010n", "leave_the_village"]
]

woman7 = [  # Alderman's Wife
    ["LEAVING", "\"Yes, yes, just go if you must.\"", None, None],
    ["DUTIES", "\"I'll have you know I have a very busy life.\"", None, None],
    ["ALDERMAN", "\"We've been married for, oh I don't know, a handful of years.\"", None, None],
    ["TAXES", "\"It is the responsibility of all our village citizens to pay their taxes.\"", None, None],
    ["CLOTHES", "\"Yes my garments are of only the highest quality. Only the best.\"", None, None],
    ["VILLAGERS", "\"Who? How should I know who lives here?\"", None, None],
    ["CHILDREN", "\"I... I've seen children... but I forget where...'\"",
     "Dialogue_CallID_009g", None],
    ["AFFAIR", "\"Oh yes... what tripe passes for entertainment here...\"", "Dialogue_CallID_007g", "affair_rumours"],
    ["NOISE", "\"Yes that dreadful thing. My husband doesn't hear it.\"", "Dialogue_CallID_008f", "village_noise"],
]

cow = [  # A cow
    ["MOOOOO", "\"MoooOoooooooOoo\"", "Dialogue_CallID_Cow", None],
    ["MOOOO", "\"MOOOOOO\"", "Dialogue_CallID_Cow", None],
    ["MOOO", "\"Moo Moo...\"", "Dialogue_CallID_Cow", None],
    ["MOO", "\"Moo?\"", "Dialogue_CallID_Cow", None],
]

test_conversation = [
    ["CHIPS", "\"Well, I do like a bit of vinegar on my chips.\"", None, None],
    ["NERDS", "\"Have you heard the tale of FATTY AND THE NERD?\"", None, None],
    ["DROOL", "\"*Slurps up drool*\"", None, None],
    ["SCREAMS", "\"Why do some people scream when walking down the street?\"", None, None],
    ["RADIO", "\"Everyone here has a bit of a head for radio.\"", None, None],
    ["BADMINTON", "\"Everyday in this village is Badminton.\"", None, None],
    ["TEA", "\"Just a light tea.\"", None, "TestGVar"],
    ["FARTS", "\"Smells a bit of farts around here.\"", "Dialogue_CallID_000", None]
]
