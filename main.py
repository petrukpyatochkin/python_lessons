from lab_25_hw.city import City

while True:
    try:
        name = input("Введіть назву міста: ") or 'Невідоме місто'
        region = input("Введіть назву регіону: ") or 'Невідомий регіон'
        country = input("Введіть назву країни: ") or 'Невідома країна'
        population_input = input("Введіть кількість жителів у місті: ")
        postal_code = input("Введіть поштовий індекс міста: ") or '00000'
        phone_code = input("Введіть телефонний код міста: ") or '+0000'

        try:
            population = int(population_input) if population_input else 0
        except ValueError:
            print("Кількість жителів має бути числом. Спробуйте ще раз.")
            continue

        city = City(name, region, country, population, postal_code, phone_code)

        city.display_info()

        while True:
            print("\nМеню:")
            print("1. Оновити інформацію про місто")
            print("2. Вийти з програми")
            choice = input("Оберіть опцію: ")

            if choice == '1':
                new_name = input("Введіть нову назву міста або залиште пустим: ")
                new_region = input("Введіть нову назву регіону або залиште пустим: ")
                new_country = input("Введіть нову назву країни або залиште пустим: ")
                new_population_input = input("Введіть нову кількість жителів у місті або залиште пустим: ")
                new_postal_code = input("Введіть новий поштовий індекс міста або залиште пустим: ")
                new_phone_code = input("Введіть новий телефонний код міста або залиште пустим: ")

                new_population = int(new_population_input) if new_population_input else city.population

                city.update_info(
                    name=new_name or city.name,
                    region=new_region or city.region,
                    country=new_country or city.country,
                    population=new_population,
                    postal_code=new_postal_code or city.postal_code,
                    phone_code=new_phone_code or city.phone_code
                )
                city.display_info()

            elif choice == '2':
                print("Вихід з програми.")
                break
            else:
                print("Невідома опція, спробуйте ще раз.")
    except Exception as e:
        print(f"Сталася помилка: {e}")
        continue

    user_choice = input("\nНатисніть Enter, щоб повернутися до головного меню, або будь-яку іншу клавішу, щоб вийти: ")
    if user_choice:
        break