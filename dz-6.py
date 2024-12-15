 result = []

def divider(a, b):
    if a < b:
        raise ValueError("Первое число меньше второго.")
    if b > 100:
        raise IndexError("Второе число больше 100.")
    return a / b

data = {10: 2, 2: 5, "123": 4, 18: 0, 8: 4}

for key, value in data.items():  
    try:
        res = divider(key, value)
        result.append(res)
    except ZeroDivisionError:
        print(f"Ошибка деления на ноль для пары ({key}, {value}).")
    except TypeError:
        print(f"Ошибка типа данных для пары ({key}, {value}). Ключ и значение должны быть числами.")
    except ValueError as e:
        print(f"Ошибка значения для пары ({key}, {value}): {e}")
    except IndexError as e:
        print(f"Ошибка индекса для пары ({key}, {value}): {e}")
    except Exception as e:
        print(f"Неизвестная ошибка для пары ({key}, {value}): {e}")

print("Результат:", result)
