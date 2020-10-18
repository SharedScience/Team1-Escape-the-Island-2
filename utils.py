# Helpful utilities

# Print a label followed by a comma separated list
def print_list(label, col):
    print(label, end='')
    print(*col, sep=', ')


# Prints *text* to the screen, 
# with a delay between characters of *typewriter_speed* (zero for no delay),
# a pause between paragraphs of *delay_after_paragraph*,
# wrapping text for the terminal width
def typewriter(text, typewriter_speed, delay_after_paragraph):
  import textwrap
  import time
  import random
  import shutil

  columns, rows = shutil.get_terminal_size(fallback=(80, 24))
  if columns > 72:
    columns = 72

  first_paragraph = True

  # For each paragraph (list item):
  for paragraph in text:
    if not first_paragraph:
      print()

    # For each character
    for char in (textwrap.fill(paragraph, width=columns)):
      print(char, end="", flush=True)
      time.sleep(random.uniform(0.0, typewriter_speed))
    print()

    # Add a new line after each paragraph (list item)
    first_paragraph = False

    # Pause before next parapgraph
    time.sleep(delay_after_paragraph)

# Convenience functions for the typewriter effect
def type_quick(text):
  typewriter(text, 0.0, 0.0)

def type_slow(text):
  typewriter(text, 0.10, 0.5)
