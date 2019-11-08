
# сделал два варианта, в первом мы указываем индекс карты, для вывода
from random import shuffle
from random import choice
ranks = [str(n) for n in range (2, 11)] + list("JQKA")
suits = 'spades diamonds clubs hearts'.split()
cards = [(suit, rank) for suit in suits 
         for rank in ranks]  
shuffle(cards)
# идея сперта из книги "Пайтон, к Вершинам мастерства"

class Deck_cards: 
    def __getitem__(self, position):
        del_ = cards.pop(position)
        print (f"Вы вытащили карту: {' - '.join(del_)}")
        print (f"Теперь в колоде: {len(cards)} карт.")
        print(cards) #тут не работает метот жоин, почему что это кортеж внутри списка
        print()
    
deck = Deck_cards()
print(f"в колоде {len(cards)} карт: ")
print("так выглядит колода изначально: ", cards)
print()