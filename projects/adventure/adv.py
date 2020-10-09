from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']

traversal_path = []

#store direction/move ad current room as variables
#transversl graph initial entry:  0: {'n': '?', 's': '?', 'w': '?', 'e': '?'}
#pick random direction to move ('move') set 'current_room_temp' to 'current room'

# TRAVERSAL 
# #while you haven't explore all paths
# player.travel(move) - store move to traversal_path
#add dict entry for room, filling based on prev location
# if dead end; travel to next open path. (dfs)
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)
last_move = ''
next_move = ''

#set first move as east
next_move = 'e'
traversal_path.append(next_move)

# Loop until all rooms have been visited
while len(visited_rooms) < 500:
    # We move in the chosen dir. and add the room to our visited set
    player.travel(next_move)
    visited_rooms.add(player.current_room)
    # rooms_been.append(player.current_room.id)

    last_move = next_move

    # Can layout instructions for moving from east, to north, west and south
    # Each move direction can draw from available exits/doors
    if last_move == 'e':
        if 's' in player.current_room.get_exits():
            next_move = 's'
        elif 'e' in player.current_room.get_exits():
            next_move = 'e'
        elif 'n' in player.current_room.get_exits():
            next_move = 'n'
        else:
            next_move = 'w'

    elif last_move == 'n':
        if 'e' in player.current_room.get_exits():
            next_move = 'e'
        elif 'n' in player.current_room.get_exits():
            next_move = 'n'
        elif 'w' in player.current_room.get_exits():
            next_move = 'w'
        else:
            next_move = 's'

    elif last_move == 'w':
        if 'n' in player.current_room.get_exits():
            next_move = 'n'
        elif 'w' in player.current_room.get_exits():
            next_move = 'w'
        elif 's' in player.current_room.get_exits():
            next_move = 's'
        else:
            next_move = 'e'

    elif last_move == 's':
        if 'w' in player.current_room.get_exits():
            next_move = 'w'
        elif 's' in player.current_room.get_exits():
            next_move = 's'
        elif 'e' in player.current_room.get_exits():
            next_move = 'e'
        else:
            next_move = 'n'

    # Got stuck in loop -> add measures to make sure each path gets traversed
    if len(player.current_room.get_exits()) == 4:
        current = player.current_room

# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")
