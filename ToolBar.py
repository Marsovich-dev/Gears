
import numpy
import pygame
from Design import Style
from Element import Element
from Factory import Factory


class ToolBar(Element):
    switch_btn_size = (50, 50)
    switch_btn_img = 'Style\\switch_btn.png'

    def __init__(self, surface, x, y):
        self.surface = surface
        self.set_xy(x, y)
        self.__switch_btn = Factory.Input.Create_PictureButton(self.surface, x, y, *self.switch_btn_size,
                                                               img_directory=self.switch_btn_img)
        self.vertical_toolbar = VerticalToolBar(self.surface, self.x, self.y + self.switch_btn_size[1])
        self.horizont_toolbar = HorizontToolBar(self.surface, self.x + self.switch_btn_size[0], self.y)
        self.__current_toolbar = self.vertical_toolbar

        self.__switch_btn.event_down += self.change_toolbar
        self.__switch_btn.event_down += self.vertical_toolbar.set_all_btns_normal_stroke
        self.__switch_btn.event_down += self.horizont_toolbar.set_all_btns_normal_stroke

    def change_toolbar(self):
        if self.__current_toolbar == self.vertical_toolbar:
            self.__current_toolbar = self.horizont_toolbar
        elif self.__current_toolbar == self.horizont_toolbar:
            self.__current_toolbar = self.vertical_toolbar

    def set_selection_btn_func(self, func):
        self.vertical_toolbar.selection_btn.event_down += func
        self.horizont_toolbar.selection_btn.event_down += func

    def set_calculator_btn_func(self, func):
        self.vertical_toolbar.calculator_btn.event_down += func
        self.horizont_toolbar.calculator_btn.event_down += func

    def set_saver_btn_func(self, func):
        self.vertical_toolbar.saver_btn.event_down += func
        self.horizont_toolbar.saver_btn.event_down += func

    def draw(self):
        self.__switch_btn.draw()
        self.__current_toolbar.draw()

    def event_handler(self, event, pos=None):
        self.__switch_btn.event_handler(event, pos)
        self.__current_toolbar.event_handler(event, pos)


class ToolBarView(Element):
    color_main = (25, 25, 25)

    def _set_btns(self):
        raise AttributeError('Необходимо переопределть метод _set_btns в дочернем классе ToolBarView')

    def _set_buttons_functions(self):
        self.selection_btn.event_down += self.set_selection_btn_bold_stroke
        self.calculator_btn.event_down += self.set_calculator_btn_bold_stroke
        self.saver_btn.event_down += self.set_saver_btn_bold_stroke

    def draw(self):
        self._my_surf.fill(self.color_main)
        self.selection_btn.draw()
        self.calculator_btn.draw()
        self.saver_btn.draw()
        self.surface.blit(self._my_surf, self.get_xy())

    def event_handler(self, event, pos=None):
        pos = self.get_event_pos(event, pos)
        if pos is not None:
            pos = tuple(numpy.array(pos) - numpy.array(self.get_xy()))
        self.selection_btn.event_handler(event, pos)
        self.calculator_btn.event_handler(event, pos)
        self.saver_btn.event_handler(event, pos)

    def set_all_btns_normal_stroke(self):
        self.selection_btn.set_normal_stroke()
        self.calculator_btn.set_normal_stroke()
        self.saver_btn.set_normal_stroke()

    def set_selection_btn_bold_stroke(self):
        self.set_all_btns_normal_stroke()
        self.selection_btn.set_bold_stroke()

    def set_calculator_btn_bold_stroke(self):
        self.set_all_btns_normal_stroke()
        self.calculator_btn.set_bold_stroke()

    def set_saver_btn_bold_stroke(self):
        self.set_all_btns_normal_stroke()
        self.saver_btn.set_bold_stroke()


class VerticalToolBar(ToolBarView):
    __size = (50, 165)
    __btn_size = (50, 50)
    def __init__(self, surface, x, y):
        self.surface = surface
        self.set_xy(x, y)
        self.set_size(*self.__size)
        self._my_surf = pygame.Surface(self.get_size())
        self._set_btns()
        self._set_buttons_functions()

    def _set_btns(self):
        y = 5
        space = 5
        self.selection_btn = Factory.Input.Create_PictureButton(self._my_surf, 0, y, *self.__btn_size,
                                                                img_directory='Style//SelectionIcon.png',
                                                                colorkey=(255, 255, 255))
        y += self.__btn_size[1] + space
        self.calculator_btn = Factory.Input.Create_PictureButton(self._my_surf, 0, y, *self.__btn_size,
                                                                 img_directory='Style//CalculateIcon.png')
        y += self.__btn_size[1] + space
        self.saver_btn = Factory.Input.Create_PictureButton(self._my_surf, 0, y, *self.__btn_size,
                                                           img_directory='Style//CalculateIcon.png')
        y += self.__btn_size[1] + space



class HorizontToolBar(ToolBarView):
    __size = (765, 50)
    __btn_size = (250, 50)
    def __init__(self, surface, x, y):
        self.surface = surface
        self.set_xy(x, y)
        self.set_size(*self.__size)
        self._my_surf = pygame.Surface(self.get_size())
        self._set_btns()
        self._set_buttons_functions()

    def _set_btns(self):
        x = 5
        space = 5
        self.selection_btn = Factory.Input.Create_TextButton(self._my_surf, x, 0, *self.__btn_size,
                                                             string='Выбор')
        x += self.__btn_size[0] + space
        self.calculator_btn = Factory.Input.Create_TextButton(self._my_surf, x, 0, *self.__btn_size,
                                                              string='Расчёт')
        x += self.__btn_size[0] + space
        self.saver_btn = Factory.Input.Create_TextButton(self._my_surf, x, 0, *self.__btn_size,
                                                              string='Сохранение')
        x += self.__btn_size[0] + space
