result = []

def divider(a, b):
    if a < b:
        print(f"Ошибка: {a} меньше, чем {b}.")
        return None
    if b > 100:
        print(f"Ошибка: {b} больше 100.")
        return None
    return a / b

data = {10: 2, 2: 5, "123": 4, 18: 0, 8: 4}

for key in data:
    try:
        # Попробуем выполнить деление
        res = divider(key, data[key])
        if res is not None:  # Если результат не равен None, добавим в список
            result.append(res)
    except ZeroDivisionError:
        print(f"Ошибка: деление на ноль для пары ({key}, {data[key]}).")
    except TypeError:
        print(f"Ошибка: неправильный тип данных для пары ({key}, {data[key]}).")
    except Exception as e:
        print(f"Неизвестная ошибка: {e} для пары ({key}, {data[key]}).")

print("Результат:", result)
