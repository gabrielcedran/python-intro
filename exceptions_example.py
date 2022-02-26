
try:
  int('a')
except ValueError as e:
  print("ops, you can't do that:", e)

print("End of the program reached.")