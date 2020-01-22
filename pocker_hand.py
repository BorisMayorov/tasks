def card_invert(cards):
    mod_hand = []
    for i in hand:
        mod_hand.append(values.get(i[0:-1]))
        mod_hand.sort()
    return mod_hand


def find_rep(x):
    rep = []
    k = 0
    counter = 1

    for i in x:
        if i == k:
            counter += 1
        else:
            if counter > 1:
                rep.append(counter)
            counter = 1
        k = i
    if counter > 1:
        rep.append(counter)
    return rep


def check_suit(x):
    k = x[0][-1]
    for i in x:
        if i[-1] != k:
            return False
        k = i[-1]
    return True


def check_straight(x):
    for i in range(len(x)-1):
        if x[i+1] - x[i] != 1:
            return False
    if x[0] == 10:
        return 'High_Straight'
    else:
        return 'Straight'


def classify(x):
    suit = check_suit(x)
    dig_cards = card_invert(x)
    rep = find_rep(dig_cards)
    straight = check_straight(dig_cards)

    if straight == 'High_Straight' and suit is True:
        return 'Royal Flush'
    elif straight == 'Straight' and suit is True:
        return 'Straight Flush'
    elif 4 in rep:
        return 'Four of Kind'
    elif 3 in rep and 2 in rep:
        return 'Full House'
    elif suit is True:
        return 'Flush'
    elif straight == 'Straight':
        return 'Straight'
    elif 3 in rep:
        return 'Three of Kind'
    elif 2 in rep and len(rep) == 2:
        return 'Two Pairs'
    elif 2 in rep:
        return 'Pair'
    else:
        return 'High Card'


values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}

hand = input().split(' ')

print(classify(hand))

