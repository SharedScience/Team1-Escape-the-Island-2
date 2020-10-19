# classes for paths between Places

# A regular Path is always passable
class Path:
  def get_name(self):
    return 'path'
  
  def is_passable(self):
    return True

  def why_blocked(self):
    return 'not blocked'


class Fire(Path):
  def __init__(self, is_burning=True):
    self.is_burning = is_burning # Boolean : True when fire is burning
    
  def get_name(self):
    if self.is_burning:
      return 'fire'
    else:
      return 'path'

  def is_passable(self):
    return not self.is_burning 

  def why_blocked(self):
    if self.is_burning:
      return 'The fire is blocking the path. Use water to put out the fire.'
    else:
      return 'The fire is not blocking the path.'
  
  def put_out(self):
    print('You put out the fire')
    self.is_burning = False


class Door(Path):
  def __init__(self, name='door', is_open=False, is_locked=False, key=None):
    self.name = name
    self.is_open = is_open # Boolean : True when door is open
    self.is_locked = is_locked # Boolean : True when door is locked
    self.key = key # string : the correct key for this door

  def get_name(self):
    if self.is_locked:
      return f'locked {self.name}'
    elif self.is_open:
      return f'open {self.name}'
    else:
      return f'{self.name} locked'

  def is_passable(self):
    return self.is_open

  def why_blocked(self):
    if self.is_locked:
      return f'The {self.name} is locked. Use the {self.key} to unlock the {self.name}.'
    elif self.is_open:
      return f'The {self.name} is open.'
    else:
      return f'The {self.name} is closed. Open it first by typing "open direction".'

  def open(self):
    if not self.is_locked:
      self.is_open = True
      print(f'{self.name} opened now you can go inside by typing "direction"')
    else:
      print(self.why_blocked())

  def close(self):
    self.is_open = False
    print(f'You closed the {self.name}. Open it next time you want to go inside by typing "open direction" ')

  def unlock(self, key):
    if self.key == key:
      self.is_locked = False
      print(f'You unlocked the {self.name} now you can open it by typing "open direction"')
    else:
      print('Wrong key. Try again')

# Connect two places together
# One Path will exist between two Places
# - first place
# - direction player will leave first Place
# - Path connecting the Places
# - direction player will leave second Place
# - second place
def connect(place1, direction1, path, direction2, place2):
  place1.add_connection(direction1, place2, path)
  place2.add_connection(direction2, place1, path)

   