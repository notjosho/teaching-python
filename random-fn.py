import random

def random_dice_generator(number_of_dice, faces=6):
    if not (isinstance(number_of_dice, int) and number_of_dice > 0):
        raise ValueError("number_of_dice must be a positive integer.")
    if not (isinstance(faces, int) and faces > 0):
        raise ValueError("faces must be a positive integer.")
    
    return [random.randint(1, faces) for _ in range(number_of_dice)]

try:
    num_dice_input = input("Enter the number of dice to roll: ")
    num_faces_input = input("Enter the number of faces per die (press Enter for 6-sided): ")

    number_of_dice = int(num_dice_input)
    faces = int(num_faces_input) if num_faces_input else 6

    results = random_dice_generator(number_of_dice, faces)
    print(f"\nRolling {number_of_dice} dice with {faces} faces each: {results}")

except ValueError as e:
    print(f"\nInvalid input: {e}")
