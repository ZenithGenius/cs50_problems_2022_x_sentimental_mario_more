# Declare height to be 0
from cs50 import get_int
height = 0
# Get height input from user and promt until it qualifies
while(height <= 0 or height > 8):
    height = get_int("Height: ")
# Loop to print pyramids on screen
# Loop to move through rows
for row in range(height):
    # Loop to print Spaces
    for i in range(height - (row + 1)):
        print(" ", end='')
    # Loop to print hashes
    for i in range(row + 1):
        print("#", end='')
    # Print 2 spaces for chasim
    print("  ", end='')
    # Loop to print other side of pyramid
    for i in range(row + 1):
        print("#", end='')
    print("")