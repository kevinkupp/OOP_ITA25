"""Simple Poker implementation."""


class Card:
    """A card in a poker game."""

    def __init__(self, value, suit):
        """Initialize Card."""
        self.value = value
        self.suit = suit

    def __repr__(self):
        """Return a string representation of the card."""
        return f"{self.value} of {self.suit}"


class Hand:
    """The hand in a poker game."""

    suits = ["diamonds", "clubs", "hearts", "spades"]
    values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    values_dict = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 11, "Q": 12, "K": 13, "A": 14}

    def __init__(self):
        """Initialize Hand."""
        self.poker_cards = []

    def can_add_card(self, card: Card) -> bool:
        """Check for card validity."""
        if card.suit not in self.suits or card.value not in self.values:
            return False

        if len(self.poker_cards) >= 5:
            return False

        for some_card in self.poker_cards:
            if some_card.suit == card.suit and some_card.value == card.value:
                return False

        return True

    def add_card(self, card: Card):
        """Add a card to hand."""
        if self.can_add_card(card):
            self.poker_cards.append(card)

    def can_remove_card(self, card: Card):
        """Check if a card can be removed from hand."""
        return card in self.poker_cards

    def remove_card(self, card: Card):
        """Remove a card from hand."""
        if self.can_remove_card(card):
            self.poker_cards.remove(card)

    def get_cards(self):
        """Return a list of cards as objects."""
        return self.poker_cards

    def is_straight(self):
        """Determine if the hand is a straight."""
        if len(self.poker_cards) < 5:
            return False

        # Sorteerime väärtused numbritena, et kontrollida järjestust
        v_list = sorted([self.values_dict[c.value] for c in self.poker_cards])

        for i in range(len(v_list) - 1):
            if v_list[i] + 1 != v_list[i + 1]:
                return False
        return True

    def is_flush(self):
        """Determine if the hand is a flush."""
        if len(self.poker_cards) < 5:
            return False
        first_suit = self.poker_cards[0].suit
        return all(card.suit == first_suit for card in self.poker_cards)

    def is_straight_flush(self):
        """Determine if the hand is a straight flush."""
        return self.is_straight() and self.is_flush()

    def is_full_house(self):
        """Determine if the hand is a full house."""
        if len(self.poker_cards) < 5:
            return False
        counts = self._get_value_counts()
        return set(counts.values()) == {2, 3}

    def is_four_of_a_kind(self):
        """Determine if there are four cards of the same value."""
        counts = self._get_value_counts()
        return 4 in counts.values()

    def is_three_of_a_kind(self):
        """Determine if there are three cards of the same value."""
        counts = self._get_value_counts()
        return 3 in counts.values()

    def is_pair(self):
        """Determine if there is a pair."""
        counts = self._get_value_counts()
        return 2 in counts.values()

    def _get_value_counts(self):
        """Count occurrences of each card value."""
        counts = {}
        for card in self.poker_cards:
            counts[card.value] = counts.get(card.value, 0) + 1
        return counts

    def get_hand_type(self):
        """Return a string representation of the hand type."""
        if len(self.poker_cards) < 5:
            return None

        # Järjekord on kriitiline: alusta tugevaimast
        if self.is_straight_flush():
            return "straight flush"
        if self.is_four_of_a_kind():
            return "four of a kind"
        if self.is_full_house():
            return "full house"
        if self.is_flush():
            return "flush"
        if self.is_straight():
            return "straight"
        if self.is_three_of_a_kind():
            return "three of a kind"
        if self.is_pair():
            return "pair"
        return "high card"

    def __repr__(self):
        """Return a string representation of the hand."""
        # Joinime kaardid komadega eraldatud tekstiks
        cards_str = ", ".join(str(card) for card in self.poker_cards)
        h_type = self.get_hand_type()

        if h_type is None:
            return f"I'm holding {cards_str}"

        # Lisatud "cards:" ja kaartide loetelu ilma [] sulgudeta
        return f"I got a {h_type} with cards: {cards_str}"


if __name__ == "__main__":
    hand = Hand()
    cards = [Card("2", "diamonds"), Card("4", "spades"), Card("5", "clubs"), Card("3", "diamonds"), Card("6", "hearts")]
    [hand.add_card(card) for card in cards]
    assert hand.get_hand_type() == "straight"

    hand = Hand()
    cards = [Card("10", "diamonds"), Card("2", "diamonds"), Card("A", "diamonds"), Card("6", "diamonds"),
             Card("9", "diamonds")]
    [hand.add_card(card) for card in cards]
    assert hand.get_hand_type() == "flush"

    hand = Hand()
    cards = [Card("A", "hearts"), Card("A", "clubs"), Card("A", "spades"), Card("A", "diamonds"),
             Card("9", "diamonds")]
    [hand.add_card(card) for card in cards]
    assert hand.get_hand_type() == "four of a kind"