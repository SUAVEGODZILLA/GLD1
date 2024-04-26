import sys, re, random, subprocess_1
from rich import print
from icecream import ic

#█▓▒░┼┌┐└┘─│╭╮╰╯

turn = 1
#Dice groups
goblinDice = {"d1": "0", "d2": "0", "d3": "0", "d4": "0", "d5": "0", "d6": "0",}
playerDice = {"d1": "0", "d2": "0", "d3": "0", "d4": "0", "d5": "0", "d6": "0",}
#Dictionaries
#PLACEHOLDERS
playerTurnMessage = 'YOUR TURN'.center(20, '=')
goblinTurnMessage = 'MY TURN!'.center(20, '~')
#Guessing
answer = {"value": "0", "amount": "0"}
value,  amount = int(answer["value"]), int(answer["amount"]) # Answer reference
valueThreshold, amountThreshold = int(value + 1), int(amount + 1) # Minimum values for concurrent guesses
turnCounter = 1
goblinLoss = ''
playerLoss = ''
goblinDiceCount = range(0, 5)
playerDiceCount = range(0, 5)

heads = "Heads"
tails = "Tails"
#GAME FUNCTIONS :
def LIAR():
    print('"!!!LIAR!!!"'.center(20, '|'))
    dicePool = list(goblinDice.append(playerDice))
    for i in dicePool:
        dicePool[i] = int()
    dicePool.sort()
    print(dicePool)
    mo = diceInspectRegex.search(dicePool)
    ic(mo)
    if mo is True:
        print(" NO LIES ")
    elif mo is False:
        print(" WE FOUND A FIBBER!!! ")

def turnStart(turn):
    for d in goblinDice:
        goblinDice[d] = str(random.randint(1, 6))
    for L in goblinLoss:
        goblinDice.pop()
    for d in playerDice:
        playerDice[d] = str(random.randint(1, 6))
    for L in playerLoss:
        playerDice.pop()
    print(goblinDice.values())
    print(playerDice.values())
    print(' Turn Start '.center(20, "▓") + 'Turn No. '.rjust(50) + str(turnCounter))
    if turn == 'Goblin':
        print(goblinTurnMessage)
        goblin()
    elif turn != 'Goblin':
        print(playerTurnMessage)
        player()

#GOBLIN :
def goblin():                                        # Decides to either Inspect or Guess, from there:
    ic(answer)
    if answer["amount"] == "0":
         print("The goblin is thinking...")  
         goblinGuess(amount, value)  
    elif answer["amount"] != "0": 
        goblinInspect()

# Dice Inspect Regex

def goblinInspect():                                # The goblin then decides to either call bluff or take a guess
    ic(goblinDice)
    diceInspectRegex = re.compile(f"{value}{amount}")
    mo = diceInspectRegex.search("".join(list(goblinDice)))
    ic(mo)
    if mo is None:
        print("There are no matches in the goblin dice pool")
        goblinGuess(amount, value) # Right now the guessing only takes place if the goblin does not see any matches in his dice pool.
    if mo is True:                                  # Right now the decision making is black and white, needs more factors and variables.
        LIAR()
    
def goblinGuess(amount, value):                                  # The goblin then decides to tell a lie or a true guess.
    pairSearch = list(goblinDice.values())
    pairSearch.sort()
    pairSearch = "".join(pairSearch)
    for diceName, dice in goblinDice.items(): #this looks for pairs in goblinDice
        guessRegex = re.compile(r"{}{{2,}}".format(re.escape(dice)))
        mo = guessRegex.search(pairSearch)
        ic(mo)
        if mo is not None and int(dice) > int(value):
            print("I found a pair in my dice!\nAnd it`s greater in value than your value!")
            value, amount = dice, len(mo.group())
            print(f"My answer: {amount} {value}'s")
            
        



        

        

        


#PLAYER : 
def player():
    if turn > 1:
        print('"Will you call "liar" or take a "guess"?"')
        play = input()
        if play.startswith('l'):
            LIAR()
        if play.startswith('g'):
            guess()
        else:
            print("I just need an answer...")
            player()
    elif turn == 1:
        guess()

# You can de deuplicate guess() with some regexpressions...

def guess():
    print('?GUESS TIME?'.center(20, '░'))
    print(f"What number is your guess?")
    answer["value"] = input()
    print(f"How many {str(answer["value"])}'s are there?")
    answer["amount"] = input()
    if str(value + amount).isnumeric():
        
        goblin()
    else:
        
        guess()


def coinTossChoice():
    print("COIN TOSS".center(19, '|'))
    coin = random.randint(1,2)
    hort = input("Heads or Tails?\n")
    if coin == 1:
        face = heads
    else:
        face = tails
    if face.lower() == hort.lower():
        print(face)
        turn = 'Player'
        turnStart(turn)
    elif face.lower() != hort.lower():
        print(face)
        turn = 'Goblin'
        turnStart(turn)
















def tryAgain():
    yn = input('Again?\n')
    if yn == 'y':
        try:
            subprocess_1.run(["python", "d:/PYTHON/PYTHON PROJECTS/Liars Dice/Liar's Dice 2.py"], check=True)
        except subprocess_1.CalledProcessError as e:
            print("Error:", e)
    elif yn == 'n':
        sys.exit()
    else:
        print('What?')
        tryAgain()
coinTossChoice()
tryAgain()
sys.exit()
        
