class WSModel:
    def __init__(self):
        self._altitude = None
        self._luminosity = None
        self._humidity = None
        self._pressure = None
        self._temperature = None

    @property
    def altitude(self) -> float:
        """
        :return: Высота точки измерения относительно места установки метеостанции, м
        """
        return self._altitude

    @altitude.setter
    def altitude(self, value: float):
        """
        :param value: Высота точки измерения относительно места установки метеостанции, м
        """
        self._altitude = value

    @property
    def luminosity(self) -> float:
        """
        :return: Уровень освещенности, люмен
        """
        return self._luminosity

    @luminosity.setter
    def luminosity(self, value: float):
        """
        :param value: Уровень освещенности, люмен
        """
        self._luminosity = value

    @property
    def humidity(self) -> float:
        """
        :return: Относительная влажность, %
        """
        return self._humidity

    @humidity.setter
    def humidity(self, value: float):
        """
        :param value: Относительная влажность, %
        """
        self._humidity = value

    @property
    def pressure(self) -> float:
        """
        :return: Давление, мм.рт.ст
        """
        return self._pressure

    @pressure.setter
    def pressure(self, value: float):
        """
        :param value: Давление, мм.рт.ст
        """
        self._pressure = value

    @property
    def temperature(self) -> float:
        """
        :return: Температура, *С
        """
        return self._temperature

    @temperature.setter
    def temperature(self, value: float):
        """
        :param value: Температура, *С
        """
        self._temperature = value
