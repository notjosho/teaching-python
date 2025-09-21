import random

def validate_input(number, name):
    if not (isinstance(number, int) and number > 0):
        raise ValueError(f"'{name}' must be a positive integer.")
    return number

def random_dice_generator(number_of_dice, faces=6):
    try:
        validated_num_dice = validate_input(number_of_dice, "number_of_dice")
        validated_faces = validate_input(faces, "faces")
        return [random.randint(1, validated_faces) for _ in range(validated_num_dice)]
    except (ValueError, TypeError) as e:
        return f"Error: {e}"

# Test cases
print("\n--- Test Cases ---")
print(f"Rolling 1 die with 6 faces: {random_dice_generator(1)}")
print(f"Rolling 2 dice with 8 faces: {random_dice_generator(2, 8)}")
print(f"Rolling 3 dice with 20 faces: {random_dice_generator(3, 20)}")
print(f"Rolling a negative number of dice: {random_dice_generator(-1)}")
print(f"Rolling with a non-integer number of faces: {random_dice_generator(2, 'd6')}")
