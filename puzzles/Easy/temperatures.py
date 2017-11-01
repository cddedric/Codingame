import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

listerino = []
minimum = 5526

n = int(input())  # the number of temperatures to analyse
for i in input().split():
    # t: a temperature expressed as an integer ranging from -273 to 5526
    t = int(i)
    listerino.append(t)
# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

if listerino != []:    
    minimum = min(listerino, key=abs)
    if abs(minimum) in listerino:
        minimum = abs(minimum)

if listerino == []:
    print("0")
    
else:
    print(minimum)