# класс PhoneBook:
# Название телефонной книги - обязательное поле;
# Телефонная книга должна работать с классами Contact.
# Методы:
#
# Вывод контактов из телефонной книги;
# Добавление нового контакта;
# Удаление контакта по номеру телефона;
# Поиск всех избранных номеров;
# Поиск контакта по имени и фамилии.

from pprint import pprint
from contacts import Contact


class PhoneBook:

    def __init__(self, name):
        self.name = name
        self.contacts = []

    def print_book(self):
        """
        Вывод контактов из телефонной книги
        """
        for each in self.contacts:
            each.__str__()

    def add_new(self, name):
        """
        Добавление нового контакта
        """
        self.contacts.append(name)

    def remove(self, number):
        """
        Удаление контакта по номеру телефона
        """
        for each in self.contacts:
            if each.base_phone == number:
                self.contacts.remove(each)

    def search_fav(self):
        """
        Поиск всех избранных номеров
        """
        for each in self.contacts:
            if each.base_favorite:
                each.__str__()

    def search_by(self, fname, sname):
        """
        Поиск контакта по имени и фамилии
        """
        for each in self.contacts:
            if each.base_first_name == fname and each.base_second_name == sname:
                each.__str__()
