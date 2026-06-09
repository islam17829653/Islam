from datetime import datetime

conversion_count = 0

while True:
    print("\n===== Конвертер =====")
    print("1. Км -> М")
    print("2. М -> Км")
    print("3. Кг -> Г")
    print("4. Г -> Кг")
    print("5. C -> F")
    print("6. F -> C")
    print("0. Шығу")

    choice = input("Таңдау: ")

    if choice == "0":
        print("\nБағдарлама аяқталды.")
        print(f"Жалпы орындалған конвертация саны: {conversion_count}")
        break

    try:
        if choice == "1":
            km = float(input("Км енгізіңіз: "))
            result = km * 1000
            print(f"\nНәтиже: {km} км = {result} м")

        elif choice == "2":
            m = float(input("М енгізіңіз: "))
            result = m / 1000
            print(f"\nНәтиже: {m} м = {result} км")

        elif choice == "3":
            kg = float(input("Кг енгізіңіз: "))
            result = kg * 1000
            print(f"\nНәтиже: {kg} кг = {result} г")

        elif choice == "4":
            g = float(input("Г енгізіңіз: "))
            result = g / 1000
            print(f"\nНәтиже: {g} г = {result} кг")

        elif choice == "5":
            c = float(input("°C енгізіңіз: "))
            result = (c * 9 / 5) + 32
            print(f"\nНәтиже: {c}°C = {result}°F")

        elif choice == "6":
            f = float(input("°F енгізіңіз: "))
            result = (f - 32) * 5 / 9
            print(f"\nНәтиже: {f}°F = {result:.2f}°C")

        else:
            print("Қате! Менюдегі нөмірлердің бірін таңдаңыз.")
            continue

        conversion_count += 1

        print("\nКонвертация сәтті аяқталды")
        print("Уақыты:")
        print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    except ValueError:
        print("Қате! Сан енгізіңіз.")

        print("\nКонвертация сәтті аяқталды")
        print("Уақыты:")
        print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))