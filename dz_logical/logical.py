age = int(input("Укажите свой возраст: "))
is_citizen = input("Вы гражданин страны? (да/нет): ").lower() == "да"
is_disqualified = input("Вы дисквалифицированы? (да/нет): ").lower() == "да"

if age >= 18 and is_citizen and not is_disqualified:
    print("Результат: Вам разрешено голосовать")
else:
    print("Результат, вам запрещено голосовать")