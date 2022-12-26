count_of_groups = int(input())
count_musala = 0
count_montblanc = 0
count_kili = 0
count_k2 = 0
count_everest = 0
sum_people = 0
for groups in range(1, count_of_groups + 1):
    people_current_group = int(input())
    sum_people += people_current_group
    if people_current_group <= 5:
        count_musala += people_current_group
    elif people_current_group <= 12:
        count_montblanc += people_current_group
    elif people_current_group <= 25:
        count_kili += people_current_group
    elif people_current_group <= 40:
        count_k2 += people_current_group
    else:
        count_everest += people_current_group
print(F"{(count_musala / sum_people) * 100:.2f}%")
print(F"{(count_montblanc / sum_people) * 100:.2f}%")
print(F"{(count_kili / sum_people) * 100:.2f}%")
print(F"{(count_k2 / sum_people) * 100:.2f}%")
print(F"{(count_everest / sum_people) * 100:.2f}%")