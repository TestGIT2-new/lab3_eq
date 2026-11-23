# Создаем функцию проверки корней подстановкой
def fun3(a, b, c, roots):
    if not roots:
        return False
    # Подставляем каждый корень в ax^2 + bx + c = 0
    for x in roots:
        res = a * (x ** 2) + b * x + c
        if abs(res) > 0.001:
            return False
    return True
