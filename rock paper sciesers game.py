import random
while (True):
    print("welcome to the rock paper scissor game\npress enter to proceed: ")
    input()
    print("""RULES\n1. There are 10 rounds, in each round you have to choose your weapon among ROCK, PAPER and SCISSOR
    2. Following shows greatness of the weapons on each other..\nROCK>SCISSOR\nSCISSOR>PAPER\nPAPER>ROCK
    3. Who wins the most rounds will be the winner of the game\nGOOD LUCK!!""")
    round = 0
    pw = 0
    cw = 0
    tie = 0
    while (True):
        round = round + 1
        print("round- ", round)
        weapons = ["ROCK", "PAPER", "SCISSOR", "ROCK", "PAPER", "SCISSOR"]
        computer = random.choice(weapons)
        player = str(input("choose 1 for ROCK 2 for PAPER 3 for SCISSOR: "))
        x = "ROCK"
        y = "PAPER"
        z = "SCISSOR"
        if computer == "ROCK" and player == "1":
            print("computer chose", computer)
            print("you chose", x)
            print("TIE")
            tie = tie + 1
            print(f"Player wins = {pw}\nComputer wins = {cw}\nTies = {tie}")
        elif computer == "PAPER" and player == "2":
            print("computer chose", computer)
            print("you chose", y)
            print("TIE")
            tie = tie + 1
            print(f"Player wins = {pw}\nComputer wins = {cw}\nTies = {tie}")
        elif computer == "SCISSOR" and player == "3":
            print("computer chose", computer)
            print("you chose", z)
            print("TIE")
            tie = tie + 1
            print(f"Player wins = {pw}\nComputer wins = {cw}\nTies = {tie}")
        elif computer == "ROCK" and player == "2":
            print("computer chose", computer)
            print("you chose", y)
            print("player won")
            pw = pw + 1
            print(f"Player wins = {pw}\nComputer wins = {cw}\nTies = {tie}")
        elif computer == "PAPER" and player == "3":
            print("computer chose", computer)
            print("you chose", z)
            print("player won")
            pw = pw + 1
            print(f"Player wins = {pw}\nComputer wins = {cw}\nTies = {tie}")
        elif computer == "SCISSOR" and player == "1":
            print("computer chose", computer)
            print("you chose", x)
            print("player won")
            pw = pw + 1
            print(f"Player wins = {pw}\nComputer wins = {cw}\nTies = {tie}")
        elif computer == "ROCK" and player == "3":
            print("computer chose", computer)
            print("you chose", z)
            print("computer won")
            cw = cw + 1
            print(f"Player wins = {pw}\nComputer wins = {cw}\nTies = {tie}")
        elif computer == "PAPER" and player == "1":
            print("computer chose", computer)
            print("you chose", x)
            print("computer won")
            cw = cw + 1
            print(f"Player wins = {pw}\nComputer wins = {cw}\nTies = {tie}")
        elif computer == "SCISSOR" and player == "2":
            print("computer chose", computer)
            print("you chose", y)
            print("computer won")
            cw = cw + 1
            print(f"Player wins = {pw}\nComputer wins = {cw}\nTies = {tie}")
        elif player=="restart":
            print("restarting...")
            break
        elif player=="quit":
            print("Do want to quit")
            quit = input("yes or no: ")
            if quit=="yes":
                break
            elif quit=="no":
                round = round - 1
                continue
            else:
                round = round - 1
                print("Didn't understand please reconfirm...")
                continue
        else:
            round = round - 1
            print("computer chose", computer)
            print("you chose", player, "which will not consider")
            print("please follow the steps as told")

        if round == 10:
            if cw>>pw:
                print("COMPUTER WON THE GAME!")
            elif pw>>cw:
                print("YOU WON THE GAME!")
            else:
                print("!TIE!")
            break
        else:
            continue

    if player=="restart":
        continue
    else:
        pass

    while (True):
        playagain = input("Want to play again ? If YES type y if NO type n: ")
        if playagain=="y":
            break
        elif playagain=="n":
            break
        else:
            print("Didn't understand please reconfirm...")
            continue

    if playagain=="y":
        print("restarting...")
        continue
    else:
        print("thank you for playing!")
        break
