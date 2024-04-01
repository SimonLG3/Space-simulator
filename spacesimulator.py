import random

print("Welcome to Space Simulator! Firstly, what is your name?")
print()
name = input("> ")
print()
print("Welcome aboard " + name + "! Below are the list of commands you can use.")


# List of commands a user can use
print("""
start - start the simulation
land - land on the nearest planet
explore - explore the area you're in
launch - launch yourself back into space after landing on a planet
quit - exit the application
help - display this screen again
""")

started = False
landed = False
launched = False
explored = False

while True:
    command = input("> ").lower()
    if command == "start":
        if started:
            print("You have already started!")
        else:
            started = True
            launched = True
            print("Prepare for launch... we have blast off! Let's try landing on a planet now.")

    elif command == "land":
        launched = False
        if not started:
            print("You haven't started yet!")
        elif landed:
            print("You have already landed!")
        else:
            landed = True
            print("You land on " + random.choice(["Mercury", "Venus", "Mars",
                                                  "Earth", "Saturn", "Jupiter",
                                                  "Neptune", "Uranus", "Pluto"]))

    elif command == "launch":
        if not started:
            print("You haven't started yet!")
        elif launched:
            print("You are already travelling through space!")
        else:
            launched = True
            landed = False
            print("You launch yourself into space!")

    elif command == "explore":
        if not started:
            print("You haven't started yet!")
        elif not landed:
            print("You explore the spacecraft...")
            print()
            print(random.choice(["You don't find anything of interest",
                                 "You find an alien onboard!",
                                 "You find an astronaut's helmet!",
                                 "You find a bottle of water!",
                                 "You find an empty cup!"]))
        elif explored:
            explored = True
            print("It looks like there is nothing else to see around here.")
        else:
            print("You begin exploring the surface of the planet...")
            print(random.choice(["You find some strange looking rocks.",
                                 "You stumble across a crater!",
                                 "You find an abandoned UFO!",
                                 "You find a local alien!",
                                 "You come across a fellow astronaut from another voyage!"]))

    elif command == "help":
        print("""
start - start the simulation
land - land on the nearest planet
launch - launch yourself back into space after landing on a planet
explore - explore the surface of the planet you're on
quit - exit the application
""")

    elif command == "quit":
        print("Simulation has ended. " + name + " signing out.")
        break
    else:
        print("Invalid command")
