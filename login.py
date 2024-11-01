"""
Main drive module.
"""

from helper import sign_in, create_account, exit_program


print("______________________________")
print("     A Simple Login System   ")
print("******************************")
print()

print("1. Login")
print("2. Create account")
print("3. Exit")
choice = input("Please choose 1, 2, or 3: ")
while choice not in ["1", "2", "3"]:
    print("")
    print(f"Incorrect input: {choice}. Please try again...")
    choice = input("Please choose 1, 2, or 3: ")
choice = int(choice)


match choice:
    case 1:
        sign_in()
    case 2:
        create_account()
    case 3:
        exit_program()
    case _:
        print("Invalid choice")
