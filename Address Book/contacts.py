# класс Contact имеет следующие поля:
# Имя, фамилия, телефонный номер - обязательные поля;
# Избранный контакт - необязательное поле. По умолчанию False;
# Дополнительная информация(email, список дополнительных номеров, ссылки на соцсети) -
# необходимо использовать *args, **kwargs.
# Переопределить "магический" метод str для красивого вывода контакта.


class Contact:

    def __init__(self, first_name, second_name, phone, favorite=False, **add_data):
        self.base_first_name = first_name
        self.base_second_name = second_name
        self.base_phone = phone
        self.base_favorite = favorite
        self.__dict__.update(add_data)

    def __str__(self):
        print(f"Имя: {self.base_first_name}")
        print(f"Фамилия: {self.base_second_name}")
        print(f"Телефон: {self.base_phone}")
        if self.base_favorite:
            print(f"В избранных: есть")
        else:
            print(f"В избранных: нет")
        print(f"Дополнительная информация:")
        for key, value in self.__dict__.items():
            if key.startswith('base'):
                pass
            else:
                print('\t\t{} = {}'.format(key, value))