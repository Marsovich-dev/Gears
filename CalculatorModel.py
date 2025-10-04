
import gears


class CalculatorModel():

    def set_input_data(self, data):
        raise AttributeError('Необходимо переопределить метод set_input_data в классе CalculatorModel')

    def get_output_data(self):
        raise AttributeError('Необходимо переопределить метод set_input_data в классе CalculatorModel')


class CalculatorModelV1(CalculatorModel):
    def __init__(self, choice: str):
        self.model = None
        exec(f'self.model = gears.{choice}()')

    def set_input_data(self, data: (list, tuple)):
        self.model.set_input_data(*data)

    def calculate(self):
        return self.model.calculate()

    def get_error(self):
        self.model.verify_input_data()
        critical_errors = self.model.get_critical_errors()
        uncritical_errors = self.model.get_uncritical_errors()
        if len(critical_errors):
            return critical_errors[0], 2
        if len(uncritical_errors):
            return uncritical_errors[0], 1
        return self.model.ErrorTexts.no_errors, 0

    def get_output_data(self):
        return self.model.get_output_data_dict()

    def get_all_data(self):
        return self.model.get_all_data_dict()
