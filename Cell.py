
import pygame
import numpy
from Color import Color
from Element import Element
from CalculatorSet import CalculatorFactory, Factory, CalculatorSet
from Text import Text


class Cell(Element):
    def __init__(self, surface, x, y, width, height, mini_button=None):
        self.surface = surface
        self.my_surf = pygame.Surface((width, height))
        self.set_xy(x, y)
        self.set_size(width, height)
        self.object = None
        self._set_extra_object(mini_button)
        self.color = Color()
        self.color.set_style_surface()

    def _set_extra_object(self, mini_button):
        if mini_button:
            if mini_button in ('Calculate', 'Change'):
                exec(f'self.extra_object = CalculatorFactory.Create_Mini_{mini_button}_Button(self.my_surf, 0, 0)')
            else:
                raise AttributeError('Ошибка в названии для mini_button')
        else:
            self.extra_object = None

    def _set_objects_xy(self):
        x = (self.width - self.object.get_size()[0]) // 2
        y = (self.height - self.object.get_size()[1]) // 2
        self.object.set_xy(x, y)
        if self.extra_object:
            self.extra_object.set_xy(x + self.object.get_size()[0], y)
            self.extra_object.update()

    def update(self):
        if self.object:
            self.object.update()
            if self.extra_object:
                self.extra_object.update()

    def draw(self):
        self.my_surf.fill(self.color.color_main)
        if self.object:
            if type(self.object) is Text:
                self.object.draw(0, 0)
            else:
                self.object.draw()
            if self.extra_object:
                self.extra_object.draw()
        if self.surface:
            self.surface.blit(self.my_surf, self.get_xy())

    def event_handler(self, event, pos=None):
        if self.object:
            pos = self.get_event_pos(event, pos)
            if pos is not None:
                pos = list(numpy.array(pos) - numpy.array(self.get_xy()))
            if self.object:
                self.object.event_handler(event, pos)
                if self.extra_object:
                    self.extra_object.event_handler(event, pos)

    def get_object(self):
        return self.object

    def get_extra_object(self):
        return self.extra_object


class IntInputBoxCell(Cell):
    def __init__(self, surface, x, y, width, height, string=None, active=True, mini_button=None):
        super().__init__(surface, x, y, width, height, mini_button)
        self.object = CalculatorFactory.Create_Int_InputBox(self.my_surf, 0, 0, string, active)
        self._set_objects_xy()
        self.update()


class FloatInputBoxCell(Cell):
    def __init__(self, surface, x, y, width, height, string=None, active=True, mini_button=None):
        super().__init__(surface, x, y, width, height, mini_button)
        self.object = CalculatorFactory.Create_Float_InputBox(self.my_surf, 0, 0, string, active)
        self._set_objects_xy()
        self.update()


class TextCell(Cell):
    def __init__(self, surface, x, y, width, height=None, string=None, plus_width=50, bold=False):
        text = Factory.Output.Create_Text(None, x, y, width, string=string,
                                          font_h=CalculatorSet.Text.font_h, bold=bold)
        if height is not None:
            if height < text.get_size()[1] + plus_width:
                raise ValueError(f'Слишком маленькая высота в ячейке {string}')
        else:
            height = text.get_size()[1] + plus_width

        super().__init__(surface, x, y, width, height, mini_button=False)
        self.object = Factory.Output.Create_Text(self.my_surf, x, y, width, string=string,
                                                 font_h=CalculatorSet.Text.font_h, bold=bold)
        self._set_objects_xy()
        self.update()
