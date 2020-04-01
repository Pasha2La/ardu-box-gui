from api import driver
from .WSModel import WSModel


class WSService:
    def __init__(self):
        # инициализируем загрузку драйвера при подключении устройства
        driver.startup()
        self._model = WSModel()

    def _sync(self):
        """
        Синхронизирует данные модели с данными от датчиков
        """
        # загружаем данные от датчика в список
        # элементы списка соответствуют шаблону "КодПараметра:ЗначениеПараметра"
        values = driver.read_line().split(' ')
        # заполняем модель полученными данными
        try:
            self._model.luminosity = float(values[0].split(':')[-1])
            self._model.temperature = float(values[1].split(':')[-1])
            self._model.humidity = float(values[2].split(':')[-1])
            self._model.pressure = float(values[3].split(':')[-1])
            self._model.altitude = float(values[4].split(':')[-1])
        except IndexError as e:
            print("Данные от датчиков представлены не в полном объеме")
            print(e)

    def get_model(self):
        """
        :return: Модель с данными из датчиков
        """
        self._sync()
        return self._model