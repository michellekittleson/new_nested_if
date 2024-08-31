# Task 1: Code Correction

place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river? ")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
    # Task 3: Default Path
    else:
        pass
elif place == "cave":
    # Task 2: Setting the Scene
    action = input("light a torch or proceed in the dark? ")
    if action == "light a torch":
        print("Good thing you can see where you're going!")
    elif action == "proceed in the dark":
        print("Careful where you're going!")
    else:
        pass
else:
    pass
