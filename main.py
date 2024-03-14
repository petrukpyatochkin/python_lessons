from lab_25_hw.address import Address
from lab_25_hw.human import Human

while True:
    try:
        full_name = input("Введіть ПІБ: ") or 'Іваненко Іван Іванович'
        birth_date = input("Введіть дату народження (DD.MM.YYYY): ") or '01.01.1980'

        phone_input = input("Введіть номери телефону (можна ввести декілька номерів, розділивши їх комою): ")
        if not phone_input.strip():
            phone_numbers = ['+380501234567', '+380951234567']
        else:
            phone_numbers = [number.strip() for number in phone_input.split(',')]

        city = input("Введіть місто: ") or 'Київ'
        country = input("Введіть країну: ") or 'Україна'
        address_line = input("Введіть адресу: ") or 'Вул. Хрещатик, 1'

        address_obj = Address(
            city=city,
            country=country,
            address=address_line)

        person = Human(
            full_name=full_name,
            birth_date=birth_date,
            phone_numbers=phone_numbers,
            address=address_obj)

        person.display_info()

        while True:
            print("\nМеню:")
            print("1. Додати номер телефону")
            print("2. Видалити номер телефону")
            print("3. Оновити персональні дані")
            print("4. Оновити адресу")
            print("5. Показати повну інформацію")
            print("6. Вийти")

            choice = input("Оберіть дію: ")

            if choice == '1':
                new_phone = input("Введіть новий номер телефону: ")
                person.add_phone_number(new_phone)
            elif choice == '2':
                phone_to_remove = input("Введіть номер телефону для видалення: ")
                person.remove_phone_number(phone_to_remove)
            elif choice == '3':
                new_full_name = input("Введіть ПІБ: ")
                new_birth_date = input("Введіть нову дату народження (DD.MM.YYYY): ")
                person.update_human(
                    full_name=new_full_name,
                    birth_date=new_birth_date)
            elif choice == '4':
                new_city = input("Введіть нове місто: ")
                new_country = input("Введіть нову країну: ")
                new_address = input("Введіть нову адресу: ")
                person.update_address_info(city=new_city, country=new_country, address=new_address)
            elif choice == '5':
                person.display_info()
            elif choice == '6':
                print("Ви вийшли з програми.")
                break
            else:
                print("Невідома опція, спробуйте ще раз.")
    except Exception as e:
        print(f"Сталася помилка: {e}")
        continue

    user_choice = input("\nНатисніть Enter, щоб повернутися до головного меню, або будь-яку іншу клавішу, щоб вийти: ")
    if user_choice:
        break