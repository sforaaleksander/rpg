import time
import random
import sys


def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        time.sleep(0.05)


class Hero:
    exp_points = 0

    def __init__(self, name, health_points, strength_points, defence_points):
        self.name = name
        self.health_points = health_points
        self.strength_points = strength_points
        self.defence_points = defence_points

    def death(self):
        if self.health_points >= 0:
            print("You are dead!")


Hero1 = Hero("", 100, 0, 0)
delay_print("Welcome to the RPG game! Type in the name of your character: ")
Hero1.name = input()
Hero1 = Hero(Hero1.name, 100, 0, 0)

delay_print("Hello " + Hero1.name + "! Time to assign your skill points. "
                        "You have 10 points left. Add points to the following atributes: \nSTRENGTH \nDEFENCE")


Hero1.strength_points = int(input("\nAdd points to strength: "))
spare_points = 10
if Hero1.strength_points <= spare_points:
    delay_print("You now have %d strength points." % Hero1.strength_points)
else:
    while Hero1.strength_points > spare_points:
        delay_print("Do not cheat! You have only 10 points to assign. Type a value in that range: ")
        correct = int(input())
        if correct <= spare_points:
            Hero1.strength_points = correct
            delay_print("You now have %d strength points." % Hero1.strength_points)


spare_points = 10 - Hero1.strength_points


Hero1.defence_points = int(input("\nAdd points to defence: "))
if Hero1.defence_points <= spare_points:
    delay_print("You now have %d defence points" % Hero1.defence_points)
else:
    while Hero1.defence_points > spare_points:
        delay_print("Do not cheat! You have only " + str(spare_points) + " points to assign. Type a value within this range.")
        correct2 = int(input())
        if correct2 <= spare_points:
            Hero1.defence_points = correct2
            delay_print("You now have %d defence points" % Hero1.defence_points)


delay_print(("\nWell done, %s. You have %d strength points and %d defence points. Let's start the game!" % (Hero1.name,
Hero1.strength_points, Hero1.defence_points)))

time.sleep(3)


class Monster:
    def __init__(self, name, health_points, strength_points, defence_points):
        self.name = name
        self.health_points = health_points
        self.strength_points = strength_points
        self.defence_points = defence_points


Jaszczur = Monster("Jaszczur", 20, 5, 6)


def fight_monster(monsters_name, monsters_health, monsters_strength, monsters_defence, heroes_health, heroes_strength, heroes_defence):
    delay_print("\nFight!")

    while True:
        delay_print("\nYou attack %s!" % monsters_name)
        attack1 = heroes_strength * random.randint(0, 5) - monsters_defence
        monsters_health -= attack1
        delay_print("\nYou took the monster %d health points!" % attack1)
        delay_print("\nThe monster has %d health points left!" % monsters_health)
        if (monsters_health <= 0) or (heroes_health <= 0):
            break

        delay_print("\nNow the monster attacks!")
        attack2 = monsters_strength * random.randint(0, 5) - heroes_defence
        heroes_health -= attack2
        delay_print("\nThe monster took you %d health points!" % attack2)
        delay_print("\nYou have %d health points left!" % heroes_health)
        if (monsters_health <= 0) or (heroes_health <= 0):
            break

    if monsters_health <= 0:
        delay_print("\nYou killed the monster!")
        delay_print("\nYou earned 10 EXP points!")
        Hero1.exp_points += 10
    elif heroes_health <= 0:
        delay_print("\nYou are dead!")
        delay_print("\nGame over!")
        sys.exit()


def yes_or_no():
    if random.randint(0,1) == 1:
        return True
    else:
        return False


def run():
    delay_print("\nYou are running! The monster is right behind you...")
    delay_print("\nCan you make it?")
    delay_print("\n......")
    delay_print("\nPray for your soul...!")
    fifty_fifty = yes_or_no()
    if fifty_fifty:
        delay_print("\nYou made it!")
    else:
        delay_print("\nThe monster got you! Prepare for the fight!")
        fight_monster(Jaszczur.name, Jaszczur.health_points, Jaszczur.strength_points, Jaszczur.defence_points, Hero1.health_points,
                      Hero1.strength_points, Hero1.defence_points)


delay_print("\nSuddenly a monster attacks you! Do you want to FIGHT or RUN?")
choice = input()
choice = choice.lower()
if choice == "run":
    run()
elif choice == "fight":
    fight_monster(Jaszczur.name, Jaszczur.health_points, Jaszczur.strength_points, Jaszczur.defence_points, Hero1.health_points,
                  Hero1.strength_points, Hero1.defence_points)


def wise_man():
    delay_print("\nYou encountered an old, wise man. Thanks to his wisdom, you gained 3 skill points. "
                "\nDo you want to add them to STRENGTH or DEFENCE?")
    wisdom = input("\nType in STRENGTH or DEFENCE to spend your points: ")
    wisdom = wisdom.lower()
    if wisdom == "strength":
        Hero1.strength_points += 3
        delay_print("\nYou now have %d strength points!" % Hero1.strength_points)
    elif wisdom == "defence":
        Hero1.defence_points += 3
        delay_print("\nYou now have %d defence points!" % Hero1.defence_points)


wise_man()

# Tic Tac Toe game in python
def tic_tac_toe():
    board = [' ' for x in range(10)]

    def insertLetter(letter, pos):
        board[pos] = letter

    def spaceIsFree(pos):
        return board[pos] == ' '

    def printBoard(board):
        print('\n   |   |')
        print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
        print('   |   |')
        print('-----------')
        print('   |   |')
        print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
        print('   |   |')
        print('-----------')
        print('   |   |')
        print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
        print('   |   |')

    def isWinner(bo, le):
        return (bo[7] == le and bo[8] == le and bo[9] == le) or (bo[4] == le and bo[5] == le and bo[6] == le) or (
                    bo[1] == le and bo[2] == le and bo[3] == le) or (bo[1] == le and bo[4] == le and bo[7] == le) or (
                           bo[2] == le and bo[5] == le and bo[8] == le) or (
                           bo[3] == le and bo[6] == le and bo[9] == le) or (
                           bo[1] == le and bo[5] == le and bo[9] == le) or (bo[3] == le and bo[5] == le and bo[7] == le)

    def playerMove():
        run = True
        while run:
            delay_print("Please select a position to place an \'X\' (1-9): ")
            move = input()
            try:
                move = int(move)
                if move > 0 and move < 10:
                    if spaceIsFree(move):
                        run = False
                        insertLetter('X', move)
                    else:
                        delay_print('Sorry, this space is occupied!')
                else:
                    delay_print('Please type a number within the range!')
            except:
                delay_print('Please type a number!')

    def compMove():
        possibleMoves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]
        move = 0

        for let in ['O', 'X']:
            for i in possibleMoves:
                boardCopy = board[:]
                boardCopy[i] = let
                if isWinner(boardCopy, let):
                    move = i
                    return move

        cornersOpen = []
        for i in possibleMoves:
            if i in [1, 3, 7, 9]:
                cornersOpen.append(i)

        if len(cornersOpen) > 0:
            move = selectRandom(cornersOpen)
            return move

        if 5 in possibleMoves:
            move = 5
            return move

        edgesOpen = []
        for i in possibleMoves:
            if i in [2, 4, 6, 8]:
                edgesOpen.append(i)

        if len(edgesOpen) > 0:
            move = selectRandom(edgesOpen)
        return move

    def selectRandom(li):
        import random
        ln = len(li)
        r = random.randrange(0, ln)
        return li[r]

    def isBoardFull(board):
        if board.count(' ') > 1:
            return False
        else:
            return True

    def main():
        printBoard(board)

        while not (isBoardFull(board)):
            if not (isWinner(board, 'O')):
                playerMove()
                printBoard(board)
            else:
                delay_print('\nDragon wins!')
                delay_print("\nLaughing madly the Dragon eats you.")
                delay_print("\nGame over!")
                sys.exit()

            if not (isWinner(board, 'X')):
                move = compMove()
                if move == 0:
                    delay_print('Tie Game!')
                else:
                    insertLetter('O', move)
                    delay_print('\nDragon placed an \'O\' in position ' + str(move) + ':')
                    printBoard(board)
            else:
                delay_print('\nYou win! Dragon is full of respect and lets you go!')
                delay_print("\nYou earn 30 exp points.")
                Hero.exp_points += 30
                break

        if isBoardFull(board):
            print('Tie Game!')


    if True:
        answer = input("\nYou encountered a dragon, he challanges you to duel TIC TAC TOE! Do you want to FIGHT or RUN?")
        if answer.lower() == "fight":
            board = [' ' for x in range(10)]
            main()
        elif answer.lower() == "run":
            run()


tic_tac_toe()

delay_print("\nTake some rest, soldier, you did well today. The journey will continue tomorrow.")