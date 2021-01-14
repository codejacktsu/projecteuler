"""
In the card game poker, a hand consists of five cards and are ranked, from lowest to highest, in the following way:

High Card: Highest value card.
One Pair: Two cards of the same value.
Two Pairs: Two different pairs.
Three of a Kind: Three cards of the same value.
Straight: All cards are consecutive values.
Flush: All cards of the same suit.
Full House: Three of a kind and a pair.
Four of a Kind: Four cards of the same value.
Straight Flush: All cards are consecutive values of same suit.
Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
The cards are valued in the order:
2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.

If two players have the same ranked hands then the rank made up of the highest value wins;
for example, a pair of eights beats a pair of fives (see example 1 below). But if two ranks tie,
for example, both players have a pair of queens, then highest cards in each hand are compared (see example 4 below);
 if the highest cards tie then the next highest cards are compared, and so on.

Consider the following five hands dealt to two players:

Hand	 	Player 1	 	Player 2	 	Winner
1	 	5H 5C 6S 7S KD
Pair of Fives
 	2C 3S 8S 8D TD
Pair of Eights
 	Player 2
2	 	5D 8C 9S JS AC
Highest card Ace
 	2C 5C 7D 8S QH
Highest card Queen
 	Player 1
3	 	2D 9C AS AH AC
Three Aces
 	3D 6D 7D TD QD
Flush with Diamonds
 	Player 2
4	 	4D 6S 9H QH QC
Pair of Queens
Highest card Nine
 	3D 6D 7H QD QS
Pair of Queens
Highest card Seven
 	Player 1
5	 	2H 2D 4C 4D 4S
Full House
With Three Fours
 	3C 3D 3S 9S 9D
Full House
with Three Threes
 	Player 1
The file, poker.txt, contains one-thousand random hands dealt to two players.
Each line of the file contains ten cards (separated by a single space):
the first five are Player 1's cards and the last five are Player 2's cards.
You can assume that all hands are valid (no invalid characters or repeated cards),
each player's hand is in no specific order, and in each hand there is a clear winner.

How many hands does Player 1 win?
"""

import os
from collections import Counter
from util import timer


@timer
def poker_hands():
    path = os.path.join(os.getcwd(), "p054_poker.txt")
    p1score = 0
    with open(path, "r") as file:
        data = file.readlines()
        for hand in data:
            P1 = Player(process(hand.split()[:5]))
            P2 = Player(process(hand.split()[5::]))
            p1score += compete(P1, P2)
            # print(P1.hand, P2.hand, "|", P1.tier, P2.tier, "|", p1score)
    return p1score


def compete(P1, P2):
    if P1.tier > P2.tier:
        return 1
    elif P1.tier < P2.tier:
        return 0
    else:
        for i in reversed(range(5)):
            if P1.hand[i] > P2.hand[i]:
                return 1
            elif P1.hand[i] < P2.hand[i]:
                return 0
    return 0


class Player:
    def __init__(self, processed):
        self.hand = sorted(processed[0])

        self.tier = 1
        self.flush = processed[1]
        self.straight = bool(self.check_straight())
        self.straight_flush = bool(self.check_straightflush())
        self.royal_flush = bool(self.straight_flush and min(self.hand) == 10)
        self.fourkind = False
        self.boat = False
        self.triple = False
        self.twopairs = False
        self.pair = False
        self.dup_order = self.check_dup()
        self.order()

    def check_flush(self):
        if self.flush:
            self.tier = max(self.tier, 6)

    def check_straight(self):
        diff = max(self.hand) - min(self.hand)
        if (diff == 4 and len(set(self.hand)) == 5) or self.hand == [2, 3, 4, 5, 14]:
            self.tier = max(self.tier, 5)
            return 1

    def check_straightflush(self):
        if self.flush and self.straight:
            self.tier = max(self.tier, 9)
            return 1

    def check_dup(self):
        pairs = []
        trip = []
        four = []
        single = []
        for card in self.hand:
            count = Counter(self.hand)[card]
            if count == 2:
                pairs.append(card)
            elif count == 3:
                trip.append(card)
                self.tier = max(self.tier, 4)
                self.triple = True
            elif count == 4:
                four.append(card)
                self.tier = max(self.tier, 8)
                self.fourkind = True
            else:
                single.append(card)

        if len(pairs) == 4:
            self.tier = max(self.tier, 3)
            self.twopairs = True
        elif len(pairs) == 2:
            self.tier = max(self.tier, 2)
            self.pair = True

        if self.triple and self.pair:
            self.tier = max(self.tier, 7)
            self.boat = True

        final = single + pairs + trip + four
        return final

    def order(self):
        if self.tier in [2, 3, 4, 7, 8]:
            self.hand = self.dup_order


def process(hand):
    t_hand = []
    suits = []
    key = {"T": 10,
           "J": 11,
           "Q": 12,
           "K": 13,
           "A": 14}
    for card in hand:
        if card[0] in key.keys():
            num = key[card[0]]
        else:
            num = int(card[0])
        t_hand.append(num)
        suits.append(card[1])
    return t_hand, not bool(len(set(suits)) - 1)


print(poker_hands())
