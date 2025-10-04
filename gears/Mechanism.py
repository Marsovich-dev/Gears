class Mechanism:
    parts = ['Ведущий компонент', 'Ведомый компонент']
    first_modules = (0.05, 0.06, 0.08, 0.1, 0.12, 0.15, 0.20, 0.25, 0.30, 0.40, 0.5, 0.6,
                     0.8, 1, 1.25, 1.5, 2, 2.5, 3, 4, 5, 6, 8, 10, 12, 16, 20, 25, 32, 40,
                     50, 60, 80, 100)
    second_modules = (1.125, 1.375, 1.6, 1.75, 2.25, 2.75, 3.15, 3.25, 3.5, 3.75, 4.25, 4.5,
                      5.5, 6.3, 6.5, 7, 9, 11, 12.5, 14, 18, 22, 28, 36, 45, 55, 70, 90)

    class ErrorTexts:
        no_errors = 'Все контролируемые параметры зацепления в норме '

        class Critical:
            nonexistent_module = 'Несуществующий стандарт модуля '
            not_enough = 'Число зубьев колеса меньше 17. Произойдёт подрезание зубьев или колесо невозможно изготовить '

        class UnCritical:
            irreverent_module = 'Значение модуля во втором (менее предпочитительном) ряду. Возможны проблемы при изготовлении. Некритично '

    def calculate(self):
        pass

    def _verify_input_data(self):
        pass

    def get_input_data_dict(self):
        pass

    def get_output_data_dict(self):
        pass

    def get_all_data_dict(self):
        pass

    def get_parts(self):
        return self.parts

    def get_critical_errors(self):
        pass

    def get_uncritical_errors(self):
        pass
