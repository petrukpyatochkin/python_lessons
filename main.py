from lab_25_hw.сountry import Country

while True:
    try:
        name = input("Введіть назву країни: ") or 'Невідома країна'
        continent = input("Введіть назву континенту: ") or 'Невідомий континент'
        population_input = input("Введіть кількість жителів країни: ")
        phone_code = input("Введіть телефонний код країни: ") or '+000'
        capital = input("Введіть назву столиці країни: ") or 'Невідома столиця'
        cities = input("Введіть назви міст країни, розділивши їх комою: ").split(',')

        population = int(population_input) if population_input else 0

        country = Country(name, continent, population, phone_code, capital, cities)

        country.display_info()

        while True:
            print("\nМеню:")
            print("1. Оновити інформацію про країну")
            print("2. Додати місто")
            print("3. Видалити місто")
            print("4. Показати інформацію про країну")
            print("5. Вийти з програми")
            choice = input("Оберіть опцію: ")

            if choice == '1':
                new_name = input("Введіть нову назву країни або залиште пустим: ")
                new_continent = input("Введіть новий континент або залиште пустим: ")
                new_population_input = input("Введіть нову кількість жителів або залиште пустим: ")
                new_population = int(new_population_input) if new_population_input else country.population
                new_phone_code = input("Введіть новий телефонний код або залиште пустим: ")
                new_capital = input("Введіть нову назву столиці або залиште пустим: ")
                country.update_info(
                    name=new_name or country.name,
                    continent=new_continent or country.continent,
                    population=new_population,
                    phone_code=new_phone_code or country.phone_code,
                    capital=new_capital or country.capital
                )
                print("Інформацію оновлено.")

            elif choice == '2':
                new_city = input("Введіть назву міста, яке бажаєте додати: ")
                country.add_city(new_city)
                print(f"Місто {new_city} додано.")

            elif choice == '3':
                city_to_remove = input("Введіть назву міста, яке бажаєте видалити: ")
                country.remove_city(city_to_remove)
                print(f"Місто {city_to_remove} видалено.")

            elif choice == '4':
                country.display_info()

            elif choice == '5':
                print("Вихід з програми.")
                break

            else:
                print("Невідома опція, спробуйте ще раз.")

            if choice == '5':
                break

    except ValueError as e:
        print(f"Помилка введення числових даних: {e}")
    except Exception as e:
        print(f"Сталася помилка: {e}")
        # В цьому місці ми використовуємо continue, щоб повернутися до початку основного циклу
        continue

    user_choice = input("\nНатисніть Enter, щоб продовжити, або будь-яку іншу клавішу, щоб вийти: ")
    if user_choice:
        break
