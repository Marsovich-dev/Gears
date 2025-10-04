from AbsMainClasses import Calculator
from CalculatorView import CalculatorViewV1
from CalculatorModel import CalculatorModelV1


class CalculatorV1(Calculator):
    def __init__(self, surface, x, y):
        self.__view = CalculatorViewV1(surface, x, y)
        self.__view.calculate_btn.event_down += self._calculate_btn_func
        self.__view.verify_btn.event_down += self._verify_btn_func
        self.__calculator_model = None

    def set_choice(self, choice: str):
        self.__calculator_model = CalculatorModelV1(choice)
        self.__view.set_model(self.__calculator_model.model)
        self.__view.set_message('Нет данных для отображения ', None)

    def __check_correct_input(self, input_data_list):
        if input_data_list in (None, [], ()):  # Если в данный момент отображается no_surf, то функция вернёт None
            self.__view.set_message('Нет данных для отображения ', None)
        elif '' in input_data_list:
            self.__view.set_message('Не все входные данные получены ', 2)
        else:
            return True

    def _calculate_btn_func(self):
        if self.__check_correct_input(self.__view.get_input_data_list()):
            self._verify_btn_func()
            self.__calculator_model.calculate()
            self.__view.update()

    def _verify_btn_func(self):
        if self.__check_correct_input(self.__view.get_input_data_list()):
            input_data = [*self.__view.get_input_data_list()]
            self.__calculator_model.set_input_data(input_data)
            self.__view.set_message(*self.__calculator_model.get_error())

    def get_save_btn(self):
        return self.__view.save_btn

    def draw(self):
        self.__view.draw()

    def event_handler(self, event, pos=None):
        self.__view.event_handler(event, pos)

    def get_all_data(self):
        return self.__calculator_model.get_all_data()

    def get_model(self):
        if self.__calculator_model is None:
            return None
        return self.__calculator_model.model
