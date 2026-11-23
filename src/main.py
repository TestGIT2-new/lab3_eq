from mod1 import fun1
from mod2 import fun2
from mod3 import fun3

# Создаем главную функцию интеграции (прямой вызов)
def zet1():
    data = fun1()
    if data is None:
        return
    a, b, c = data
    roots = fun2(a, b, c)
    # Ловим ошибку, если a = 0
    if isinstance(roots, str):
        print(roots)
        return
    print("Корни:", roots)
    # Проверяем корни через mod3
    if roots:
        print("Проверка подстановкой:", fun3(a, b, c, roots))
    else:
        print("Корней нет")

zet1()
