
from SelectionSet import SelectionFactory, SelectionSettings
from Color import Color
from Element import Element
import numpy
import pygame

class SelectSurfaceV1(Element):
    def __init__(self, surface, x, y, dictionary):
        self.surface = surface
        self.set_xy(x, y)
        self.surf_stroke = 0

        self.color = Color()
        self.color.set_style_surface()

        self.set_size(800, SelectionSettings.get_full_height(dictionary))
        self.my_surf = pygame.Surface((self.width, self.height))
        self.__set_objects(dictionary)

    def set_surface(self, surface): #  метод нужен, когда при создании объекта ещё нет surface.
        self.surface = surface

    def __set_objects(self, dictionary):
        self.dictionary = dictionary
        x = (self.my_surf.get_width() - SelectionSettings.btn_width) // 2
        btn_height = SelectionSettings.btn_height
        txt_height = SelectionSettings.txt_height
        space = SelectionSettings.space
        y = SelectionSettings.y
        for name_mech in self.dictionary:
            self.dictionary[name_mech][0] = SelectionFactory.Create_Select_Text(self.my_surf, x, y, name_mech)
            y += txt_height + space
            for name_calcul in self.dictionary[name_mech][1]:
                self.dictionary[name_mech][1][name_calcul] = SelectionFactory.Create_Select_Button(self.my_surf, x, y, name_calcul)
                y += btn_height + space

    def draw(self):
        self.my_surf.fill(self.color.color_main)
        if self.surf_stroke:
            pygame.draw.rect(self.my_surf, self.color.color_stroke, pygame.Rect(0, 0, *self.my_surf.get_size()),
                             self.surf_stroke)
        for name_mech in self.dictionary:
            self.dictionary[name_mech][0].draw(-1, 0)
            for name_calcul in self.dictionary[name_mech][1]:
                self.dictionary[name_mech][1][name_calcul].draw()
        self.surface.blit(self.my_surf, (self.x, self.y))


    def event_handler(self, event, pos=None):
        ev_pos = self.get_event_pos(event, pos)
        if ev_pos is not None:
            ev_pos = numpy.array(ev_pos) - numpy.array((self.x, self.y))
        for name_mech in self.dictionary:
            self.dictionary[name_mech][0].event_handler(event, ev_pos)
            for name_calcul in self.dictionary[name_mech][1]:
                self.dictionary[name_mech][1][name_calcul].event_handler(event, ev_pos)

    def get_dictionary(self):
        return self.dictionary
