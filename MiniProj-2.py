import random

print("\n\n\n \t \t \t \t \t\t \tWelcome to this guessing game \n \n")

ans = random.randrange(1, 10)

print("\t \t \t \t \t\t \tThe numbers is between 1 & 10\n\n")

c = 5

num_of_chances = 5

for i in range(1, 6):
    inp = int(input("Enter the answer you think that is correct : "))
    if inp == ans:
        print(f"\n\nCongo!, You won the game, no. of chances took - {5-(c-1)}\n\n")
        break

    elif c == 1:
        print(f"\n\nYou loose the game !!, the correct answer was {ans}\n\n")
        break

    else:
        print(f"Try again, no. of chances left - {num_of_chances-i} \n")
        if ans <= 5 and i == 1:
            print("Answer is between 1 & 5")
        elif ans > 5 and i == 1:
            print("Answer is between 5 & 10")
        elif ans <= 5 and i == 2:
            print(f"Answer is between {ans-(random.randrange(1, 2))} & 5")
        elif ans > 5 and i == 2:
            print(f"Answer is between {ans-(random.randrange(1, 2))} & 10")
        elif ans <= 5 and i == 3:
            print(f"Answer is between {ans-(random.randrange(1, 2))} & {ans+(random.randrange(1, 2))}")
        elif ans > 5 and i == 3:
            print(f"Answer is between {ans-(random.randrange(1, 2))} & {ans+(random.randrange(1, 2))}")
        elif ans <= 5 and i == 4:
            print("Enough hints are given now, u shoudld be able to solve it !!")
        elif ans > 5 and i == 4:
            print("Enough hints are given now, u shoudld be able to solve it !!")
        elif ans <= 5 and i == 5:
            print("u r really a dumb, not able to even solve it at this movement !!!!!!!")
        elif ans > 5 and i == 5:
            print("u r really a dumb, not able to even solve it at this movement !!!!!!!")


    c = c-1
