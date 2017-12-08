import sys
import math
import string

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

l = int(raw_input())
h = int(raw_input())
t = raw_input()
print >> sys.stderr, "{} {} {}".format(l, h, t)

rows = [raw_input() for x in xrange(h)]
print >> sys.stderr, '\n'.join(rows)

def get_index(character):
    if character.upper() in string.uppercase:
        return string.uppercase.index(character.upper())
    else:
        return 26

letters = [get_index(x) for x in list(t)]


# Write an action using print
# To debug: print >> sys.stderr, "Debug messages..."
def get_letter_row(width, letter, row):
    position = width * letter
    return row[position: position + l]
    
for i in range(h):
    print(''.join([get_letter_row(l, letters[j], rows[i]) for j in range(len(letters))]))
