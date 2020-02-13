# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, player_name, starting_room, inventory):
        self.player_name = player_name
        self.current_room = starting_room
        self.inventory = inventory
    def travel(self, direction):
        next_room = getattr(self.current_room, f"{direction}_to")
        if next_room is not None:
            self.current_room = next_room
            print(self.current_room)
        else:
            print("\npath blocked try another direction")