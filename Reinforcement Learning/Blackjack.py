import numpy as np

cards = [['A',1], ['1',1], ['2',2], ['3',3], ['4',4], ['5',5], ['6',6], ['7',7], ['8',8], ['9',9], ['10',10], ['J',10], ['Q',10], ['K',10]]
player_cards = []
dealer_cards = []

def add_cards(Add):
    indices = np.arange(len(cards))
    Add.append(cards[np.random.choice(indices)])
    return Add

print(add_cards(player_cards))