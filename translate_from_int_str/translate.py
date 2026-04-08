words = ["One", "Two", "Three", "Four", "Five"]
user_input = input("Введите число от 1 до 5: ")

try:
    num = int(user_input)

    if 1 <= num <= 5:
        index = num - 1
        print(f"Соответствующее слово: {words[index]}")
    else:
        print("Ошибка: число вне диапазона (введите от 1 до 5).")
except ValueError:
    print("Ошибка: вы ввели не целое число.")
