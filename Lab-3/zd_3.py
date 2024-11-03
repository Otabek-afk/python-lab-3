# TODO  Напишите функцию count_letters
def count_letters(text):
    textlist = []
    text = text.lower()
    for i in text:
        if i.isalpha():
            textlist += i
    setlist = list(set(textlist))
    newlist = []
    for i in textlist:
        for j in range(len(setlist)):
            if i == setlist[j]:
                newlist += i
                setlist[j] = ' '
    dict = {}
    for i in newlist:
        dict[i] = 0
    for i in newlist:
        for j in textlist:
            if i == j:
                dict[i] += 1
    return dict, newlist

# TODO Напишите функцию calculate_frequency

def calculate_frequency(dict, newlist):
    summ = 0
    for i in newlist:
        summ += dict[i]
    for i in newlist:
        dict[i] /= summ
        dict[i] = round(dict[i], 2)
    return dict

main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""

# TODO Распечатайте в столбик букву и её частоту в тексте

dict, newlist = count_letters(main_str)
dict = calculate_frequency(dict, newlist)
for i in newlist:
    print(f"{i}: {dict[i]:.2f}")
