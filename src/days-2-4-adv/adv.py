from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

# room['outside'].n_to = room['foyer']
# room['foyer'].s_to = room['outside']
# room['foyer'].n_to = room['overlook']
# room['foyer'].e_to = room['narrow']
# room['overlook'].s_to = room['foyer']
# room['narrow'].w_to = room['foyer']
# room['narrow'].n_to = room['treasure']
# room['treasure'].s_to = room['narrow']

room['outside'].connectRooms(room['foyer'], "n")
room['foyer'].connectRooms(room['overlook'], "n")
room['foyer'].connectRooms(room['narrow'], "e")
room['narrow'].connectRooms(room['treasure'], "n")

#
# Main
#
#print("Welcome to Game!")
# Make a new player object that is currently in the 'outside' room.
# player = Player(room['outside'])
#print("You are in the %s. %s" % (player.room.name, player.room.description))
# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

# while True:
#     print (f"\n  {player.location.title}\n    {player.location.description}\n" )
#     inp = input("What is your command: ")
#     if inp == "q":
#         break
#     if inp == "n" or inp == "s" or inp == "w" or inp == "e":
#         newRoom = player.location.getRoomInDirection(inp)
#         if newRoom == None:
#             print("You cannot move in that direction")
#         else:
#             player.change_location(newRoom)   

# Game variables
suppressRoomPrint = False

def printErrorString(errorString):
    print(f'\x1b[1;31;40m\n{errorString}\x1b[0m\n')
    global suppressRoomPrint
    suppressRoomPrint = True


# player = Player( input("\nWhat is your name?: ") , room['outside'])
player = Player(room['outside'])
# print (f"Welcome, {player.name}!\n")

validDirections = ["n", "s", "e", "w"]

############
# Command functions
############



def moveCommand(player, *args):
    newRoom = player.location.getRoomInDirection(args[0])
    if newRoom == None:
        printErrorString("You cannot move in that direction!")
    else:
        player.change_location(newRoom)
    return False

def lookCommand(player, *args):
    """
    Returns suppressRoomString value
    """
    if not (args[0] == "l" or args[0] == "look"):
        printErrorString("That is not a look command")
    elif len(args) == 1:
        return False
    elif args[1] in validDirections:
        lookRoom = player.location.getRoomInDirection(args[1])
        if lookRoom is not None:
            print (lookRoom)
        else:
            printErrorString("There is nothing in that direction.")
        return True

commands = {}
commands["n"] = moveCommand
commands["s"] = moveCommand
commands["e"] = moveCommand
commands["w"] = moveCommand
commands["l"] = lookCommand
commands["look"] = lookCommand

commandsHelp = {}
commandsHelp["n"] = "Move North"
commandsHelp["s"] = "Move South"
commandsHelp["e"] = "Move Eath"
commandsHelp["w"] = "Move West"
commandsHelp["l"] = "Look somewhere"
commandsHelp["look"] = "Look somewhere"        

#######
# Util
#######



# Room.connect(<Room>, <direction>)



######
# Start Game loop here
######




while True:
    if suppressRoomPrint:
        suppressRoomPrint = False
    else:
        print (player.location)
    inputList = input(">>> ").split(" ")
    if inputList[0] == "q":
        break
    elif inputList[0] in commands:
        suppressRoomPrint = commands[inputList[0]](player, *inputList)
    elif inputList[0] == "help":
        for command in commandsHelp:
            print (f"{command} - {commandsHelp[command]}")
    else:
        printErrorString("I do not understand that command")