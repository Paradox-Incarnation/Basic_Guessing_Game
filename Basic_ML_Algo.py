import random
import json
import os

filename = "Python/Machine Learning/human-guesses-dataset.json"
if os.path.exists(filename):
    with open(filename, "r") as file:
        Dict = json.load(file)
else:
    Dict = []

number_data = {str(i): 0 for i in range(1, 11)}
for entry in Dict:
    guess = str(entry["guess"])
    number_data[guess] += 1
sorted_numbers = sorted(number_data.items(), key=lambda x: x[1], reverse=True)
guess_list = [int(num) for num, _ in sorted_numbers]

print("I'm a basic ML algorithm")
print("I can guess your number in 3 tries!!")
print("Think of a number between 1 and 10")
print("Press Enter when you are ready")
input()

guessed_correctly = False
for i in range(3):
        print(f"Is your number {guess_list[0]}?")
        print("If yes, type 'yes' else type 'no'")
        response = input()
        if response.lower() == 'yes':
            print("I guessed it right!!")
            Dict.append({"participant_id": len(Dict) + 1, "guess": guess_list[0]})
            guessed_correctly = True
            break
        elif response.lower()=="q":
            guessed_correctly=True
            break
        else:
            for i in range(len(Dict)):
                if Dict[i]["guess"] == guess_list[0]:
                    Dict.pop(i)
                    break
            guess_list.pop(0)

if not guessed_correctly:
    actual_number = input("Enter the number you thought of: ")
    Dict.append({"participant_id": len(Dict) + 1, "guess": int(actual_number)})

with open(filename, "w") as file:
    json.dump(Dict, file, indent=4)