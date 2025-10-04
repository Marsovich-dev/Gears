
import numpy
import pygame
from CalculatorSet import CalculatorSet, CalculatorFactory
from Design import Style
from Element import Element
from InputTable import InputTable
from Text import Text


class CalculatorBigSurf(Element):
    def __init__(self, surface, x, y):
        self.set_surface(surface)
        self.set_xy(x, y)
        self.__table_spacing = CalculatorSet.Table.table_spacing
        self.__objects = [None, None, None, None]
        self.set_text_between_tables('Входные данные: ', 0)
        self.set_text_between_tables('Расчётные данные: ', 2)

    def set_text_between_tables(self, string, obj_index):
        text = CalculatorFactory.Create_Text_Between_Tables(None, self.get_y_for_next_obj(obj_index), string)
        self.__objects[obj_index] = text
        self._update_size()
        self._update_objects_y()

    def set_table(self, table_dict_data, obj_index):
        table = InputTable(None, 0, self.get_y_for_next_obj(obj_index),
                           CalculatorSet.Table.width_columns)
        table.set_inputrows(table_dict_data)
        self.__objects[obj_index] = table
        self._update_size()
        self._update_objects_y()

    def _update_size(self):
        self.set_size(sum(CalculatorSet.Table.width_columns), self.get_height())
        self._my_surf = pygame.Surface(self.get_size())
        self._set_objects_surf()

    def _set_objects_surf(self):
        for i in self.__objects:
            if i is not None:
                i.set_surface(self._my_surf)
                i.update()

    def _update_objects_y(self):
        for i in self.__objects:
            if i is not None:
                i.set_xy(i.x, self.get_y_for_next_obj(self.__objects.index(i)))
                i.update()

    def get_y_for_next_obj(self, index=None):
        if index is None:
            index = len(self.__objects)
        y = self.__table_spacing
        for i in range(index):
            if self.__objects[i] is not None:
                y += self.__objects[i].get_size()[1] + self.__table_spacing
        return y

    def get_height(self):
        return self.get_y_for_next_obj()

    def event_handler(self, event, pos=None):
        pos = Element.get_event_pos(event, pos)
        if pos is not None:
            pos = numpy.array(pos) - numpy.array(self.get_xy())
        for i in self.__objects:
            if i is not None:
                i.event_handler(event, pos)

    def draw(self):
        if self.__objects:
            self._my_surf.fill(Style.background)
            for i in self.__objects:
                if i is not None:
                    if type(i) is Text:
                        i.draw(0, 0)
                    else:
                        i.draw()
        if self.surface:
            self.surface.blit(self._my_surf, self.get_xy())

    def get_objects(self):
        return [*self.__objects]
