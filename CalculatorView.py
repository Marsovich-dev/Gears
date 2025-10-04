
import numpy
import pygame
from CalculatorBigSurf import CalculatorBigSurf
from Cell import TextCell
from Design import Style
from Element import Element
from Catalog import Catalog
from CalculatorSet import CalculatorSet, CalculatorFactory
from CalculatorMessage import CalculatorMessage
from TextRow3 import TextRow3


class CalculatorView(Element):
    def draw(self):
        raise AttributeError('Необходимо переопределить метод draw в классе CalculatorView')

    def event_handler(self, event, pos=None):
        raise AttributeError('Необходимо переопределить метод event_handler в классе CalculatorView')

    def set_model(self, model):
        raise AttributeError('Необходимо переопределить метод set_model в классе CalculatorView')

    def set_message(self, message: str, degree_of_badness: int):
        raise AttributeError('Необходимо переопределить метод set_message в классе CalculatorView')


class CalculatorViewV1(CalculatorView):
    no_surf = TextCell(None, 0, 0, *CalculatorSet.Catalog.size, string='Нет данных для отображения ')
    __header_color = (25, 25, 25)
    def __init__(self, surface, x, y):
        self.set_surface(surface)
        self.set_xy(x, y)
        self.set_size(*CalculatorSet.View.size)
        self._my_surf = pygame.Surface(self.get_size())
        self.__set_buttons()
        self.__message = CalculatorMessage(self._my_surf, 0, 0, self.get_size()[0],200)
        self.set_model(None)

    def set_model(self, model):
        self.model = model
        self.update()

    def update(self):
        if self.model is None:
            texts = ['', '', '']
            big_surf = self.no_surf
        else:
            texts = ['Параметр', *self.model.parts]
            big_surf = CalculatorBigSurf(None, 0, 0)
            big_surf.set_table(self.model.get_input_data_dict(), 1)
            big_surf.set_table(self.model.get_output_data_dict(), 3)
        self.__header = TextRow3(self._my_surf, 0, 0, CalculatorSet.Table.width_columns, texts, bold=True)
        self.__header.color.set_normal_color(self.__header_color, None, None)
        self.__header.update_color()
        self.__catalog = Catalog(self._my_surf, 0, self.__header.get_size()[1], *CalculatorSet.Catalog.size, big_surf)
        y_message = self.__catalog.get_xy()[1] + self.__catalog.get_size()[1]
        self.__message.set_xy(0, y_message)
        self.__message.update()
        self.__patch = pygame.Rect(self.__header.get_size()[0], 0, self.__catalog.get_size()[0]-self.__header.get_size()[0], self.__header.get_size()[1])

    def __set_buttons(self):
        x = CalculatorSet.FuncBtn.x
        y = CalculatorSet.FuncBtn.y_first
        self.calculate_btn = CalculatorFactory.Create_Func_Btn(self._my_surf, x, y, string='Рассчитать')
        y += self.calculate_btn.get_size()[1] + CalculatorSet.FuncBtn.spacing
        self.verify_btn = CalculatorFactory.Create_Func_Btn(self._my_surf, x, y, string='Проверить')
        y += self.verify_btn.get_size()[1] + CalculatorSet.FuncBtn.spacing
        self.save_btn = CalculatorFactory.Create_Func_Btn(self._my_surf, x, y, string='Сохранить')

    def draw(self):
        self._my_surf.fill(Style.background)
        self.__header.draw()
        self.__catalog.draw()
        self.__message.draw()
        self.calculate_btn.draw()
        self.verify_btn.draw()
        self.save_btn.draw()
        pygame.draw.rect(self._my_surf, self.__header.color.color_main, self.__patch) # чтобы понять, зачем __patch, просто закомментируй эту строку и запусти программу
        self.surface.blit(self._my_surf, self.get_xy())

    def event_handler(self, event, pos=None):
        pos = Element.get_event_pos(event, pos)
        if pos is not None:
            pos = tuple(numpy.array(pos) - numpy.array(self.get_xy()))
        self.__header.event_handler(event, pos)
        self.__catalog.event_handler(event, pos)
        self.__message.event_handler(event, pos)
        self.calculate_btn.event_handler(event, pos)
        self.verify_btn.event_handler(event, pos)
        self.save_btn.event_handler(event, pos)

    def set_message(self, message: str, degree_of_badness):
        self.__message.set_message(message, degree_of_badness)
        self.__message.update()

    def get_big_surf(self):
        return self.__catalog.big_surf

    def get_input_data_list(self):
        if self.__catalog.big_surf == self.no_surf:
            return None
            # raise AttributeError('В данный момент отображается no_surf, поэтому метод get_input_data_list не может быть вызван')
        data_lict = []
        for row in self.__catalog.big_surf.get_objects()[1].get_inputrows():
            data_lict += row.get_srings()
        return data_lict
