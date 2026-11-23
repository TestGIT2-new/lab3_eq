from mod1 import fun1
from mod3 import fun3

# Создаем заглушку вместо среднего модуля
def zet_stub(a, b, c):
    print("Заглушка получила:", a, b, c)
    return [2.0, 1.0]

# Проверяем верхний модуль с заглушкой
data = fun1()
if data:
    print("Ответ заглушки:", zet_stub(*data))

# Драйвер проверяет нижний модуль напрямую
ok = fun3(1, -3, 2, [2.0, 1.0])
print("Драйвер проверил mod3:", ok)
