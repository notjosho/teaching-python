import random

def coin_flip_simulator(number_of_flips=1):
  try:
    validated_number_of_flips = validation(number_of_flips)
    result=[]
    for i in range(validated_number_of_flips):
      flip= random.choice(['heads', 'tails'])
      result.append(flip)
    return result
  
  except ValueError as e:
    print(f'Error": {e}')
    return []
  
def validation(number_of_flips):
  if not isinstance(number_of_flips, int):
    raise ValueError(f'"{number_of_flips}" Must be a number')
  if number_of_flips <= 0:
    raise ValueError(f'"{number_of_flips}"Must be positive')
  return number_of_flips
  
print(coin_flip_simulator()) # ["heads"] or ["tails"]
print(coin_flip_simulator(3)) # ["heads", "tails", "heads"] (example)
print(coin_flip_simulator(5)) # list of 5 elements, each "heads" or "tails"
