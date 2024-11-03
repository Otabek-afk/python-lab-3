# TODO Напишите функцию find_common_participants

def find_common_participants(G1, G2, A3 = ','):
    G1 = list(G1.split(A3))
    G2 = list(G2.split(A3))
    G3 = list(set(G1).intersection(G2))
    G3.sort()
    return G3

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой

print(find_common_participants(participants_first_group, participants_second_group, '|'))


