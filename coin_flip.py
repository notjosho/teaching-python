import random

def coin_flip_simulator(number_of_flips=1):
  try:
    if not isinstance(number_of_flips, int):
      raise ValueError('Must be a number')
    if number_of_flips <= 0:
      raise ValueError('Must be positive')
    
    result=[]
    for i in range(number_of_flips):
      flip= random.choice(['heads', 'tails'])
      result.append(flip)
    return result
  
  except ValueError as e:
    print(f'Error": {e}')
    return []
  
print(coin_flip_simulator()) # ["heads"] or ["tails"]
print(coin_flip_simulator(3)) # ["heads", "tails", "heads"] (example)
print(coin_flip_simulator(5)) # list of 5 elements, each "heads" or "tails"
