# Defines the player

import utils

class Player:
  def __init__(self, place, health=100, inventory=set()):
    self.place = place # Place : Where the player is now
    self.health = health # integer : percent healthy 0-100
    self.inventory = inventory # set of Thing

  def get_place(self):
    return self.place
    
  def get_health(self):
    return self.health

  def print_inventory(self):
    items = []
    for i in self.inventory:
      items.append(i.get_name())
    if len(items) == 0:
      items = ['nothing']
    utils.print_list('You have: ', items)

  def is_alive(self):
    return self.health > 0

  def change_health(self, amount):
    self.health += amount
    if self.health < 0:
      self.health = 0
      print('You died')
    elif self.health > 100:
      self.health = 100
      print('You are completely healed')
    elif amount < 0:
      print(f'Your health decreased by {amount} and is now {self.health}')
    else:
      print(f'Your health increased by {amount} and is now {self.health}')

  def die(self):
    self.health = 0

  # Execute a player command.  Currently that means moving.
  # return True/False depending on whether or not this was a valid command
  def do(self, verb):
    # Check to see if the verb is a passable Path
    connection = self.place.get_connection(verb)
    if connection != None:
      if connection[0].is_passable():
        self.place = connection[1]
      else:
        print(verb, 'is blocked.', connection[0].why_blocked())
      return True
    if verb == 'health':
      print('You are feeling {}% healthy'.format(self.get_health()))
      return True
    return False

  # Look for an item in the player's inventory by name.
  # If found, return the item.
  def get_in_inventory(self, item_name):
    for i in self.inventory:
      if i.get_name() == item_name:
        return i
    return None

  def put_in_inventory(self, item):
    if item != None:
      self.inventory.add(item)
      item.taken(self, self.place)

  def remove_from_inventory(self, item):
    if item in self.inventory:
      self.inventory.remove(item)
      item.dropped(self, self.place)