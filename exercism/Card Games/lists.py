def get_rounds(number):
    """Create a list containing the current and next two round numbers.

    :param number: int - current round number.
    :return: list - current round and the two that follow.
    """

    list_rounds = []
    for i in range(3):
        list_rounds.append(number + i)
    return list_rounds
  
# print(get_rounds(27))

def concatenate_rounds(rounds_1, rounds_2):
    """Concatenate two lists of round numbers.

    :param rounds_1: list - first rounds played.
    :param rounds_2: list - second set of rounds played.
    :return: list - all rounds played.
    """

    return rounds_1 + rounds_2
  
# print(concatenate_rounds([27, 28, 29], [35, 36]))



def list_contains_round(rounds, number):
    """Check if the list of rounds contains the specified number.

    :param rounds: list - rounds played.
    :param number: int - round number.
    :return: bool - was the round played?
    """

    return number in rounds
  
  
# print(list_contains_round([27, 28, 29, 35, 36], 29))

# print(list_contains_round([27, 28, 29, 35, 36], 30))

def card_average(hand):
    """Calculate and returns the average card value from the list.

    :param hand: list - cards in hand.
    :return: float - average value of the cards in the hand.
    """

    sum_cards = sum(hand)
    return sum_cards / len(hand)
  
# print(card_average([5, 6, 7]))


def approx_average_is_average(hand):
    """Return if the (average of first and last card values) OR ('middle' card) == calculated average.

    :param hand: list - cards in hand.
    :return: bool - does one of the approximate averages equal the `true average`?
    """

    average = card_average(hand)
    approx_average = (hand[0] + hand[-1]) / 2
    middle_card = hand[len(hand) // 2]
    return approx_average == average or middle_card == average
  
# print(approx_average_is_average([1, 2, 3]))
# print(approx_average_is_average([2, 3, 4, 8, 8]))
# print(approx_average_is_average([1, 2, 3, 5, 9]))


def average_even_is_average_odd(hand):
    """Return if the (average of even indexed card values) == (average of odd indexed card values).

    :param hand: list - cards in hand.
    :return: bool - are even and odd averages equal?
    """

    even_cards = hand[1::2]
    odd_cards = hand[0::2]
    
    # print(f"pares {even_cards}")
    # print(f"impares {odd_cards}")
    
    average_even_cards = sum(even_cards) / len(even_cards)
    average_odd_cards = sum(odd_cards) / len(odd_cards)
    
    return average_even_cards == average_odd_cards
  
  
# print(average_even_is_average_odd([1, 2, 3]))
# print(average_even_is_average_odd([1, 2, 3, 4]))

def maybe_double_last(hand):
    """Multiply a Jack card value in the last index position by 2.

    :param hand: list - cards in hand.
    :return: list - hand with Jacks (if present) value doubled.
    """
    last_card = hand[-1]
    if last_card == 11:
        print("entre")
        last_card *= 2
        hand.pop()
        hand.append(last_card)
        return hand

    return hand
  
hand = [5, 9, 10]
print(maybe_double_last(hand))

