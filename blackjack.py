import numpy as np
from math import *

deck_dict = {"1♠": 1, "1♥": 1, "1♦": 1, "1♣": 1,
        "2♠": 2, "2♥": 2, "2♦": 2, "2♣": 2,
        "3♠": 3, "3♥": 3, "3♦": 3, "3♣": 3,
        "4♠": 4, "4♥": 4, "4♦": 4, "4♣": 4,
        "5♠": 5, "5♥": 5, "5♦": 5, "5♣": 5,
        "6♠": 6, "6♥": 6, "6♦": 6, "6♣": 6,
        "7♠": 7, "7♥": 7, "7♦": 7, "7♣": 7,
        "8♠": 8, "8♥": 8, "8♦": 8, "8♣": 8,
        "9♠": 9, "9♥": 9, "9♦": 9, "9♣": 9,
        "T♠": 10, "T♥": 10, "T♦": 10, "T♣": 10,
        "J♠": 10, "J♥": 10, "J♦": 10, "J♣": 10,
        "Q♠": 10, "Q♥": 10, "Q♦": 10, "Q♣": 10,
        "K♠": 10, "K♥": 10, "K♦": 10, "K♣": 10,
        "A♠": 11, "A♥": 11, "A♦": 11, "A♣": 11}

deck_list = ["A♠", "A♥", "A♦", "A♣",
             "2♠", "2♥", "2♦", "2♣",
             "3♠", "3♥", "3♦", "3♣",
             "4♠", "4♥", "4♦", "4♣",
             "5♠", "5♥", "5♦", "5♣",
             "6♠", "6♥", "6♦", "6♣",
             "7♠", "7♥", "7♦", "7♣",
             "8♠", "8♥", "8♦", "8♣",
             "9♠", "9♥", "9♦", "9♣",
             "T♠", "T♥", "T♦", "T♣",
             "J♠", "J♥", "J♦", "J♣",
             "Q♠", "Q♥", "Q♦", "Q♣",
             "K♠", "K♥", "K♦", "K♣"]



def calc_score(lst):
    score = 0
    for i in lst:
        score += deck_dict[i]
    return score

def hit(lst, deck):
    lst.append(deck.pop())



def play():

    d = []
    p = []
    d_score = 0
    p_score = 0

    deck = list(deck_list)
    np.random.shuffle(deck)
    hit(d, deck)
    hit(d, deck)
    hit(p, deck)
    hit(p, deck)
    while True:
        p_score = calc_score(p)
        if p_score > 21:
            if ("A♠" in p):
                p.remove("A♠")
                p.append("1♠")
            elif ("A♥" in p):
                p.remove("A♥")
                p.append("1♥")
            elif ("A♦" in p):
                p.remove("A♦")
                p.append("1♦")
            elif ("A♣" in p):
                p.remove("A♣")
                p.append("1♣")
            else:
                print(f"Here is your hand: {p}. You busted. The dealer wins.")
                return
        else:
            print(f"Here is your hand: {p}. Here is one of the dealer's cards: {d[0]}.")
            print(f"Would you like to hit or stand? Input 0 for hit and 1 for stand.")
            player_input = int(input())
            if player_input == 0:
                hit(p, deck)
            else:
                d_score = calc_score(d)
                if d_score > p_score and d_score >= 17:
                    print(f"Here is the dealer's hand: {d}. The dealer's score was {d_score}. The dealer wins.")
                    return
                elif d_score == p_score and d_score >= 17:
                    print(f"Here is the dealer's hand: {d}. The dealer's score was {d_score}. You pushed.")
                    return
                elif d_score < p_score and d_score >= 17:
                    print(f"Here is the dealer's hand: {d}. The dealer's score was {d_score}. The player wins.")
                    return
                else:
                    while d_score < 17:
                        hit(d, deck)
                        d_score = calc_score(d)
                        if d_score > 21:
                            if ("A♠" in d):
                                d.remove("A♠")
                                d.append("1♠")
                            elif ("A♥" in d):
                                d.remove("A♥")
                                d.append("1♥")
                            elif ("A♦" in d):
                                d.remove("A♦")
                                d.append("1♦")
                            elif ("A♣" in d):
                                d.remove("A♣")
                                d.append("1♣")
                            else:
                                print(f"Here is the dealer's new hand: {d}. The dealer busted. The player wins.")
                                return
                        elif d_score > p_score:
                            print(f"Here is the dealer's new hand: {d}. The dealer's score was {d_score}. The dealer wins.")
                            return
                        d_score = calc_score(d)
                    if d_score == p_score:
                        print(f"Here is the dealer's hand: {d}. The dealer's score was {d_score}. You pushed.")
                        return
                    else:
                        print(f"Here is the dealer's new hand: {d}. The dealer's score was {d_score}. The player wins.")
                        return