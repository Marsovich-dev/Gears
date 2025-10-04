
import math
from gears.Mechanism import Mechanism


class CylindricalGeometry(Mechanism):
    parts = ('Ведущее колесо ', 'Ведомое колесо ')
    class ErrorTexts:
        no_errors = 'Все контролируемые параметры зацепления в норме '
        class Critical:
            nonexistent_module = 'Несуществующий стандарт модуля '
            not_enough = 'Число зубьев колеса меньше 17. Произойдёт подрезание зубьев или колесо невозможно изготовить '
        class UnCritical:
            irreverent_module = 'Значение модуля во втором (менее предпочитительном) ряду. Возможны проблемы при изготовлении. Некритично '

    def __init__(self):
        self.critical_errors = []
        self.uncritical_errors = []
        self.z1 = None
        self.z2 = None
        self.m = None
        self.b1 = None
        self.b2 = None
        self.__set_input_data_dict()
        self.u = None
        self.a = None
        self.h = None
        self.ha = None
        self.hf = None
        self.d1 = None
        self.d2 = None
        self.da1 = None
        self.da2 = None
        self.df1 = None
        self.df2 = None
        self.p = None
        self.S = None
        self.e = None
        self.__set_output_data_dict()

    def set_input_data(self, z1, z2, m, b1, b2):
        self.z1 = int(z1)
        self.z2 = int(z2)
        self.m = float(m)
        self.b1 = float(b1)
        self.b2 = float(b2)
        self.__set_input_data_dict()

    def __set_input_data_dict(self):
        self.input_data_dict = {
            'Число зубьев: z1, z2 ': [self.z1, self.z2],
            'Модуль: m ': [self.m],
            'Ширина зубчатого венца: b1, b2 ': [self.b1, self.b2]
        }

    def get_input_data_dict(self):
        return self.input_data_dict

    def verify_input_data(self):
        self.critical_errors = []
        self.uncritical_errors = []
        if not (self.m in (*self.first_modules, *self.second_modules)):
            self.critical_errors.append(self.ErrorTexts.Critical.nonexistent_module)
        elif self.m in self.second_modules:
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
            self.a = round((self.m * (self.z1 + self.z2)) / 2, ndigits)

            self.h = round(2.25 * self.m, ndigits)
            self.ha = round(self.m, ndigits)
            self.hf = round(1.25 * self.m, ndigits)

            self.d1 = round(self.m * self.z1, ndigits)
            self.d2 = round(self.m * self.z2, ndigits)

            self.da1 = round(self.m * (self.z1 + 2), ndigits)
            self.da2 = round(self.m * (self.z2 + 2), ndigits)

            self.df1 = round(self.m * (self.z1 - 2.5), ndigits)
            self.df2 = round(self.m * (self.z2 - 2.5), ndigits)

            self.p = round(self.m * math.pi, ndigits)
            self.S = round(0.5 * self.m, ndigits)
            self.e = round(0.5 * self.m, ndigits)
        self.__set_output_data_dict()

    def __set_output_data_dict(self):
        if self.critical_errors == []:
            self.output_data_dict = {
                'Передаточное число ': [self.u],
                'Межосевое расстояние ': [self.a],
                'Высота зуба ': [self.h],
                'Высота головки зуба ': [self.ha],
                'Высота ножки зуба ': [self.hf],
                'Делительный диаметр ': [self.d1, self.d2],
                'Диаметр вершин зубьев ': [self.da1, self.da2],
                'Диаметр впадин зубьев ': [self.df1, self.df2],
                'Шаг зубьев ': [self.p],
                'Толщина зуба ': [self.S],
                'Ширина впадин ': [self.e],
            }
        else:
            self.output_data_dict = {}

    def get_output_data_dict(self):
        return self.output_data_dict

    def get_all_data_dict(self):
        return {**self.get_input_data_dict(), **self.get_output_data_dict()}


if __name__ == '__main__':
    a = Cylindrical()
    print(a.get_input_data_dict())
    a.set_input_data(27, 30, 4, 10, 15)
    a.calculate()
    print(a.get_output_data_dict())
    print(*a.get_critical_errors())
    print(*a.get_uncritical_errors())
    # print(a.get_all_data_dict())
