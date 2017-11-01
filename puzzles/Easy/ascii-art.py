import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

l = int(input())
h = int(input())
t = input()

printable = [str(input()) for i in range(h)]
#for i in range(h):
#    row = input()

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

for i in range(h):
    for letter in t:
        if letter >= 'a' and letter <= 'z':
            start = ord(letter) - ord('a')  #using unicode value to get index
        elif letter >= 'A' and letter <= 'Z':
            start = ord(letter) - ord('A')
        else:
            start = ord('z') - ord('a') +1 #letter out of range, getting index of "?"
            
        for j in range(l):
            print(printable[i][start * l + j], end="")  #prints line of asterisks per letter on each row
            
    print("") #forces a newline for next row
        
#print("answer")