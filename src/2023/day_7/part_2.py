from utils.utils import read_file
from collections import Counter

rank_card = {
    "A": 1, "K": 2, "Q": 3, "J": 14, "T": 5, "9": 6, "8": 7, "7": 8, "6": 9, "5": 10, "4": 11, "3": 12, "2": 13,
}

rank_type = {
    (5,): 1,
    (4,1): 2,
    (3,2): 3,
    (3,1,1): 4,
    (2,2,1): 5,
    (2,1,1,1): 6,
    (1,1,1,1,1): 7
}

def get_type(hand):
    if not "J" in hand or hand == "JJJJJ":
        counts = Counter(ch for ch in hand)
        return tuple(sorted(counts.values(), reverse=True))
    else:
        cards_to_try = set(hand).difference({"J"})
        top_type = None
        for card in cards_to_try:
            new_type = get_type(hand.replace("J", card))
            if top_type is None or rank_type[new_type] < rank_type[top_type]:
                top_type = new_type
        return top_type


def sorting_func(hand):
    type_ = get_type(hand)
    rank = [rank_type[type_]]
    for i in range(len(hand)):
        rank.append(rank_card[hand[i]])
    return rank


def main(example=False):
    hands = []
    hands_bid = {}
    for line in read_file(example):
        hand, bid = line.split(" ")
        hands.append(hand)
        hands_bid[hand] = int(bid)
    hands.sort(key=sorting_func, reverse=True)
    res = 0
    for i in range(len(hands)):
        res += (i+1)*hands_bid[hands[i]]
    print(res)
    return res


assert main(True) == 5905
main()
