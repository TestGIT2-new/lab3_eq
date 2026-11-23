import sys
sys.path.append("src")
from json_int import zet3

# Создаем функцию запуска интеграционных тестов
def zet4():
    # Тест 1: два корня (D > 0)
    r1 = zet3({"k_a": "1", "k_b": "-3", "k_c": "2"})
    assert r1["roots"] == [2.0, 1.0] and r1["check_ok"] is True

    # Тест 2: один корень (D = 0)
    r2 = zet3({"k_a": "1", "k_b": "-2", "k_c": "1"})
    assert r2["roots"] == [1.0] and r2["check_ok"] is True

    # Тест 3: нет корней (D < 0)
    r3 = zet3({"k_a": "1", "k_b": "1", "k_c": "5"})
    assert r3["roots"] == [] and r3["check_ok"] is False

    # Тест 4: граничный случай (a = 0)
    r4 = zet3({"k_a": "0", "k_b": "2", "k_c": "1"})
    assert "error" in r4

    print("Все 4 интеграционных теста пройдены!")

zet4()
