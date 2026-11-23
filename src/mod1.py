# Создаем функцию ввода коэффициентов
def fun1():
    try:
        # Вводим числа и переводим в float
        a = float(input("a = "))
        b = float(input("b = "))
        c = float(input("c = "))
        return a, b, c
    except ValueError:
        # Если ввели буквы вместо цифр
        print("Ошибка: нужно вводить числа")
        return None
