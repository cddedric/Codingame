import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
# ---
# Hint: You can use the debug stream to print initialTX and initialTY, if Thor seems not follow your orders.

# light_x: the X position of the light of power
# light_y: the Y position of the light of power
# initial_tx: Thor's starting X position
# initial_ty: Thor's starting Y position
light_x, light_y, initial_tx, initial_ty = [int(i) for i in input().split()]
tx = initial_tx
ty = initial_ty

# game loop
while True:
    remaining_turns = int(input())  # The remaining amount of turns Thor can move. Do not remove this line.

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)
    
    if light_x > tx:
        #light W
        if light_y > ty:
            print("SE")
            tx += -1
            ty += 1
            continue
        elif light_y < ty:
            print("NE")
            tx += -1
            ty += -1
            continue
        else:
            print("E")
            tx += -1
            continue
    elif light_x < tx:
        #light E
        if light_y > ty:
            print("SW")
            tx += 1
            ty += 1
            continue
        elif light_y < ty:
            print("NW")
            tx += 1
            ty += -1
            continue
        else:
            print("W")
            tx += 1
            continue
    else: #just N or S
        if light_y > ty:
            print("S")
            ty -=1
            continue
        else:
            print("N")
            ty +=1
            continue

    # A single line providing the move to be made: N NE E SE S SW W or NW
#    print("SE")