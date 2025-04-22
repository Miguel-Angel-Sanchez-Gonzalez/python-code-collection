# Solución al ejercicio de Exercism: "Lists"
# Enunciado tomado de Exercism.org

def get_rounds(number):
    list_rounds = []
    for i in range(3):
        list_rounds.append(number + i)
    return list_rounds
  
# print(get_rounds(27))

def concatenate_rounds(rounds_1, rounds_2):
    return rounds_1 + rounds_2
  
# print(concatenate_rounds([27, 28, 29], [35, 36]))



def list_contains_round(rounds, number):
    return number in rounds
  
  
# print(list_contains_round([27, 28, 29, 35, 36], 29))

# print(list_contains_round([27, 28, 29, 35, 36], 30))

def card_average(hand):
    sum_cards = sum(hand)
    return sum_cards / len(hand)
  
# print(card_average([5, 6, 7]))


def approx_average_is_average(hand):
    average = card_average(hand)
    approx_average = (hand[0] + hand[-1]) / 2
    middle_card = hand[len(hand) // 2]
    return approx_average == average or middle_card == average
  
# print(approx_average_is_average([1, 2, 3]))
# print(approx_average_is_average([2, 3, 4, 8, 8]))
# print(approx_average_is_average([1, 2, 3, 5, 9]))


def average_even_is_average_odd(hand):

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

