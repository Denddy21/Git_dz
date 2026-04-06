# Сложение
print("=== Сложение ===")
try:
    a = float(input("Введите первое число: "))
    b = float(input("Введите второе число: "))
    print(f"Результат сложения: {a + b}")
except ValueError:
    print("Ошибка: Введите корректное число")

# Вычитание
print("\n=== Вычитание ===")
try:
    a = float(input("Введите первое число: "))
    b = float(input("Введите второе число: "))
    print(f"Результат вычитания: {a - b}")
except ValueError:
    print("Ошибка: Введите корректное число")

# Умножение
print("\n=== Умножение ===")
try:
    a = float(input("Введите первое число: "))
    b = float(input("Введите второе число: "))
    print(f"Результат умножения: {a * b}")
except ValueError:
    print("Ошибка: Введите корректное число")

# Деление
print("\n=== Деление ===")
try:
    a = float(input("Введите первое число: "))
    b = float(input("Введите второе число: "))
    print(f"Результат деления: {a / b}")
except ZeroDivisionError:
    print("Деление на 0 невозможно")
except ValueError:
    print("Ошибка: Введите корректное число")