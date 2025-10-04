
import numpy, pygame
from Element import Element
from Factory import Factory
from Design import Style
from CalculatorSet import CalculatorFactory, CalculatorSet
from Cell import IntInputBoxCell, FloatInputBoxCell, TextCell


class InputRow(Element):
    def __init__(self, surface, width_columns: (list, tuple), y, parameter: str, data_type='Float', active=True,
                 mini_button=None, plus_width=40):
        self.surface = surface
        self.width_columns = tuple([*width_columns])
        self.__data_type = data_type
        self._active = active
        self._mini_button = mini_button
        self.parameter = parameter

        self._cell_0 = TextCell(None, 0, 0, width=self.width_columns[0], string=parameter, plus_width=plus_width)

        self.set_size(sum(self.width_columns), self._cell_0.get_size()[1])
        self.my_surf = pygame.Surface(self.get_size())
        self._cell_0.set_surface(self.my_surf)

        self.set_xy(0, y)
        self._input_cells = []
        self.__set_input_cells()

    def __set_input_cells(self):
        x = self.width_columns[0]
        for i in range(1, len(self.width_columns)):
            exec(f'self._input_cells.append({self.__data_type}InputBoxCell(self.my_surf, {x}, 0, self.width_columns[{i}], self.height, active=self._active, mini_button=self._mini_button))')
            x += self.width_columns[i]

    def draw(self):
        if self.surface:
            self.my_surf.fill(Style.background)
            self._cell_0.draw()
            for i in self._input_cells:
                i.draw()
            self.surface.blit(self.my_surf, self.get_xy())

    def event_handler(self, event, pos=None):
        pos = Element.get_event_pos(event, pos)
        if pos is not None:
            pos = list(numpy.array(pos) - numpy.array(self.get_xy()))
        for i in self._input_cells:
            i.event_handler(event, pos)

    def get_inputboxes(self):
        objects = []
        for i in self._input_cells:
            objects.append(i.get_object())
        return tuple(objects)

    def get_parameter(self):
        return self.parameter

    def get_srings(self):
        strings = []
        for i in self.get_inputboxes():
            strings.append(i.get_string())
        return strings

    def get_mini_buttons(self):
        btns = []
        for i in self._input_cells:
            btns.append(i.get_extra_object())
        return btns
