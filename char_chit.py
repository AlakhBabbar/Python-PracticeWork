import random
import time
while True:
    #making player class
    class Player:
        def __init__(self, name):
            self.name = name

        # def score(self, int):
        #     self.score = int

        def character(self, char):
            self.char = char

        def change(self, thing, newthing):
            if thing=="score":
                self.score = newthing
            elif thing=="name":
                self.name = newthing
            elif thing=="guess":
                guess = input(f"for {self.name}'s character type s for sipahi and c for chor")
                self.guess = guess
            else:
                print("specify the thing you want to change")
        def input_chance(self):
            chance = input(f"{self.name} enter a character among a, b, c, d: ")
            self.chance = chance

        # def guess(self):
        #     guess = input(f"for {self.name}'s character type s for sipahi and c for chor")
        #     self.guess = guess
        def printcas(self):
            if self.char == "Raja":
                print(f"{self.name} picked Raja and their score of this round is: {self.score}")
            if self.char == "Mantri":
                print(f"{self.name} picked Mantri and their score of this round is: {self.score}")
            if self.char == "Sipahi":
                print(f"{self.name} picked sipahi and their score of this round is: {self.score}")
            if self.char == "Chor":
                print(f"{self.name} picked chor and their score of this round is: {self.score}")

    print("welcome to digital chr chit game. enter your names and enjoy the game...")
    time.sleep(3)
    #creating player class instance and denoting them their name
    namep1, namep2, namep3, namep4 = input("enter your name: "), input("enter your name: "), input("enter your name: "),input("enter your name: ")

    player1, player2, player3, player4 = Player(namep1), Player(namep2),Player(namep3),Player(namep4)

    round = 0
    tsp1 = 0
    tsp2 = 0
    tsp3 = 0
    tsp4 = 0
    #main game starts
    while 4>round:
        round +=1

    #randomnise the characters

        character = ["Raja-100", "Mantri-50", "Sipahi-10", "Chor-0"]
        a = random.choice(character)
        scorea = int(a.split("-")[1])
        character.remove(a)
        b = random.choice(character)
        scoreb = int(b.split("-")[1])
        character.remove(b)
        c = random.choice(character)
        scorec = int(c.split("-")[1])
        character.remove(c)
        d = random.choice(character)
        scored = int(d.split("-")[1])

    #getting players input and dinoting them their character as their input
        chance_draw = [player1,player2,player3,player4]
        random.shuffle(chance_draw)
        letter = ["a","b","c","d"]
        while True:
            chance_draw[0].input_chance()
            if chance_draw[0].chance == "a":
                letter.remove("a")
                chance_draw[0].character(a.split("-")[0])
                chance_draw[0].change("score", scorea)
                break
            elif chance_draw[0].chance=="b":
                letter.remove("b")
                chance_draw[0].character(b.split("-")[0])
                chance_draw[0].change("score", scoreb)
                break
            elif chance_draw[0].chance == "c":
                letter.remove("c")
                chance_draw[0].character(c.split("-")[0])
                chance_draw[0].change("score", scorec)
                break
            elif chance_draw[0].chance == "d":
                letter.remove("d")
                chance_draw[0].character(d.split("-")[0])
                chance_draw[0].change("score", scored)
                break
            else:
                print(f"{chance_draw[0].name} chose an invalid character.")
                continue
        time.sleep(1)
        while True:
            chance_draw[1].input_chance()
            if chance_draw[1].chance == "a":
                try:
                    letter.remove("a")
                except Exception as galti:
                    print("this character is already choosen\nchoose another one")
                    continue
                chance_draw[1].change("score", scorea)
                chance_draw[1].character(a.split("-")[0])
                break
            elif chance_draw[1].chance=="b":
                try:
                    letter.remove("b")
                except Exception as galti:
                    print("this character is already choosen\nchoose another one")
                    continue
                chance_draw[1].change("score", scoreb)
                chance_draw[1].character(b.split("-")[0])
                break
            elif chance_draw[1].chance == "c":
                try:
                    letter.remove("c")
                except Exception as galti:
                    print("this character is already choosen\nchoose another one")
                    continue
                chance_draw[1].change("score", scorec)
                chance_draw[1].character(c.split("-")[0])
                break
            elif chance_draw[1].chance == "d":
                try:
                    letter.remove("d")
                except Exception as galti:
                    print("this character is already choosen\nchoose another one")
                    continue
                chance_draw[1].change("score",scored)
                chance_draw[1].character(d.split("-")[0])
                break
            else:
                print(f"{chance_draw[1].name} chose an invalid character.")
                continue
        time.sleep(1)
        while True:
            chance_draw[2].input_chance()
            if chance_draw[2].chance == "a":
                try:
                    letter.remove("a")
                except Exception as galti:
                    print("this character is already choosen\nchoose another one")
                    continue
                chance_draw[2].change("score",scorea)
                chance_draw[2].character(a.split("-")[0])
                break
            elif chance_draw[2].chance=="b":
                try:
                    letter.remove("b")
                except Exception as galti:
                    print("this character is already choosen\nchoose another one")
                    continue
                chance_draw[2].change("score",scoreb)
                chance_draw[2].character(b.split("-")[0])
                break
            elif chance_draw[2].chance == "c":
                try:
                    letter.remove("c")
                except Exception as galti:
                    print("this character is already choosen\nchoose another one")
                    continue
                chance_draw[2].change("score",scorec)
                chance_draw[2].character(c.split("-")[0])
                break
            elif chance_draw[2].chance == "d":
                try:
                    letter.remove("d")
                except Exception as galti:
                    print("this character is already choosen\nchoose another one")
                    continue
                chance_draw[2].change("score",scored)
                chance_draw[2].character(d.split("-")[0])
                break
            else:
                print(f"{chance_draw[2].name} chose an invalid character.")
                continue
        time.sleep(1)
        while True:
            chance_draw[3].input_chance()
            if chance_draw[3].chance == "a":
                try:
                    letter.remove("a")
                except Exception as galti:
                    print("this character is already choosen\nchoose another one")
                    continue
                chance_draw[3].change("score",scorea)
                chance_draw[3].character(a.split("-")[0])
                break
            elif chance_draw[3].chance=="b":
                try:
                    letter.remove("b")
                except Exception as galti:
                    print("this character is already choosen\nchoose another one")
                    continue
                chance_draw[3].change("score",scoreb)
                chance_draw[3].character(b.split("-")[0])
                break
            elif chance_draw[3].chance == "c":
                try:
                    letter.remove("c")
                except Exception as galti:
                    print("this character is already choosen\nchoose another one")
                    continue
                chance_draw[3].change("score",scorec)
                chance_draw[3].character(c.split("-")[0])
                break
            elif chance_draw[3].chance == "d":
                try:
                    letter.remove("d")
                except Exception as galti:
                    print("this character is already choosen\nchoose another one")
                    continue
                chance_draw[3].change("score",scored)
                chance_draw[3].character(d.split("-")[0])
                break
            else:
                print(f"{chance_draw[3].name} chose an invalid character.")
                continue

        for item in chance_draw:
            if item.score == 100:
                raja = item
                break
        for item in chance_draw:
            if item.score == 10:
                sipahi = item
                break
        for item in chance_draw:
            if item.score == 0:
                chor = item
        for item in chance_draw:
            if item.score== 50:
                time.sleep(1)
                print(f"{raja.name}: mera mantri kon?")
                time.sleep(1)
                print(f"{item.name}: ji huzur..")
                time.sleep(1)
                print(f"{raja.name}: {sipahi.name} aur {chor.name} mein se chor aur sipahi ka pta lagao.")
                time.sleep(1)
                guess_ = [chor,sipahi]
                random.shuffle(guess_)
                # print(f"{sipahi.name} sipahi {chor.name} chor")
                guess_[0].change("guess", None)
                time.sleep(1)
                guess_[1].change("guess", None)

                while True:

                    if sipahi.guess=="s" and chor.guess=="c":
                        time.sleep(1)
                        print(f"you guessed right! {sipahi.name} is sipahi and {chor.name} is chor. you have secured your 50 points.")
                        break
                    elif sipahi.guess=="c" and chor.guess=="s":
                        time.sleep(1)
                        print(f"you guessed wrong\n{sipahi.name} is sipahi and {chor.name} is chor.\nyou loss your 50 points to chor {chor.name}")
                        item.change("score", 0)
                        chor.change("score", 50)
                        break
                    else:
                        print("you typed an invalid guess\ntry again...")
                        continue
                break

        time.sleep(1)
        print(f"round-{round} is completed and here are the results:-")
        time.sleep(1)
        player1.printcas()
        time.sleep(1)
        player2.printcas()
        time.sleep(1)
        player3.printcas()
        time.sleep(1)
        player4.printcas()

        tsp1 += player1.score
        tsp2 += player2.score
        tsp3 += player3.score
        tsp4 += player4.score

    print("your total score of this game is following:- ")
    print(f"{player1.name} total score is {tsp1}")
    print(f"{player2.name} total score is {tsp2}")
    print(f"{player3.name} total score is {tsp3}")
    print(f"{player4.name} total score is {tsp4}")
    winner = [tsp1,tsp2,tsp3,tsp4]
    if tsp1 == max(winner):
        print(f"{player1.name} is winner")
    elif tsp2 == max(winner):
        print(f"{player2.name} is winner")
    elif tsp3 == max(winner):
        print(f"{player3.name} is winner")
    elif tsp4 == max(winner):
        print(f"{player4.name} is winner")
    else:
        print("kuchh to gadbad hein...")

    while True:
        play_again = input("do you want to play again? if YES type y if NO type n: ")
        if play_again=="y":
            break
        elif play_again=="n":
            break
        else:
            print("didn't understand please reconfirm:- ")
            continue
    if play_again=="y":
        print("restarting...")
        time.sleep(2)
        continue
    else:
        print("thankyou for playing have a good day!")
        break