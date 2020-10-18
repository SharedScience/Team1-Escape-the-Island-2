# Get input from the player and parse it

from path import Door
import utils

# A new command is created every time around the main loop


class Command:
    # Converts input to lower case, splits words into a list
    def __init__(self, player, prompt):
        self.player = player

        raw_input = input(prompt)
        # Convert the input to lower case:
        smooth_input = raw_input.lower()
        # Convert the lower case input into a list:
        self.word_list = smooth_input.split()

        # Are there any words at all?
        # The first word is always the verb
        if len(self.word_list) > 0:
            self.verb = self.word_list[0]
        else:
            self.verb = None

        # Is there a second word?
        # The second word is always a noun
        if len(self.word_list) > 1:
            self.noun = self.word_list[1]
        else:
            self.noun = None

    # Library of game commands
    # These methods handle very high level or generic commands

    # Immediately quit the game
    def quit(self):
        self.player.die()

    # Display the list of valid commands
    def help(self):
        utils.type_quick([
          'Type any of the following command words when needed:',
          'help (gets a list of all the commands you can use  in the game)',
          'quit (ends the game)', 
          'look (gives more details on where you are)',
          'inventory (shows all the objects you have)',
          'health (shows your health)',
          'north, south, east, west (directions you can go)',
          'examine [thing] (gives details about the thing you chose to examine.)',
          'take [thing] (you can pick up a thing)',
          'use [thing] (you can use a thing)',
          'drop [thing] (you can drop a thing)',
          'combine [thing1] [thing2] (you can combine two things to make them work together)',
          'open [direction] (you can open any door that is closed)',
          'close [direction] (you can close any door that is opened)',
          'unlock [direction] with [key] (you can unlock a door that is locked)'
        ])

    # Display the full description of the current location even the player has been there before
    def look(self):
        self.player.get_place().describe(True)

    # List the items currently in the player's inventory
    def inventory(self):
        self.player.print_inventory()

    # If possible, move an item from the current location into the player's inventory
    def take(self):
        if self.noun != None:
            place = self.player.get_place()
            item = place.get_item(self.noun)
            if item != None:
                if item.is_takeable():
                    place.remove_item(item)
                    self.player.put_in_inventory(item)
                    print(f'You picked up the {self.noun}')
                else:
                    print(f"You can't pick {self.noun} up")
            else:
                print(f'There is no {self.noun} here')
        else:
            print(f'Name what you want to take.  Try "take {self.noun}"')

    # If possible, move an item from the player's inventory to the current location
    def drop(self):
        if self.noun != None:
            place = self.player.get_place()
            item = self.player.get_in_inventory(self.noun)
            if item != None:
                self.player.remove_from_inventory(item)
                place.put_item(item)
                print(f'You dropped the {self.noun}')
            else:
                print(f"You aren't carrying a {self.noun}")
        else:
            print('Name what you want to drop')

    # Look for something to open and try to open it
    def open(self):
        if self.noun == None:
            print('What do you want to open? "open [direction]"')
        else:
            connection = self.player.get_place().get_connection(self.noun)
            if connection != None and isinstance(connection[0], Door):
                connection[0].open()
            elif self.noun == 'door':
                print(
                    'Which door do you want to open?  Try "open [direction]"')
            else:
                print('There is no door here', self.noun)

    # Look for something to close and try to close it
    def close(self):
        if self.noun == None:
            print('What do you want to close? Try "close [direction]"')
        else:
            connection = self.player.get_place().get_connection(self.noun)
            if connection != None and isinstance(connection[0], Door):
                connection[0].close()
            elif self.noun == 'door':
                print(
                    'Which door do you want to close?  Try "close [direction]"'
                )
            else:
                print('There is no door here', self.noun)

    # Look for something to unlock and try to unlock it
    def unlock(self):
        if self.noun == None:
            print('What do you want to unlock?')
        else:
            if len(self.word_list) < 4:
                print('What do you want to unlock the {} with?'.format(
                    self.noun))
            else:
                keyname = self.word_list[3]
                key = self.player.get_in_inventory(keyname)
                if key != None:
                    connection = self.player.get_place().get_connection(
                        self.noun)
                    if connection != None and isinstance(connection[0], Door):
                        connection[0].unlock(keyname)
                    elif self.noun == 'door':
                        print(
                            'Which door do you want to open?  Try "unlock [direction] with [key]"'
                        )
                    else:
                        print('There is no door', self.noun)
                else:
                    print("You don't have the", keyname)

    # Display helpful debugging information
    def track(self):
        place = self.player.get_place()
        print('Location:', place.get_name())
        print('Visited:', place.get_visited())
        place.print_contents()
        print('Health:', self.player.get_health())
        self.player.print_inventory()

    # Map between the names of valid commands and the methods that implement them
    commands = {
        'quit': quit,
        'help': help,
        'look': look,
        'inventory': inventory,
        'take': take,
        'drop': drop,
        'open': open,
        'close': close,
        'unlock': unlock,
        'track': track,
    }

    # Validate and execute the command
    def execute(self):
        if self.verb != None:
            # Check for game commands
            if self.verb in self.commands:
                self.commands[self.verb](self)
                return

            # Check to see if this is a player command
            if self.player.do(self.verb):
                return

            # For 2-word commands, check for commands on the thing
            if self.noun != None:
                place = self.player.get_place()
                # check the player's inventory for the item first
                in_inventory = True
                item = self.player.get_in_inventory(self.noun)
                if item == None:
                    # check the current location second
                    in_inventory = False
                    item = place.get_item(self.noun)
                if item != None:
                    # found something, try the command on it
                    item.execute(self.verb, self.word_list, self.player, place,
                                 in_inventory)
                    return
                print('There is no {} here'.format(self.noun))
                return

            print("You can't do that")
