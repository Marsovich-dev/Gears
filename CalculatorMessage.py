
from Element import Element
from Factory import Factory
from Color import Color
import pygame


class CalculatorMessage(Element):
    # степень "плохости" (degree_of_badness) измеряется от 0 (всё норм)
    # до 2 (всё плохо). Если он равен None, то это нейтральный
    __font_h = 20
    __offset = (20, 20)

    class Colors:
        neutral = (255, 255, 255)
        no_errors = (0, 255, 0)
        not_critical = (255, 255, 0)
        critical = (255, 0, 0)

    def __init__(self, surface, x, y, width, height):
        self.set_surface(surface)
        self.set_xy(x, y)
        self.set_size(width, height)
        self._my_surf = pygame.Surface(self.get_size())
        self.color = Color()
        self.color.set_normal_color((25, 25, 25), None, None)
        self.__message = Factory.Output.Create_Text(self._my_surf, *self.__offset, self.width, font_h=self.__font_h)
        self.set_message(None, None)

    def set_message(self, message, degree_of_badness):
        self.__message.height = None
        self.__message.set_string(message)
        self.__degree_of_badness = degree_of_badness
        self._set_color()
        self.__message.update()

    def draw(self):
        self._my_surf.fill(self.color.color_main)
        self.__message.draw()
        self.surface.blit(self._my_surf, self.get_xy())

    def update(self):
        self._set_color()
        self.__message.update()

    def _set_color(self):
        if self.__degree_of_badness is None:
            self.__message.color.set_normal_color(None, None, self.Colors.neutral)
        elif self.__degree_of_badness == 0:
            self.__message.color.set_normal_color(None, None, self.Colors.no_errors)
        elif self.__degree_of_badness == 1:
            self.__message.color.set_normal_color(None, None, self.Colors.not_critical)
        elif self.__degree_of_badness == 2:
            self.__message.color.set_normal_color(None, None, self.Colors.critical)
