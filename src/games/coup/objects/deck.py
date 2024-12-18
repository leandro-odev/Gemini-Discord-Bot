import random
from games.coup.objects.card import Card

class Deck:
    def __init__(self, gamemode):
        base_cards = [
            Card("duque"), Card("duque"), Card("duque"),
            Card("condesa"), Card("condesa"), Card("condesa"),
            Card("capitao"), Card("capitao"), Card("capitao"),
            Card("embaixador"), Card("embaixador"), Card("embaixador"),
            Card("assassino"), Card("assassino"), Card("assassino")
        ]
        expansion_cards = base_cards + [
            Card("duque"), Card("condesa"), Card("capitao"),
            Card("embaixador"), Card("assassino")
        ]
        self.cards = base_cards if gamemode == "base" else expansion_cards
        self.shuffle()

    def __str__(self):
        cards = ", ".join(str(card) for card in self.cards)
        return f"Baralho: {cards}"

    def shuffle(self):
        random.shuffle(self.cards)
    
    def get_card(self):
        if not self.cards:
            return None
        return self.cards.pop(0)

    def return_card(self, card):
        self.cards.append(card)