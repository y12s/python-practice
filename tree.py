
def draw_tree(size):
  # Initialize variables
  spaces = size - 1
  stars = 1
  # Draw each row of the tree
  for i in range(size):
    # Draw the spaces
    for j in range(spaces):
      print(" ", end="")
    # Draw the stars
    for j in range(stars):
      print("*", end="")
    # Move to the next line
    print("")
    # Update the number of spaces and stars for the next row
    spaces -= 1
    stars += 2

# Test the function
draw_tree(5)
