import random
deck = [
    "HA", "SA", "DA", "CA",
    "H2", "S2", "D2", "C2",
    "H3", "S3", "D3", "C3",
    "H4", "S4", "D4", "C4",
    "H5", "S5", "D5", "C5",
    "H6", "S6", "D6", "C6",
    "H7", "S7", "D7", "C7",
    "H8", "S8", "D8", "C8",
    "H9", "S9", "D9", "C9",
    "H10", "S10", "D10", "C10",
    "HJ", "SJ", "DJ", "CJ",
    "HQ", "SQ", "DQ", "CQ",
    "HK", "SK", "DK", "CK"
]
existingCards = []
hand1 = []

def dealing(hand):
    while len(hand) < 2:
        randCard = random.choice(deck)
        if not(randCard in existingCards):
            hand.append(randCard)
            existingCards.append(randCard)
def summingHand(hand):
    sum = 0
    sum_alternate = sum
    for card in hand:
        card = card[1:]
        if card.isdigit():
            sum += int(card)
            sum_alternate += int(card)
        else:
            if card == "A":
                sum += 1
                sum_alternate += 11
            else:
                sum += 10
                sum_alternate += 10

    if sum_alternate > 21:
        return (sum, 0)
    return sum, sum_alternate
def decision(dealerHand, ownHand):
    ohs = summingHand(ownHand)
    dhs = summingHand(dealerHand)

    

