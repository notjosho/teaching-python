import random


# Dice Roller
def validate_input(number, name):
    if not (isinstance(number, int) and number > 0):
        raise ValueError(f"'{name}' must be a positive integer.")
    return number

def random_dice_generator(number_of_dice, faces=6):
    try:
        validated_num_dice = validate_input(number_of_dice, "number_of_dice")
        validated_faces = validate_input(faces, "faces")
        # The next line of code which is a list comprehension works in the following way:
        # the square brackets tells the program that it'll be a list
        # "random.randint(1, validated_faces)" this part calls the randint function from the random module
        # it then generates a random integer which will be a number between 1 and the value of "validated_faces"
        # "for _ in range(validated_num_dice)" this part sets up the loop needed for the amount of die
        # "range(validated_num_dice)" creates a range of numbers from 0 up to the "validated_num_dice" 
        # the "for _ in" the underscore means we just want to repeat the action a certain number of times aka "validated_num_dice"
        return [random.randint(1, validated_faces) for _ in range(validated_num_dice)]
    except (ValueError, TypeError) as e:
        return f"Error: {e}"

# Coin Flip
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
  

# Test cases random dice generator
print("\n--- Test Cases Dice Roller ---")
print(f"Rolling 1 die with 6 faces: {random_dice_generator(1)}")
print(f"Rolling 2 dice with 8 faces: {random_dice_generator(2, 8)}")
print(f"Rolling 3 dice with 20 faces: {random_dice_generator(3, 20)}")
print(f"Rolling a negative number of dice: {random_dice_generator(-1)}")
print(f"Rolling with a non-integer number of faces: {random_dice_generator(2, 'd6')}")

# Test cases coin flip
print("\n--- Test Cases Coin Flip ---")
print(coin_flip_simulator()) # ["heads"] or ["tails"]
print(coin_flip_simulator(3)) # ["heads", "tails", "heads"] (example)
print(coin_flip_simulator(5)) # list of 5 elements, each "heads" or "tails"