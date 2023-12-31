traning_list = [
    ['Гарри Поттер и философский камень', 'Джоан Роулинг'],
    ['Убить пересмешника', 'Харпер Ли'],
    ['Война и мир', 'Лев Толстой'],
    ['Мцыри', 'Михаил Лермонтов']
]

def to_int(input_str: str = None) -> int:
    try:
        return int(input_str)
    except ValueError:
        error_input_format()
        return None

def error_input_format():
    """Вывод ошибки: Неверный формат ввода!"""

    print("Неверный формат ввода!")


def help() -> str:
    """Получение справки о доступных командах"""

    commands_list = ['Вывести - просмотреть весь список', 'Значение - просмотреть значение элемента в списке', 'Добавить - добавить элемент в список', 'Удалить - удалить элемент из списка', 'Изменить - изменить значение элемента в списке', 'Стоп - завершить работу программы']

    return "Список команд для работы с программой:" + "\n" + "\n".join(commands_list)


def view_list() -> list:
    """Получние содержимого списка книг"""

    return traning_list


def add_element(idx: str or int = None, element: list = None):
    """Добавить элемент в список книг"""

    element = [str(element[0]).lower().title(), str(element[1])]

    if idx is None or element is None:
        error_input_format()
        return

    try:
        idx = int(idx)
    except ValueError:
        if idx.lower() not in ["начало", "конец"]:
            error_input_format()
            return

    if idx == "начало":
        traning_list.insert(0, element)
    elif idx == "конец":
        traning_list.append(element)
    elif 0 <= idx <= len(traning_list):
        traning_list.insert(idx - 1, element)
    else:
        error_input_format()
        return


def view_element(idx: int) -> list:
    """Получение информации о опрелённой книге из списка по индексу"""

    return traning_list[idx]


def delete_element(idx: int = None) -> list:
    """Удаление информации и книге из списка по инфексу"""

    if idx != None:
        return traning_list.pop(idx)
    else:
        error_input_format()


def change_element(idx: int = None, element: list = None):
    """Изменить информацию о книге по индексу"""

    element = [str(element[0]).lower().title(), str(element[1])]

    if idx is None or element is None:
        error_input_format()
        return

    traning_list[idx] = element


def main():
    while True:
        print(help())

        commands = input('Введите команду: ').lower().strip()

        if "вывести" in commands:
            print(view_list())
        elif "значение" in commands:
            index_number = int(input("Введите номер элемента: ").lower()) - 1

            if 0 <= index_number <= len(traning_list):
                print(f"Элемент под номером {index_number + 1}: \n Название: {view_element(index_number)[0]} \n Автор: {view_element(index_number)[1]}")
            else:
                print(f"Элемента с номером {index_number} нет в списке")
        elif "добавить" in commands:
            name_element = str(input(
                "Введите добавляемый элемент в формате: название, автор ('строка,строка'): "))
            if [str(name_element.split(",")[0]).lower().title(), str(name_element.split(",")[1])] in traning_list:
                print(f"Данный элемент уже состоит в списке!")
                continue

            index_number = input(
                'Введите команду: начало - для добавления в начало списка, конец - для добавления в конец списка или номер позиции (число) - для добавления в указанную позицию: ').lower().strip()

            if name_element == "" or name_element.count(",") != 1 or ("" in name_element.split(",")):
                error_input_format()
            else:
                add_element(index_number, (name_element).split(","))
                print(f"Элемент {name_element} добавлен. Список обновлен: \n{
                      traning_list}")
        elif "удалить" in commands:
            index_number = input("Введите индекс удаляемого элемента: ")
            if 0 <= index_number <= len(traning_list):
                index_number = int(index_number)
                if 0 <= index_number <= len(traning_list):
                    print(f"Элемент {delete_element(index_number)} успешно удалён!")
                else:
                    print(f"Элемента с номером {index_number} нет в списке")
            else:
                error_input_format()
        elif "изменить" in commands:
            index_number = input(f"{view_list()}\n Введите номер элемента: ")

            if (index_number := to_int(index_number)) == None:
                continue
            
            index_number -= 1

            if not (0 <= index_number <= len(traning_list)):
                print(f"Элемента с данным номером нет в списке")

            name_element = str(input("Введите новый элемент в формате: название, автор ('строка,строка'): "))
            if name_element == "" or name_element.count(",") != 1 or ("" in name_element.split(",")):
                error_input_format()
            else:
                change_element(index_number, (name_element).split(","))
                print(f"Элемент {name_element} изменён. Список обновлен: \n{view_list()}")

        elif "стоп" in commands:
            break
        else:
            print(f"Ошибка: Команда [{commands}] не распознана!")


if __name__ == "__main__":
    main()
