def max_number(a,b):
    if a > b:
        return a
    else:
        return b
result = max_number(-1,-5)
print(result)

def empty_function():
    pass

def even_numbers( n ):
    for i in range(0, n + 1, 2 ):
        yield i

limit = 10
print(list(even_numbers(limit)))

def test():
    assert max_number(10,5) == 10, "Ошибка: 10 должно быть больше 5"
    assert max_number(2,8) == 8, "Ошибка: 8 должно быть больше 3"
    assert max_number(7,7) == 7, "Ошибка: при равных числах должно возвращаться само число"
    assert max_number(-1, -5) == -1, "Ошибка: -1 больше -5"

    print("Все тесты пройдены")
test()