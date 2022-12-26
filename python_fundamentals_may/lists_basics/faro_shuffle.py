# deck_of_cards = input().split()
# number_of_shuffles = int(input())
# for shuffle in range(number_of_shuffles):
#     final_deck = []
#     middle_of_the_deck = len(deck_of_cards) // 2
#     left_part = deck_of_cards[0:middle_of_the_deck]
#     right_part = [middle_of_the_deck::]
#     for index_of_the_card in range(len(left_part)):

list_of_cards = input().split(" ")
number_of_shuffles = int(input())

for shuffle in range(number_of_shuffles):
    final_list = []
    middle = len(list_of_cards) // 2
    left_part = list_of_cards[:middle]
    right_part = list_of_cards[middle::]
    for index in range(len(left_part)):
        final_list.append(left_part[index])
        final_list.append(right_part[index])
    list_of_cards = final_list
print(list_of_cards)