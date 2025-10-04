
import os
import gears
from SaverView import SaverViewV1

class SaverV1():
    def __init__(self, surface, x, y):
        self.__view = SaverViewV1(surface, x, y)
        self.__model = None
        self.__view.save_txt_btn.event_down += self.save_txt
        self.__view.save_and_replace_txt_btn.event_down += self.save_and_raplace_txt

    def save_txt(self):
        if self.__model is None:
            self.__view.set_message('Нет данных для сохранения', None)
        else:
            open = SaverModel.open_txt(self.__view.name_input_box.get_string(), False)
            self.__view.set_message(*open[:2])
            if len(open) == 3:
                SaverModel.save_txt(open[2], self.__model)

    def save_and_raplace_txt(self):
        if self.__model is None:
            self.__view.set_message('Нет данных для сохранения', None)
        else:
            open = SaverModel.open_txt(self.__view.name_input_box.get_string(), True)
            self.__view.set_message(*open[:2])
            if len(open) == 3:
                SaverModel.save_txt(open[2], self.__model)

    def set_model(self, model):
        self.__model = model

    def draw(self):
        self.__view.draw()

    def event_handler(self, event, pos=None):
        self.__view.event_handler(event, pos)







class SaverModel():
    replacement_message = 'Файл с таким именем уже существует. Нажмите "Сохранить/заменить при наличии" '
    no_errors = 'Сохранено в папке "Результаты вычислений". '
    empty_file_name = 'Имя файла не может быть пустым '

    @classmethod
    def open_txt(cls, file_name: str, replace: bool):
        # print(os.getcwd())
        if file_name is None or file_name == '':
            return cls.empty_file_name, 2
        file_name += '.txt'
        if not os.path.isdir('Результаты вычислений'):
            os.mkdir('Результаты вычислений')
        os.chdir('Результаты вычислений')
        if not os.path.isfile(file_name) or replace is True:
            return cls.no_errors, None, open(file_name, 'w')
        else:
            os.chdir('..')
            return cls.replacement_message, 1

    @classmethod
    def save_txt(cls, file, model: gears.Mechanism):
        input_data = model.get_input_data_dict()
        output_data = model.get_output_data_dict()
        uncritical_errors = model.get_uncritical_errors()
        print('Параметр', *model.get_parts(), file=file, sep='  ')
        print('-----', file=file)
        print('Полученные данные:', file=file)
        print(' ', file=file)
        for i in input_data:
            print(i, *input_data[i], file=file, sep='  ')
        print('-----', file=file)
        print('Расчётные данные:', file=file)
        print(' ', file=file)
        for i in output_data:
            print(i, *output_data[i], file=file, sep='  ')
        if uncritical_errors is not None or len(uncritical_errors) != 0:
            print('-----', file=file)
            print(*uncritical_errors, file=file, sep='\n')
        file.close()
        os.chdir('..')
