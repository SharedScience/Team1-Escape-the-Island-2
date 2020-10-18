class Thing:
  def __init__(self, name, description, can_take):
    self.name = name # string : one word name
    self.description = description # string : full description
    self.can_take = can_take # Boolean : thing can be picked up
    self.commands = {
      'examine': self.examine,
      'use': self.use,
      'combine': self.combine
    }

  def get_name(self):
    return self.name

  def is_takeable(self):
    return self.can_take
  
  def add_command(self, command):
    self.commands.add(command)

  def replace_command(self, command, method):
    self.commands[command] = method

  def examine(self, word_list, player, place, in_inventory):
    print(self.description)

  def use(self, word_list, player, place, in_inventory):
    print('nothing happens')

  def combine(self, word_list, player, place, in_inventory):
    print('nothing happens')

  def execute(self, verb, word_list, player, place, in_inventory):
    # print('command:', verb, self.name)
    if verb in self.commands:
      self.commands[verb](word_list, player, place, in_inventory)
    else:
      print(f"You can't {verb} the {self.name}")

  def combine_things(self, word_list, player, in_inventory, valid_others):
    if not in_inventory:
      print("You're not holding the", self.get_name())
    elif len(word_list) < 3:
      print('Combine the {} with what?'.format(self.get_name()))
    else:
      othername = word_list[2]
      other = player.get_in_inventory(othername)
      if other == None:
        print("You're not holding the", othername)
      elif other.get_name() in valid_others:
        return other
    return None

  def use_together(self, word_list, player, in_inventory, valid_others):
    if not in_inventory:
      print("You're not holding the", self.get_name())
    elif len(word_list) < 3:
      print(f'Use the {self.get_name()} with what?')
    else:
      othername = word_list[2]
      other = player.get_in_inventory(othername)
      if other != None and other.get_name() in valid_others:
        return other
      other = player.get_place().get_item(othername)
      
      if other != None and other.get_name() in valid_others:   
        return other
      
      other = player.get_place().get_connection(othername)
      if other != None and other[0].get_name() in valid_others:
        return other[0]
      print(f"You're not holding the {othername}")
    return None

  # Called when a thing is added to the player's inventory
  def taken(self, player, place):
    pass

  # Called when a thing is removed from the player's inventory
  def dropped(self, player, place):
    pass