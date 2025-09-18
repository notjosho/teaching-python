import random

def _validate_input(number, name):
    if not (isinstance(number, int) and number > 0):
        raise ValueError(f"'{name}' must be a positive integer.")
    return number

def random_dice_generator(number_of_dice, faces=6):
    try:
        validated_num_dice = _validate_input(number_of_dice, "number_of_dice")
        validated_faces = _validate_input(faces, "faces")
        return [random.randint(1, validated_faces) for _ in range(validated_num_dice)]
    except ValueError as e:
        print(f"Error: {e} You provided: {number_of_dice} for 'number_of_dice' and {faces} for 'faces'.")
        return []

if __name__ == '__main__':
    while True:
        # Loop for number of dice
        while True:
            try:
                num_dice_input = input("Enter the number of dice to roll: ")
                number_of_dice = int(num_dice_input)
                break
            except ValueError:
                print("Invalid input. Please enter a number.")

        # Loop for number of faces
        while True:
            try:
                num_faces_input = input("Enter the number of faces per die (press Enter for 6-sided): ")
                if num_faces_input:
                    faces = int(num_faces_input)
                else:
                    faces = 6
                break
            except ValueError:
                print("Invalid input. Please enter a number.")

        results = random_dice_generator(number_of_dice, faces)
        if results:
            print(f"\nRolling {number_of_dice} dice with {faces} faces each: {results}")

        keep_rolling = input("\nPress Enter to roll again or 'q' to exit: ")
        if keep_rolling.lower() == 'q':
            break
