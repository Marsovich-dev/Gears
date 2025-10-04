from gears.Mechanism import Mechanism
import math


class ConicalGeometry(Mechanism):
    parts = ['Ведущее колесо ', 'Ведомое колесо ']

    def __init__(self):

        self.critical_errors = []
        self.uncritical_errors = []
        self.z1 = None
        self.z2 = None
        self.mte = None
        self.b = None
        self.__set_input_data_dict()
        self.u = None
        self.mm = None
        self.dm1 = None
        self.dm2 = None
        self.de1 = None
        self.de2 = None
        self.Rm = None
        self.Re = None
        self.E = 90
        self.__set_output_data_dict()


    def set_input_data(self, z1, z2, mte, b):
        self.z1 = int(z1)
        self.z2 = int(z2)
        self.mte = float(mte)
        self.b = float(b)
        self.__set_input_data_dict()


    def __set_input_data_dict(self):
        self.input_data_dict = {
            'Число зубьев: z1, z2 ': [self.z1, self.z2],
            'Внешний окружной модуль: mte ': [self.mte],
            'Ширина зубчатого венца: b ': [self.b]
        }


    def get_input_data_dict(self):
        return self.input_data_dict


    def verify_input_data(self):
        self.critical_errors = []
        self.uncritical_errors = []
        if not (self.mte in (*self.first_modules, *self.second_modules)):
            self.critical_errors.append(self.ErrorTexts.Critical.nonexistent_module)
        elif self.mte in self.second_modules:
            self.uncritical_errors.append(self.ErrorTexts.UnCritical.irreverent_module)
        if self.z1 < 17 or self.z2 < 17:
            self.critical_errors.append(self.ErrorTexts.Critical.not_enough)


    def get_critical_errors(self):
        return self.critical_errors


    def get_uncritical_errors(self):
        return self.uncritical_errors


    def calculate(self, ndigits=3):
        self.verify_input_data()
        if self.critical_errors == []:
            self.u = round(self.z1 / self.z2, ndigits)
            self.Re = round(0.5 * self.mte * math.sqrt(self.z1 ** 2 + self.z2 ** 2), ndigits)
            self.mm = round(self.mte * (1 - 0.5 * (self.b / self.Re)), ndigits)
            self.Rm = round(0.5 * self.mm * math.sqrt(self.z1 ** 2 + self.z2 ** 2), ndigits)
            self.dm1 = round(self.mm * self.z1, ndigits)
            self.dm2 = round(self.mm * self.z2, ndigits)
            self.de1 = round(self.mte * self.z1, ndigits)
            self.de2 = round(self.mte * self.z2, ndigits)
        self.__set_output_data_dict()

    def __set_output_data_dict(self):
        if self.critical_errors == []:
            self.output_data_dict = {
                'Передаточное число: u': [self.u],
                'Средний окружной модуль: mm ': [self.mm],
                'Средний делительный диаметр: dm1, dm2 ': [self.dm1, self.dm2],
                'Внешний делительный диаметр: de1, de2 ': [self.de1, self.de2],
                'Среднее конусное расстояние: Rm ': [self.Rm],
                'Внешнее конусное расстояние: Re ': [self.Re],
                'Угол между осями валов: E ': [self.E] }
        else:
            self.output_data_dict = {}

    def get_output_data_dict(self):
        return self.output_data_dict


    def get_all_data_dict(self):
        return {**self.get_input_data_dict(), **self.get_output_data_dict()}


if __name__ == '__main__':
    a = Conical()
    print(a.get_input_data_dict())
    a.set_input_data(18, 30, 10, 10)
    a.calculate()
    print(a.get_output_data_dict())
    print(*a.get_critical_errors())
    print(*a.get_uncritical_errors())
    # print(a.get_all_data_dict())
