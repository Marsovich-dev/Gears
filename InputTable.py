
import pygame, numpy
from Element import Element
from Design import Style
from InputRow import InputRow, TextCell
from CalculatorSet import CalculatorSet


class InputTable(Element):

    def set_inputrows(self, dict_data):
        self.dict_data = dict_data
        self._inputrows = []
        y = 0
        if dict_data is not None:
            for key in dict_data:
                if len(dict_data[key]) == 2:
                    if str(key) == 'Число зубьев: z1, z2 ': data_type = 'Int'
                    else: data_type = 'Float'
                    row = InputRow(None, self.width_columns, y, str(key), data_type=data_type)
                elif len(dict_data[key]) == 1:
                    row = InputRow(None, [self.width_columns[0], self.width_columns[1] + self.width_columns[2]], y, str(key))
                else:
                    raise TypeError('Ошибка в структуре полученного словаря dict_data в методе set_output_rows класса InputTable')
                for i in range(len(dict_data[key])):
                    row.get_inputboxes()[i].set_string(dict_data[key][i])
                self._inputrows.append(row)
                y += row.get_size()[1] + CalculatorSet.Table.row_spacing
        self.set_size(sum(self.width_columns), self.get_height())
        self._my_surf = pygame.Surface(self.get_size())
        self.set_rows_surface()


    def __init__(self, surface, x, y, width_columns: (list, tuple)):
        self.set_xy(x, y)
        self.surface = surface
        self.width_columns = tuple(width_columns)
        self.set_inputrows(None)

    def set_rows_surface(self):
        for i in self._inputrows:
            i.set_surface(self._my_surf)
            i.update()

    def draw(self):
        if self._inputrows:
            self._my_surf.fill(Style.background)
            for i in self._inputrows:
                i.draw()
        if self.surface:
            self.surface.blit(self._my_surf, self.get_xy())

    def event_handler(self, event, pos=None):
        pos = Element.get_event_pos(event, pos)
        if pos is not None:
            pos = numpy.array(pos) - numpy.array(self.get_xy())
        for i in self._inputrows:
            i.event_handler(event, pos)

    def get_inputrows(self):
        return tuple(self._inputrows)

    def get_height(self):
        height = 0
        for i in self._inputrows:
            height += i.get_size()[1] + CalculatorSet.Table.row_spacing
        return height
