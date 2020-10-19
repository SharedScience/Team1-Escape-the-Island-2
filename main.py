# testing gitignore

# The game starts here.  This is the home of the main game loop.

from command import Command
from player import Player
import map
import utils

# Startup by initializing the world
player = Player(map.start);

# Display the introduction to the story
utils.type_slow([
  'You wake up and dont know where you are.', 
  "You have no idea how you got here and no idea what's going on.", 
  'You see water all around you so you guess you are on an island.', 
  'Instructions- type help to see all of the commands that you can use.', 
  'You can only type commands when > is shown.', 
  'Good luck escaping the Island!'
  ])
print()
ready = input('Are you ready? ')
if(ready == 'no'):
  print("I think you can do this so let's get going")
print()

# Loop untib   l the end condition is met
while (player.is_alive()):
  # Describe the current place and do any actions
  place = player.get_place()
  place.describe()
  place.action(player)
  if player.is_alive():
    # prompt for command
    command = Command(player, "> ")

    # execute command
    try:
      command.execute()
    except:
      print('Something went wrong')
      raise # re-raise the exception so you can see the stack dump and debug it.

  # whitespace between turns
  print()

# game over
utils.type_slow(['Game Over', 'Thanks for playing!']) 