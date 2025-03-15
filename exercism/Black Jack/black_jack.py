"""Functions to help play and score a game of blackjack."""

def value_of_card(card):
    """Determine the scoring value of a card.

    :param card: str - given card.
    :return: int - value of a given card.  See below for values.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """

    if card in {'J', 'Q', 'K'}:
        return 10
    elif card == 'A' :
        return 1
    try:
        return int(card)
    except ValueError:
        return None


def higher_card(card_one, card_two):
    """Determine which card has a higher value in the hand.

    :param card_one, card_two: str - cards dealt in hand.  See below for values.
    :return: str or tuple - resulting Tuple contains both cards if they are of equal value.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """


    def valor_carta(card):
        if card in {'J', 'Q', 'K'}:
            return 10
        elif card == 'A':
            return 1
        else:
            try:
                return int(card)
            except ValueError:
                return None 

    temp_card_one = valor_carta(card_one)
    temp_card_two = valor_carta(card_two)

    if temp_card_one is None or temp_card_two is None:
        return None

    if temp_card_one == temp_card_two:
        return card_one, card_two
    elif temp_card_one > temp_card_two:
        return card_one

    return card_two



def value_of_ace(card_one, card_two):
    """Calculate the most advantageous value for the ace card.

    :param card_one, card_two: str - card dealt. See below for values.
    :return: int - either 1 or 11 value of the upcoming ace card.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """

    
    def valor_carta(card):
        if card in {'J', 'Q', 'K'}:
            return 10
        elif card == 'A':
            return 11
        else:
            try:
                return int(card)
            except ValueError:
                return None

    temp_card_one = valor_carta(card_one)
    temp_card_two = valor_carta(card_two)

    if temp_card_one + temp_card_two + 11 > 21:
        return 1
    else: 
        return 11


def is_blackjack(card_one, card_two):
    """Determine if the hand is a 'natural' or 'blackjack'.

    :param card_one, card_two: str - card dealt. See below for values.
    :return: bool - is the hand is a blackjack (two cards worth 21).

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """

    face_cards = {'J', 'Q', 'K', '10'}
    ace_card = 'A'

    hand = {card_one, card_two}

    return ace_card in hand and any(card in face_cards for card in hand)


def can_split_pairs(card_one, card_two):
    """Determine if a player can split their hand into two hands.

    :param card_one, card_two: str - cards dealt.
    :return: bool - can the hand be split into two pairs? (i.e. cards are of the same value).
    """

    
    def value_of_cards(card_temp):
        if card_temp in {'J','Q', 'K'}:
            return 10
        else :
            return card_temp
        
    return value_of_card(card_one) == value_of_card(card_two)

        
    


def can_double_down(card_one, card_two):
    """Determine if a blackjack player can place a double down bet.

    :param card_one, card_two: str - first and second cards in hand.
    :return: bool - can the hand can be doubled down? (i.e. totals 9, 10 or 11 points).
    """

    pass

can_split_pairs('10','A')
