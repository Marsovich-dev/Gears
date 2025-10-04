from Element import Element
from SelectionSet import SelectView, SelectionSettings, Factory
from SelectSurfaceV1 import SelectSurfaceV1
from Catalog import Catalog
from Color import Color
import pygame
import numpy

class SelectViewV1(SelectView):
    def __init__(self, surface, x, y, width, height, buttons_dict, finish_btn_text='Ok'):
        self.surface = surface
        self.set_xy(x, y)
        self.set_size(width, height)
        self.my_surf = pygame.Surface(self.get_size())
        self.color = Color()
        self.color.set_style_surface()

        self.big_surf = SelectSurfaceV1(None, 0, 0, buttons_dict)
        self.catalog = Catalog(self.my_surf, 0, 0, self.width, self.height - SelectionSettings.btn_height, self.big_surf)
        self.big_surf.set_surface(self.catalog.get_my_surf())

        self.finish_btn = Factory.Input.Create_TextButton(self.my_surf, 0,
                                                          self.my_surf.get_height() - SelectionSettings.btn_height,
                                                          self.width, SelectionSettings.btn_height, finish_btn_text,
                                                          mouse_hover=0)
        self.finish_btn.color.set_normal_color(SelectionSettings.finish_btn_color_main, (255, 255, 255), (255, 255, 255))
        self.finish_btn.repaint_to_normal_color()


    def draw(self):
        self.my_surf.fill(self.color.color_main)
        self.catalog.draw()
        self.finish_btn.draw(0, 0)
        self.surface.blit(self.my_surf, (self.x, self.y))


    def event_handler(self, event, pos=None):
        pos = Element.get_event_pos(event, pos)
        if pos is not None:
            pos = tuple(numpy.array(pos) - numpy.array(self.get_xy()))
        # if type(pos) in (tuple, list):
        #     if self.get_rect().collidepoint(*pos):  # если событие за пределами my_surf, то оно нам совершенно не интересно
        self.catalog.event_handler(event, pos)
        if self.finish_btn_active:
            self.finish_btn.event_handler(event, pos)

    def update(self):
        self.catalog.update()

    def lock_finish_btn(self):
        self.finish_btn.color.repaint_to_lock_color()
        self.finish_btn_active = False

    def dislock_finish_btn(self):
        self.finish_btn.color.repaint_to_normal_color()
        self.finish_btn_active = True

    def get_dictionary(self):
        return self.big_surf.get_dictionary()
