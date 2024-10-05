class Car:
    def __init__(self, model, _vin, __numbers):
        self.model = model
        self._vin = _vin
        self.__numbers = __numbers
        self.__is_valid_vin()
        self.__is_valid_numbers()

    def __is_valid_vin(self):
        if not isinstance(self._vin, int):
            raise IncorrectVinNumber(f'У {self.model} Некорректный тип {type(self._vin)} номер')
        if self._vin < 1000000 or self._vin > 9999999:
            raise IncorrectVinNumber(f'У {self.model} Неверный диапазон для номера - {self._vin}')
        else:
            return True

    def __is_valid_numbers(self):
        if not isinstance(self.__numbers, str):
            raise IncorrectCarNumbers(f'Некорректный тип данных для номеров {type(self.__numbers)}')
        if len(self.__numbers) != 6:
            raise IncorrectCarNumbers(f'Неверная длина номера {self.__numbers}')
        else:
            return True


class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message


class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        self.message = message


# try:
#     f1 = Car('Model1', 1000000, 'f123dj')
#     f2 = Car('Model2', 1000000, 12)
# except IncorrectVinNumber as exc:
#     print(exc.message)
# except IncorrectCarNumbers as exc:
#     print(exc.message)
try:
    first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{first.model} успешно создан')

try:
    second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{second.model} успешно создан')

try:
    third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{third.model} успешно создан')
