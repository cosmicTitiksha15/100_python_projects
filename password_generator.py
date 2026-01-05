# This program is password generator where you could choose number of characters you need in your password and your random password would be ready in a single click.

# | **Beginner** | **Console/CLI** | **5. Password Generator** | `random` and `string` modules, list/string methods. |
import random

while True:
    try:
        query = int(input("How many characters you need in your password : "))
        if query > 0 :
            characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*_+=:;>.<,?ś'
            list_chars = list(characters)
            password = []
            for character in range(query):
                password.append(random.choice(list_chars))
            password = ''.join(password)
            print(password)
            break
        else:
            continue
    except ValueError:
        print(f"Please enter a valid positive integer. Remember more number of characters in your password, more secure it is.")