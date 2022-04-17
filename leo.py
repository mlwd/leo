
import leo_lookup
import sys

nargs = len(sys.argv)

if nargs < 2:
  print("Not enough arguments.")
elif nargs > 2:
  print("Too many arguments:")
  sys.exit()

word_en = sys.argv[1]
print("English:", word_en)
word_de = leo_lookup.leo_lookup(word_en)
print("Deutsch:", word_de)
