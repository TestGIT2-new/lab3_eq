import json
from mod2 import fun2
from mod3 import fun3

# Создаем функцию маппинга: переводим строковые поля в float
def zet2(raw):
    return {"a": float(raw["k_a"]), "b": float(raw["k_b"]), "c": float(raw["k_c"])}

# Создаем функцию интеграции модулей через JSON-файл
def zet3(raw_input):
    # Записываем входные данные в data.json
    with open("data.json", "w", encoding="utf-8") as f:
        json.dump(raw_input, f)

    # Читаем JSON и выполняем маппинг
    with open("data.json", "r", encoding="utf-8") as f:
        m = zet2(json.load(f))

    # Решаем уравнение через mod2
    roots = fun2(m["a"], m["b"], m["c"])
    if isinstance(roots, str):
        return {"error": roots}

    # Проверяем корни через mod3 и сохраняем ответ в result.json
    ok = fun3(m["a"], m["b"], m["c"], roots) if roots else False
    out = {"a": m["a"], "b": m["b"], "c": m["c"], "roots": roots, "check_ok": ok}
    with open("result.json", "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2)
    return out

if __name__ == "__main__":
    res = zet3({"k_a": "1", "k_b": "-5", "k_c": "6"})
    print("Итог JSON:", res)
