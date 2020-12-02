with open("input.txt") as f:
  input = list(map(int, f.readlines()))

found = False
sorted_input = sorted(input)

for x in sorted(input, reverse=True):
  for y in sorted_input:
    if x == y:
      continue

    elif x + y == 2020:
      print(f"Found {x} and {y}, result: {x * y}")
      found = True
    
    elif x + y > 2020:
      break

  if found:
    break