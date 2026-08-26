from random import randint

money=1000

player_hand=0
dealer_hand=0

def Play():
    print(f"Dealer Hand:{dealer_card1}+X")
    print("="*100)
    print(f"Player Hand:{player_hand}")
    print("="*100)
    option=input("Hit(h) or Stay(s):").lower()
    print("="*100)

    if option == ("h" or "hit"):
        print("You Hit!")
        print("="*100)
        Hit()
    elif option == ("s" or "stay"):
        print("You Pass!")
        print("="*100)
        pass

def Hit():
    global player_hand
    PlayerNewCard=randint(1,10)

    player_hand=+PlayerNewCard

    print(f"Your New Card:{PlayerNewCard}")
    print(f"Your Total Hand:{player_hand}")
    print("="*100)
    Play()

while True:
    print("="*100)
    bet=int(input("Bet:"))
    print("="*100)

    player_card1=randint(1,10)
    player_card2=randint(1,10)

    dealer_card1=randint(1,10)
    dealer_card2=randint(1,10)

    player_hand=player_card1+player_card2

    money=-bet

    Play()

    #Dealer

    print("Dealer Turn!")
    print("="*100)
    print(f"Dealer Hand:{dealer_hand}")
    print("="*100)
    
    