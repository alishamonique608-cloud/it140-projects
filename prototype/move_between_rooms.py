"""Module Six Milestone starter for the simplified movement prototype."""

# move_between_rooms.py
# Simplified Dragon Text Game
# Allows the player to move between rooms or exit the game.

# Dictionary linking rooms and possible directions
rooms = {
    "Great Hall": {"south": "Bedroom"},
    "Bedroom": {"north": "Great Hall", "east": "Cellar"},
    "Cellar": {"west": "Bedroom"},
}


rooms = {
    'Great Hall': {'south': 'Bedroom'},
    'Bedroom': {'north': 'Great Hall', 'east': 'Cellar'},
    'Cellar': {'west': 'Bedroom'}
}

# Starting room
current_room = 'Great Hall'

# Welcome message
print('Welcome to the Dragon Text Game!')
print('Move commands: go North, go South, go East, go West')
print('Type "exit" to leave the game.\n')

# Gameplay loop
while current_room != 'exit':

    # Display current room
    print(f'You are in the {current_room}')

    # Get player command
    command = input('Enter your move: ').strip().lower()

    # Exit command
    if command == 'exit':
        current_room = 'exit'
        print('Thanks for playing!')

    # Movement command
    elif command.startswith('go '):
        direction = command[3:]  # Get direction after "go "

        # Check if direction is valid for current room
        if direction in rooms[current_room]:
            current_room = rooms[current_room][direction]
        else:
            print('You cannot go that way!')

    # Invalid command
    else:
        print('Invalid command. Use "go north", "go south", '
              '"go east", "go west", or "exit".')
