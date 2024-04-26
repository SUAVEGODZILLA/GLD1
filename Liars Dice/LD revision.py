import sys, re, random, subprocess_1
from rich import print
from icecream import ic

answer = {"value": "0", "amount": "0"}
value, amount = answer["value"], answer["amount"]
goblinDiceCount, playerDiceCount = range(0, 5), range(0, 5)
coin = random.randint(0, 1)
if coin == 0:
    coin == 'heads'
else:
    coin == 'tails'
def coinToss(coin):
    hort = input("Heads or Tails?\n")
    hort = hort.lower()
    hortValidity = bool(hort = 'heads' or 'tails') 
    if hortValidity is False:
        print("Invalid input! Try again.")
    elif coin in hort.lower():
        print("You win the coin toss!!")
    else:
        print("You lose the coin toss!")

coinToss(coin)