
from Element import Element


class MainProgram(Element):
    def draw(self):
        raise AttributeError('Необходимо переопределить метод draw в классе MainProgram ')

    def event_handler(self, event, pos=None):
        raise AttributeError('Необходимо переопределить метод event_handler в классе MainProgram ')

class Selection():
    def draw(self):
        pass

    def event_handler(self, event, pos=None):
        pass

    def update(self):
        pass

    def get_choice(self):
        pass


class Calculator():
    def draw(self):
        pass

    def event_handler(self, event, pos=None):
        pass

    def update(self):
        pass

    def set_choice(self, choice: str):
        pass

    def get_all_data(self):
        pass


class Gen():
    def draw(self):
        pass

    def event_handler(self, event, pos=None):
        pass

    def update(self):
        pass

    def set_select(self, sequence):
        pass

    def set_all_data(self, model: dict):
        pass

    def save(self):
        pass


class Saver():
    @staticmethod
    def save_txt(directory, data):
        pass

    @staticmethod
    def save_png(directory, data):
        pass

class Loader():
    @staticmethod
    def load_txt(directory):
        pass
