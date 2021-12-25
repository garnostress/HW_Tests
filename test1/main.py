import json

with open('documents.json', 'r+', encoding='utf-8') as f:
    documents = json.load(f)
with open('directories.json', 'r+', encoding='utf-8') as f:
    directories = json.load(f)


class Secretery:
    def __init__(self, name, password):
        self.name = name
        self.password = password

    def get_number_name(self, number):
        self.number = number
        for human in documents:
            if self.number == human["number"]:
                print(human['name'])
                return human['name']
        print('Документ не найден')
        return None

    def get_number_dir(self, number):
        self.number = number
        for shelf in directories:
            if self.number in directories[shelf]:
                print(f'Документ номер {self.number} найден на полке номер {shelf}')
                return shelf
        print(f'Документ c номером {self.number} не найден')
        return None

    def get__all_list(self):
        data = []
        count = 1
        while count <= len(documents):
            for human in documents:
                print(human)
                self.type1 = human["type"]
                self.number = human["number"]
                self.name = human["name"]
                self.string_doc = f'{self.type1} "{self.number}" "{self.name}"'
                data.append(self.string_doc)
                # print(data)
                count += 1
        return data

    def add_doc(self, type_doc, number, name, shelf):
        self.type_doc = type_doc
        self.number = number
        self.name = name
        self.shelf = shelf

        if self.shelf not in directories.keys():  # проверяем на наличие полки
            print('Полки с таким номером не существует')
            return None

        new_human = {}  # создаем словарь с новыми данными и добавляем в общий каталог
        new_human["type"] = self.type_doc
        new_human["number"] = self.number
        new_human["name"] = self.name
        documents.append(new_human)

        directories[self.shelf] += [self.number]  # добавляем документ на необходимую полку
        print(f'В каталог добавлена новая запись {new_human}')
        print(f'Документ №{self.number} добавлен на полку {self.shelf}')
        return new_human


secretery = Secretery('Bill', '1234567')