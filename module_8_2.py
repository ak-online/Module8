def personal_sum(numbers):
    incorrect_data = 0
    result = 0
    # print('num - ', numbers)
    for i in numbers:
        # print('i - ', i)
        try:
            result += i
            # print('result - ', result)
        except TypeError:
            incorrect_data += 1
            print("Некорректный тип данных для подсчёта суммы - ", i)
    return result, incorrect_data


def calculate_average(numbers):
    try:
        # print('calculate_average(numbers):',personal_sum(numbers)[0] , len(numbers), personal_sum(numbers)[1])
        aver = personal_sum(numbers)[0] / (len(numbers) - personal_sum(numbers)[1])
        return aver
    except ZeroDivisionError as exc:
        print(f'ошибочка тут на ноль не надо делить то  -  {exc} .')
    except TypeError as exc:
        print(f'В numbers записан некорректный тип данных  -  {exc} .')


print(f'Результат 1: {calculate_average("1, 2, 3")}')  # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')  # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}')  # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')  # Всё должно работать
