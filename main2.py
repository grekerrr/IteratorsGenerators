class Iterator2:

    def __init__(self, multi_list):
        # Хранение списка списков
        self.multi_list = multi_list

    def __iter__(self):
        # Итерация по списку
        self.list_iter = iter(self.multi_list)  # итератор для списка
        self.nested_list = []  # вложенный список для добавления элементов
        self.cursor = -1  # смещение курсора за границу списка
        return self

    def __next__(self):
        # Следущий элемент списка списков
        self.cursor += 1
        if len(self.nested_list) == self.cursor:  # если курсор в конце вложенного списка, то "обнуляем" список и курсор
            self.nested_list = None
            self.cursor = 0
            while not self.nested_list:  # если вложенные списки закончились, то получаем stop iteration
                self.nested_list = next(self.list_iter)  # если  список пустой, то получаем следующий вложенный список
        return self.nested_list[self.cursor]


def flat_generator(my_list):
    # Генератор возврата элементов из списка списков с двойным уровнем вложенности
    for sub_list in my_list:
        for elem in sub_list:
            yield elem


if __name__ == '__main__':

    nested_list = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None],
    ]

    print('Вызов итератора:')
    for item in Iterator2(nested_list):
        print(item)
    print()

    print('Вызов компрехеншен:')
    flat_list = [item for item in Iterator2(nested_list)]
    print(flat_list)
    print()

    print('Вызов генератора:')
    for item in flat_generator(nested_list):
        print(item)
    print()
