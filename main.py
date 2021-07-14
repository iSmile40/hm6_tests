from data import documents, directories


def people_document(doc_number):
    for number in documents:
        if number["number"] == doc_number:
            num_doc = number["name"]
            return num_doc
    return "Такого номера нет"


def shelf_document(doc_number):
    for number in directories:
        if doc_number in directories[number]:
            return number
    return "Такого номера нет"


def show_document_info(document):
    doc_type = document['type']
    doc_number = document['number']
    doc_owner_name = document['name']
    print(f'"{doc_type}" "{doc_number}" "{doc_owner_name}"')


def list_database():
    print('Список всех документов:\n')
    for data in documents:
        show_document_info(data)
        print()


def add_command(a_type, number, name, shelf_directories):
    if shelf_directories not in directories:
        return "Такой полки не существует"
    if shelf_directories in directories:
        documents.append({"type": a_type, "number": number, "name": name})
        directories[shelf_directories].append(number)
        return "Документ успешно создан и добавлен на полку"


def delete_command(doc_number):
    for a, b in enumerate(documents):
        if b["number"] == doc_number:
            documents.pop(a)
    for key, value in directories.items():
        if doc_number in value:
            value.remove(doc_number)
            return "Документ успешно удален"
    return "Такого номера не существует"


def move_command(doc_number, shelf_directories):
    real_doc_number = False
    if shelf_directories not in directories:
        return "Такой полки не существует"
    for key, value in directories.items():
        if doc_number in value:
            real_doc_number = True
            directories[shelf_directories] += [doc_number]
            value.remove(doc_number)
        if real_doc_number:
            return "Документ успешно перемещен"
        else:
            return "Такого документа не существует"


def add_shelf(number_shelf):
    if number_shelf in directories:
        return "Такая полка уже существует"
    elif number_shelf not in directories:
        directories.setdefault(number_shelf, [])
        return "Новая полка создана"


def main():
    while True:
        print("Введите любую команду: p / s / l / a / d / m / as / exit")
        command = input('Введите команду: ')

        if command == 'p':
            number = input('Введите номер документа: ')
            print(people_document(number))

        elif command == "s":
            number = input('Введите номер документа: ')
            print(shelf_document(number))

        elif command == "l":
            list_database()

        elif command == "a":
            a_type = input("Введите тип документа: ")
            number = input("Введите номер документа: ")
            name = input("Введите ФИО кому принадлежит документ: ")
            shelf_directories = input("Введите номер полки, на которую необходимо положить номер документа: ")
            print(add_command(a_type, number, name, shelf_directories))

        elif command == "d":
            doc_number = input("Введите номер документа, который хотите удалить: ")
            print(delete_command(doc_number))

        elif command == "m":
            doc_number = input("Введите номер документа, который хотите переместить: ")
            shelf_directories = input("Введите номер полки, на которую хотите переместить: ")
            print(move_command(doc_number, shelf_directories))

        elif command == "as":
            number_shelf = input("Введите номер полки: ")
            print(add_shelf(number_shelf))

        elif command == "exit":
            break

        else:
            print("Вы ввели неверную команду, попробуйте еще раз")

if __name__ == '__main__':
   main()
