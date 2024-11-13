# Замість списку створимо один словник для розкладу
train_schedule = {
    332: {"Призначення": "Київ - Харків", "Прибуття": "12:43", "Відправлення": "12:57"},
    340: {"Призначення": "Київ - Суми", "Прибуття": "17:23", "Відправлення": "17:33"},
    366: {"Призначення": "Харків - Дніпро", "Прибуття": "10:15", "Відправлення": "10:30"},
    348: {"Призначення": "Львів - Херсон", "Прибуття": "09:23", "Відправлення": "09:33"},
    320: {"Призначення": "Запоріжжя - Київ", "Прибуття": "19:53", "Відправлення": "20:05"},
    365: {"Призначення": "Львів - Одеса", "Прибуття": "14:43", "Відправлення": "14:55"},
    387: {"Призначення": "Чернігів - Дніпро", "Прибуття": "16:33", "Відправлення": "16:44"},
    390: {"Призначення": "Полтава - Суми", "Прибуття": "13:05", "Відправлення": "13:19"},
    321: {"Призначення": "Суми - Львів", "Прибуття": "20:20", "Відправлення": "20:30"},
    356: {"Призначення": "Київ - Луцьк", "Прибуття": "17:55", "Відправлення": "18:03"}
}

def print_schedule(schedule):
    print("Розклад поїздів:")
    for train_number, details in schedule.items():
        print(f"Потяг номер: {train_number}, Призначення: {details['Призначення']}, "
              f"Прибуття: {details['Прибуття']}, Відправлення: {details['Відправлення']}")
    print()

def add_train(schedule, train_number, destination, arrival, departure):
    if train_number in schedule:
        print(f"Потяг з номером {train_number} вже існує.")
    else:
        schedule[train_number] = {"Призначення": destination, "Прибуття": arrival, "Відправлення": departure}
        print(f"Додано потяг: {train_number}.")

def delete_train(schedule, train_number):
    if train_number in schedule:
        del schedule[train_number]
        print(f"Видалено потяг: {train_number}.")
    else:
        print(f"Потяг {train_number} не знайдено.")

def sort_schedule(schedule):
    sorted_schedule = dict(sorted(schedule.items()))
    print("Відсортований розклад поїздів:")
    print_schedule(sorted_schedule)

def trains_at_station(schedule, current_time):
    current_hour, current_minute = map(int, current_time.split(':'))
    print("Поїзди на станції в даний момент:")
    for train_number, details in schedule.items():
        arrival_hour, arrival_minute = map(int, details["Прибуття"].split(':'))
        departure_hour, departure_minute = map(int, details["Відправлення"].split(':'))
        
        if (arrival_hour < current_hour or (arrival_hour == current_hour and arrival_minute <= current_minute)) and \
           (departure_hour > current_hour or (departure_hour == current_hour and departure_minute >= current_minute)):
            print(f"Потяг номер: {train_number}, Призначення: {details['Призначення']}")
    print()

def main():
    while True:
        print("Меню:")
        print("1. Виведення на екран всіх значень словника")
        print("2. Додавання нового запису до словника")
        print("3. Видалення запису із словника")
        print("4. Перегляд вмісту словника за відсортованими ключами")
        print("5. Визначити, які поїзди стоять на станції в визначений момент часу")
        print("0. Вихід з програми")
        choice = input("Введіть пункт меню: ")

        if choice == '1':
            print_schedule(train_schedule)
        elif choice == '2':
            try:
                train_number = int(input("Введіть номер потяга: "))
                destination = input("Введіть призначення: ")
                arrival = input("Введіть час прибуття (години:хвилини): ")
                departure = input("Введіть час відправлення (години:хвилини): ")
                add_train(train_schedule, train_number, destination, arrival, departure)
            except ValueError:
                print("Помилка вводу! Переконайтесь, що номер потяга є числом, а час введено у форматі години:хвилини.")
        elif choice == '3':
            try:
                train_number = int(input("Введіть номер потяга для видалення: "))
                delete_train(train_schedule, train_number)
            except ValueError:
                print("Помилка вводу! Введіть коректний номер потяга.")
        elif choice == '4':
            sort_schedule(train_schedule)
        elif choice == '5':
            current_time = input("Введіть поточний час (години:хвилини): ")
            trains_at_station(train_schedule, current_time)
        elif choice == '0':
            print("Вихід з програми.")
            break
        else:
            print("Неправильний вибір. Спробуйте ще раз.")

if __name__ == "__main__":
    main()
