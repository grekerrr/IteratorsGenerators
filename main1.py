class Iterator1:

    def __init__(self, multi_list):
        # Хранение списка списков
        self.multi_list = multi_list

    def __iter__(self):
        # Итерация по списку
        self.iterators_queue = []  # список для добавления элементов очереди итераторов
        self.current_iterator = iter(self.multi_list)  # итератор для списка
        return self

    def __next__(self):
        # Следущий элемент списка списков
        while True:
            try:
                self.current_element = next(self.current_iterator)   # следующий элемент списка
            except StopIteration:  # исключение, ели следующего элемента нет
                if not self.iterators_queue:  # возвращаем исключение, если не осталось элементов в очереди
                    raise StopIteration
                else:
                    self.current_iterator = self.iterators_queue.pop()  # следующий элемент очереди
                    continue
            if isinstance(self.current_element, list):  # тип следующего элемента: список или нет
                self.iterators_queue.append(self.current_iterator)  # если список, то добавляем в очередь
                self.current_iterator = iter(self.current_element)  # и смещаем указатель текущего итератора
            else:  # если элемент не список, то возвращаем этот элемент
                return self.current_element


def flat_generator_enhanced(multi_list):
    """Генератор возврата эелементов из списка списков с любым уровнем вложености"""
    for elem in multi_list:
        if isinstance(elem, list):  # тип следующего элемента: список или нет
            for sub_elem in flat_generator_enhanced(elem):  # если список, то рекурсивно вызываем этот же генератор
                yield sub_elem
        else:
            yield elem  # если не список, то возвращаем этот элемент


if __name__ == '__main__':

    nested_list = [
        ['a', ['b'], 'c'],
        ['d', 'e', [[[[['f']]]]], 'h', False],
        [1, [[[2]]], None],
    ]

    print('Вызов расширенного итератора:')
    for item in Iterator1(nested_list):
        print(item)
    print()

    print('Вызов расширенного генератора:')
    for item in flat_generator_enhanced(nested_list):
        print(item)
    print()

    print('Вызов компрехеншен:')
    flat_list = [item for item in Iterator1(nested_list)]
    print(flat_list)
    print()
