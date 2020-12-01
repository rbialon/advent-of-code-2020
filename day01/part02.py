with open("input.txt") as f:
  input = list(map(int, f.readlines()))

found = False

for x in sorted(input, reverse=True):
  for y in sorted(input, reverse=True):
    for z in sorted(input):
      if x == y or x == z or y == z:
        continue

      elif x + y + z == 2020:
        print(f"Found {x}, {y} and {z}, result: {x * y * z}")
        found = True
      
      elif x + y + z > 2020:
        break

    if found:
      break

  if found:
    break