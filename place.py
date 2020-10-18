import utils

# Defines the class of places
class Place:
  def __init__(self, name, weather, hear, smell, contents):
    self.name = name # string : short name for this Place
    self.weather = weather
    self.hear = hear
    self.smell = smell
    self.connections = dict()
    self.contents = contents
    self.visited = False # Boolean : has the player been here before?
  
  def get_name(self):
    return self.name

  def get_weather(self):
    return self.weather
  
  def get_hear(self):
    return self.hear
  
  def get_smell(self):
    return self.smell
  
  def get_visited(self):
    return self.visited
  
  def get_contents(self):
    return self.contents

  def contains(self, item):
    return item in self.contents

  def add_connection(self, direction, place, path):
    self.connections[direction] = (path, place)

  def print_contents(self):
    if len(self.contents) > 0:
      items = []
      for i in self.contents:
        items.append(i.get_name())
      utils.print_list('You look around and can see: ', items)
  
  def get_path_names(self):
    names = []
    for direction, connection in self.connections.items():
      names.append('{} {}'.format(connection[0].get_name(), direction))
    return names

  def get_connection(self, name):
    return self.connections.get(name)

  # Describe this place
  def describe(self, force_describe = False):
    typer = (utils.type_quick if self.visited else utils.type_slow)
    typer(['You are in ' + self.name])
    if force_describe or not self.visited:
      typer([self.weather])
      typer([self.hear])
      typer([self.smell])
      self.print_contents()
      utils.print_list('You can go: ', self.get_path_names())
      self.visited = True

  # Lookup an item by name in this Place.
  # return the item if it's here.
  def get_item(self, item_name):
    for i in self.contents:
      if i.get_name() == item_name:
        return i;
    return None

  def remove_item(self, item):
    if item in self.contents:
      self.contents.remove(item)

  def put_item(self, item):
    if item != None:
      self.contents

  # An action that occurs every turn the player is in this place
  def action(self, player):
    pass


# A type of place that hurts the player every turn they stay there
class HarmfulPlace(Place):
  def __init__(self, name, weather, hear, smell, contents, damage):
    super().__init__(name, weather, hear, smell, contents)
    self.damage = damage

  def action(self, player):
    player.change_health(self.damage)
