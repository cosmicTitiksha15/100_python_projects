# This program is a dice roll simulator...where dice generates random number 1-6 (inclusive)
# | **Beginner** | **Console/CLI** | **6. Dice Rolling Simulator** | `random` module, functions. |

import random

while True:
    random_num = random.randint(1,6)
    print(f"Your generated random number is : {random_num}")
    while True:
        query = input("Wanna roll once more ? (y/n) : ")
        if query.lower() == 'y':
            break # Breaks the inner loop to roll again
        elif query.lower() == 'n':
            exit() # Ends the entire program
        else:
            print(f"Invalid input, please enter (y/n).")