# all the functional objects in the game

from thing import Thing
# Use the example of Flashlight and Battery to see how to add behaviors.

# The Flashlight starts out dead.  It needs a new battery.
# The Flashlight needs to know if it is dead, off, or on.  This is called 'state'.
class Flashlight(Thing):
  def __init__(self):
    # Call the init of the base Thing to set the name and description
    super().__init__('flashlight', 'an old flashlight', True)
    self.state = 'dead' # start out dead

  # What happens when we 'use' the Flashlight depends on its state.
  # This dictionary lists what to print and the new state.
  # Examples:
  #  - If you use a dead Flashlight, it stays dead
  #  - If you use a good Flashlight, it will toggle on and off
  on_use = {
    'dead': ('The flashlight is dead', 'dead'),
    'off': ('You turned the flashlight on', 'on'),
    'on': ('You turned the flashlight off', 'off')
  }

  # When we examine the Flashlight, describe it, but also show what state it's in
  def examine(self, word_list, player, place, in_inventory):
    print(self.description)
    print('The flashlight is', self.state)

  # When we use the Flashlight, make sure we're holding it first.
  # Then use the on_use dictionary to figure out what happens.
  def use(self, word_list, player, place, in_inventory):
    if not in_inventory:
      print("You're not holding the flashlight pick it up by typing [Take flashlight]. ")
    else:
      action = self.on_use[self.state]
      print(action[0])
      self.state = action[1]

  # When we combine the Flashlight with something else, make sure that's a legal action.
  # The only thing we can combine the Flashlight with is the battery.
  # If the other thing is the battery, then make the Flashlight work and hide the battery.
  def combine(self, word_list, player, place, in_inventory):
    other = self.combine_things(word_list, player, in_inventory, {'battery'})
    if other != None:
      self.new_battery()
      player.remove_from_inventory(other)

  # When putting a battery in the Flashlight, it changes from dead to off.
  # This is used when changing a dead Flashlight into a working one.
  def new_battery(self):
    print('You put a fresh battery in the flashlight')
    self.state = 'off'


# A Battery is a mostly non-functional object.
# We could have gotten away with just a plain thing named 'battery',
# but we want to allow combining with the Flashlight even if the battery is listed first.
# We want both of these things to work:
# - combine flashlight battery
# - combine battery flashlight
class Battery(Thing):
  def __init__(self):
    # Call the init of the base Thing to set the name and description
    super().__init__('battery', 'a new battery', True)
  
  # This combine is very much like the one in Flashlight, but self and other are swapped
  def combine(self, word_list, player, place, in_inventory):
    other = self.combine_things(word_list, player, in_inventory, {'flashlight'})
    if other != None:
      other.new_battery()
      player.remove_from_inventory(self)

class Water(Thing):
  def __init__(self):
    # Call the init of the base Thing to set the name and description
    super().__init__('water', 'lots of water from the ocean',False)
  
  # This combine is very much like the one in Flashlight, but self and other are swapped
  def combine(self, word_list, player, place, in_inventory):
    other = self.combine_things(word_list, player,
    in_inventory, {'waterfilter', 'bucket'})
    
    if other != None:
      other.add_water()

class Sailboat(Thing):
  def __init__(self):
    # Call the init of the base Thing to set the name and description
    super().__init__('sailboat', 'a sailboat',False)
    self.state = 'without a sail' # start out dead

  # What happens when we 'use' the Flashlight depends on its state.
  # This dictionary lists what to print and the new state.
  # Examples:
  #  - If you use a dead Flashlight, it stays dead
  #  - If you use a good Flashlight, it will toggle on and off
  on_use = {
    'without a sail': ("The sailboat doesn't have a sail yet. combine it with the sail by typing [combine sail with sailboat]", 'without a sail'),
    
    'with a sail': ('You started sailing', 'with a sail')
  }

  # When we examine the Flashlight, describe it, but also show what state it's in
  def examine(self, word_list, player, place, in_inventory):
    print(self.description)
    print('The sailboat is', self.state)

  # When we use the Flashlight, make sure we're holding it first.
  # Then use the on_use dictionary to figure out what happens.
  def use(self, word_list, player, place, in_inventory):
    action = self.on_use[self.state]
    print(action[0])
    self.state = action[1]
    
  def combine(self, word_list,  player, place, in_inventory):
    other = self.combine_things(word_list, player, in_inventory,  {'sheet'})
    if other != None:
      self.new_sail()
      player.remove_from_inventory(other)
  
  def new_sail(self):
    print('You attached the sail to the sailboat')
    self.state = 'with a sail'



class Sheet(Thing):
  def __init__(self):
    # Call the init of the base Thing to set the name and description
    super().__init__('sheet', 'a plain white sheet', True)
  
  
  def combine(self, word_list, player, place, in_inventory):
    other = self.combine_things(word_list, player, in_inventory, {'sailboat'})
    if other != None:
      other.new_sail()
      player.remove_from_inventory(self)


class Scissor(Thing):
  def __init__(self):
    # Call the init of the base Thing to set the name and description
    super().__init__('scissor', 'a sharp scissor', True)
    self.state = 'unused' # start out dead

  on_use = {
    'unused': ('You used the scissors to cut the sheet and .', 'unused'),
 }

  # When we examine the Flashlight, describe it, but also show what state it's in
  def examine(self, word_list, player, place, in_inventory):
    print(self.description)
    print('The scissor is', self.state)

  # When we use the Flashlight, make sure we're holding it first.
  # Then use the on_use dictionary to figure out what happens.
  def use(self, word_list, player, place, in_inventory):
    if not in_inventory:
      print("You're not holding the scissor. Try [take scissor]")
    else:
      action = self.on_use[self.state]
      print(action[0])
      self.state = action[1]


class Waterfilter(Thing):
  def __init__(self):
    # Call the init of the base Thing to set the name and description
    super().__init__('waterfilter', 'a small plant waterfilter', True)
    self.state = 'empty' # start out dead

  # What happens when we 'use' the Flashlight depends on its state.
  # This dictionary lists what to print and the new state.
  # Examples:
  #  - If you use a dead Flashlight, it stays dead
  #  - If you use a good Flashlight, it will toggle on and off
  on_use = {
    'empty': ('The waterfilter is empty. Fill it up by combining it with water', 'empty'),
    'full': ('You drank the water.', 'empty'),
    }

  # When we examine the Flashlight, describe it, but also show what state it's in
  def examine(self, word_list, player, place, in_inventory):
    print(self.description)
    print('The waterfilter is', self.state)

  # When we use the Flashlight, make sure we're holding it first.
  # Then use the on_use dictionary to figure out what happens.
  def use(self, word_list, player, place, in_inventory):
    if not in_inventory:
      print("You're not holding the waterfilter pick it up by typing [Take waterfilter]. ")
    else:
      action = self.on_use[self.state]
      print(action[0])
      self.state = action[1]

  # When we combine the Flashlight with something else, make sure that's a legal action.
  # The only thing we can combine the Flashlight with is the battery.
  # If the other thing is the battery, then make the Flashlight work and hide the battery.
  def combine(self, word_list, player, place, in_inventory):
    other = self.combine_things(word_list, player, in_inventory, {'water'})
    if other != None:
      self.new_water()
      player.remove_from_inventory(other)

  # When putting a battery in the Flashlight, it changes from dead to off.
  # This is used when changing a dead Flashlight into a working one.
  def new_water(self):
    print('You poured water into the waterfilter. Now the water is clean.')
    self.state = 'full'



class Bucket(Thing):
  def __init__(self):
    # Call the init of the base Thing to set the name and description
    super().__init__('bucket', 'a bucket with a broken handle', True)
    self.state = 'empty' # start out dead

  # What happens when we 'use' the Flashlight depends on its state.
  # This dictionary lists what to print and the new state.
  # Examples:
  #  - If you use a dead Flashlight, it stays dead
  #  - If you use a good Flashlight, it will toggle on and off
  on_use = {
    'empty': ('The bucket is empty fill it up by combining it with water.', 'empty'),
    'full': ('You emptied the bucket.  Now your feet are wet.', 'empty'),
    }

  # When we examine the Flashlight, describe it, but also show what state it's in
  def examine(self, word_list, player, place, in_inventory):
    print(self.description)
    print('The bucket is', self.state)

  # When we use the Flashlight, make sure we're holding it first.
  # Then use the on_use dictionary to figure out what happens.
  def use(self, word_list, player, place, in_inventory):
    if not in_inventory:
      print("You're not holding the bucket. Pick it up by typing [take bucket]. ")
    elif len(word_list) == 3:
      other = self.use_together(word_list, player, in_inventory, {'fire'})
      if other != None:
        other.put_out()
        self.state = 'empty'
    else:
      action = self.on_use[self.state]
      print(action[0])
      self.state = action[1]

  # When we combine the Flashlight with something else, make sure that's a legal action.
  # The only thing we can combine the Flashlight with is the battery.
  # If the other thing is the battery, then make the Flashlight work and hide the battery.
  def combine(self, word_list, player, place, in_inventory):
    other = self.combine_things(word_list, player, in_inventory, {'water'})
    if other != None:
      self.new_water()
      player.remove_from_inventory(other)
  # When putting a battery in the Flashlight, it changes from dead to off.
  # This is used when changing a dead Flashlight into a working one.
  def new_water(self):
    print('You poured the water into the bucket')
    self.state = 'full'


class Person(Thing):
  def __init__(self):
    # Call the init of the base Thing to set the name and description
    super().__init__('a person', 'a person sleeping in a bed without a shirt on with a knife next to them with blood', False)

  def examine(self, word_list, player, place, in_inventory):
    print(self.description)


class Lava(Thing):
  def __init__(self):
    super().__init__('lava', 'hot lava', True)

  # Called when a thing is added to the player's inventory
  def taken(self, player, place):
    player.change_health(-101)

