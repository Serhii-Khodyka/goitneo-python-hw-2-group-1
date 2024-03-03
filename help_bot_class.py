from collections import UserDict

def main():

    class Field:
        def __init__(self, value):
            self.value = value

        def __str__(self):
            return str(self.value)

    class Name(Field):
        def __init__(self, name):
            super().__init__(name)

    class Phone(Field):
        def __init__(self, phone):
            if not phone.isdigit() or len(phone) != 10:
                print(f"Invalid phone number {phone}. It must contain only digits and have a length of 10.")
                #use empty phone number
                phone = ""
            super().__init__(phone)

    class Record:
        def __init__(self, name):
            self.name = Name(name)
            self.phones = []

        def add_phone(self, phone):
            self.phones.append(Phone(phone))

        def remove_phone(self, phone):
            for i in self.phones:
                if i.value == phone:
                    self.phones.remove(i)
                    break

        def edit_phone(self, old_phone, new_phone):
            if not old_phone.isdigit() or len(old_phone) != 10:
                print(f"Invalid phone number {old_phone}. It must contain only digits and have a length of 10.")
                return
            if not new_phone.isdigit() or len(new_phone) != 10:
                print(f"Invalid phone number {new_phone}. It must contain only digits and have a length of 10.")
                return
            for i in self.phones:
                if i.value == old_phone:
                    i.value = new_phone
                    break

        def find_phone(self, phone):
            for i in self.phones:
                if i.value == phone:
                    return i.value

        def __str__(self):
            return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

    class AddressBook(UserDict):
        def add_record(self, record):
            self.data[record.name.value] = record

        def find(self, name):
            return self.data.get(name)

        def delete(self, name):
            if name in self.data:
                self.data.pop(name)


    # Створення нової адресної книги
    book = AddressBook()

    # Створення запису для John
    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")

    # Додавання запису John до адресної книги
    book.add_record(john_record)

    # Створення та додавання нового запису для Jane
    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    book.add_record(jane_record)

    # Виведення всіх записів у книзі
    for name, record in book.data.items():
        print(record)

    # Знаходження та редагування телефону для John
    john = book.find("John")
    john.edit_phone("1234567890", "1112223333")

    print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

    # Пошук конкретного телефону у записі John
    found_phone = john.find_phone("5555555555")
    print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

    # Видалення запису Jane
    book.delete("Jane")


if __name__ == "__main__":
    main()