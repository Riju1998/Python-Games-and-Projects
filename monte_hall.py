import random

doors = [0] * 3
goatdoor = [0] * 2
swap = 0  # No of swap wins
dont_swap = 0  # No of don't swap wins
j = 0
n = int(input("Enter the number of times you want to play: "))
while j < n:
    x = random.randint(0, 2)  # xth door will comprise of BMW
    doors[x] = "BMW"
    for i in range(0, 3):
        if i == x:
            continue
        else:
            doors[i] = "Goat"
            goatdoor.append(i)

    choice = int(input("Enter your choice"))
    door_open = random.choice(goatdoor)  # Open a door that comprises with goat
    while door_open == choice:  # door open shouldn't be equal to choice made by the participant
        door_open = random.choice(goatdoor)
    ch = input("Do you want to swap? y/n")
    if ch == "y":
        if doors[choice] == "Goat":
            print("Player wins")
            swap = swap + 1
        else:
            print("Player lost")
    else:
        if doors[choice] == "Goat":
            print("Player lost")
        else:
            print("Player wins")
            dont_swap = dont_swap + 1
    j = j + 1
print(swap)
print(dont_swap)
