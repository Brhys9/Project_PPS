import random
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.rank['rank']} of {self.suit}"


class Deck:
    def __init__(self):
        self.cards = []
        suits = ["\u2764\ufe0f", "\u2660\ufe0f", "\u2666\ufe0f", "\u2663\ufe0f"]
        ranks = [{"rank": 'A', "value": 11}, {"rank": '2', "value": 2}, {"rank": '3', "value": 3},
                 {"rank": '4', "value": 4}, {"rank": '5', "value": 5}, {"rank": '6', "value": 6},
                 {"rank": '7', "value": 7}, {"rank": '8', "value": 8}, {"rank": '9', "value": 9},
                 {"rank": '10', "value": 10}, {"rank": 'J', "value": 10}, {"rank": 'Q', "value": 10},
                 {"rank": 'K', "value": 10}]
        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(suit, rank))

    def shuffle(self):
        if len(self.cards) > 1:
            random.shuffle(self.cards)

    def deal(self, number):
        card_dealt = []
        for x in range(number):
            if len(self.cards) > 0:
                card = self.cards.pop()
                card_dealt.append(card)
        return card_dealt


class Hand:
    def __init__(self, dealer=False):
        self.cards = []
        self.value = 0
        self.dealer = dealer

    def addCards(self, card_list):
        self.cards.extend(card_list)

    def calValue(self):
        has_ace = False
        self.value = 0
        for x in self.cards:
            cardValue = int(x.rank["value"])
            self.value += cardValue
            if x.rank["rank"] == "A":
                has_ace = True

        if has_ace and self.value > 21:
            self.value -= 10

    def getValue(self):
        self.calValue()
        return self.value

    def isBlackJack(self):
        return self.value == 21

    def disp(self, show_all_dealer_cards=False):
        print(f''' {"Dealer's " if self.dealer else "Your"} hand:''')
        for index, x in enumerate(self.cards):
            if index == 0 and self.dealer \
                    and not show_all_dealer_cards \
                    and not self.isBlackJack():
                print("Hidden")
            else:
                print(x)
        if not self.dealer:
            print("Value: ", self.getValue())
        print()


class Game:
    def play(self):
        game_number = 0
        games_to_play = 0
        while games_to_play <= 0:
            try:
                games_to_play = int(input("how many games do you want to play?"))
            except:
                print(" Please enter a number ")

        while game_number < games_to_play:
            game_number += 1
            deck = Deck()
            deck.shuffle()
            pHand = Hand()
            dealerHand = Hand(dealer=True)
            for x in range(2):
                pHand.addCards(deck.deal(1))
                dealerHand.addCards(deck.deal(1))
            print()
            print("*" * 30)
            print(f'{game_number} of {games_to_play}')
            print("*" * 30)
            pHand.disp()
            dealerHand.disp()

            if self.check_winner(pHand, dealerHand):
                continue
            choice = ""
            while pHand.getValue() < 21 and choice not in ['s', 'stand']:
                choice = input("hit or stand ").lower()
                print()
                while choice not in ['s', 'h', 'hit', 'stand']:
                    choice = input("hit or stand (h/s)").lower()
                    print()
                if choice in ['hit', 'h']:
                    pHand.addCards((deck.deal(1)))
                    pHand.disp()
            if self.check_winner(pHand, dealerHand):
                continue
            phandValue = pHand.getValue()
            dealerHandValue = dealerHand.getValue()
            while dealerHandValue < 17:
                dealerHand.addCards(deck.deal(1))
                dealerHandValue = dealerHand.getValue()
            dealerHand.disp(show_all_dealer_cards=True)
            if self.check_winner(pHand, dealerHand):
                continue
            print('Final Results')
            print("your hand", phandValue)
            print("dealer hand", dealerHandValue)
            self.check_winner(pHand, dealerHand, True)
        print("\nThanks for Playing!")

    def check_winner(self, pHand, dealerHand, gameOver=False):
        if not gameOver:
            if pHand.getValue() > 21:
                print("Dealer WIns!")
                return True
            elif dealerHand.getValue() > 21:
                print("You WIn!")
                return True
            elif dealerHand.isBlackJack() and pHand.isBlackJack():
                print("tie")
                return True
            elif pHand.isBlackJack():
                print("bj, you win")
                return True
            elif dealerHand.isBlackJack():
                print("bj ,dealer wins")
                return True
        else:
            if pHand.getValue() > dealerHand.getValue():
                print("you win!")
            elif pHand.getValue() == dealerHand.getValue():
                print("Tie")
            else:
                print("Dealer wins")
            return True
        return False


g = Game()
g.play()


