# TODO Напишите функцию для поиска индекса товара
def finder(items_list, find_item):
    ret = None
    for i in range(0, len(items_list)):
        if items_list[i] == find_item:
            if ret == None:
                ret = i
    return ret
items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for find_item in ['банан', 'груша', 'персик']:
    index_item = finder(items_list, find_item)  # TODO Вызовите функцию, что получить индекс товара
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")