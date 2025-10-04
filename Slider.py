import pygame
import numpy
from Scroll import Scroll
from Color import Color
from base_classes import Event
from Design import Style
from Element import Element
from Button import Button

class Slider(Element):
    def __init__(self, surface, x, y, length, diapason: (list, tuple), vertical=True):
        self.set_surface(surface)
        self.set_diapason(diapason)
        self.current_value = self.diapason[0]

        self.move_event = Event()

        self.vertical = vertical
        self.set_xy(x, y)
        self.set_length(length)
        self.update_size()

        self.button = Button(self.strip, 0, 0, 0, 0, mouse_hover=True)
        self.button.color.set_style_slider()
        self.button.event_down += self.button_down
        self.button.event_up += self.button_up

        self.need_move = False
        self.current_coord = 0
        self.update_button()

    def set_diapason(self, diapason: (list, tuple)):
        self.diapason = [*diapason]
        self.reverse = self.get_reverse()
        self.calculate_length_diapason()

    def get_reverse(self):
        if self.diapason[0] < self.diapason[1]:
            return False
        elif self.diapason[0] == self.diapason[1]:
            raise ValueError('Диапазон не диапазон')
        else:
            return True

    def calculate_length_diapason(self):
        if (self.diapason[0] > 0) + (self.diapason[1] > 0) == 1:
            self.length_diapason = abs(self.diapason[0]) + abs(self.diapason[1])
        else:
            if abs(self.diapason[1]) > abs(self.diapason[0]):
                self.length_diapason = abs(abs(self.diapason[1]) - abs(self.diapason[0]))
            else:
                self.length_diapason = abs(abs(self.diapason[0]) - abs(self.diapason[1]))

    def update(self):
        self.update_size()
        self.update_button()

    def set_length(self, length=None):
        if length is not None:
            self.length = length

    def update_size(self):
        if self.vertical:
            self.set_size(Style.Slider.width, self.length)
        else:
            self.set_size(self.length, Style.Slider.width)
        self.strip = pygame.Surface((self.width, self.height))  # strip - полоса (англ.)
        self.k = self.length_diapason / self.length
        self.slider_length = self.length // self.k
        self.stop_coord = self.length - self.slider_length

    def update_button(self):
        self.button.set_surface(self.strip)
        self.set_current_coord(self.current_coord)
        if self.vertical:
            self.button.set_size(Style.Slider.width, self.slider_length)
        else:
            self.button.set_size(self.slider_length, Style.Slider.width)
        self.button.update()

    def update_button_pos(self):
        if self.vertical:
            self.button.set_xy(y=self.current_coord)
        else:
            self.button.set_xy(x=self.current_coord)
        self.button.update()

    def draw(self):
        self.strip.fill(Style.Slider.strip_color)
        self.button.draw()
        self.surface.blit(self.strip, (self.x, self.y))

    def event_handler(self, event, pos=None):
        event_pos = self.get_event_pos(event, pos)
        if event_pos is not None:
            event_pos = numpy.array(event_pos) - numpy.array(self.get_xy())
            self.button.event_handler(event, event_pos)
        if self.need_move:
            if event.type == pygame.MOUSEMOTION:
                self.set_current_coord(self.current_coord + event.rel[int(self.vertical)])
                if self.reverse:
                    self.set_current_value(round(self.diapason[0] - self.current_coord * self.k))
                else:
                    self.set_current_value(round(self.diapason[0] + self.current_coord * self.k))
                self.move_event.invock()
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                self.button_up()

    def set_current_value(self, current_value):
        if not self.reverse:
            if current_value < self.diapason[0]:
                self.current_value = self.diapason[0]
            elif current_value > self.diapason[1]:
                self.current_value = self.diapason[1]
            else:
                self.current_value = current_value
        else:
            if current_value > self.diapason[0]:
                self.current_value = self.diapason[0]
            elif current_value < self.diapason[1]:
                self.current_value = self.diapason[1]
            else:
                self.current_value = current_value



    def set_current_coord(self, current_coord: int):
        if current_coord < 0:
            self.current_coord = 0
        elif current_coord > self.stop_coord:
            self.current_coord = self.stop_coord
        else:
            self.current_coord = current_coord
        self.update_button_pos()


    def calculate_current_coord(self):
        if self.reverse:
            self.set_current_coord(round(self.get_current_value() / -self.k))
        else:
            self.set_current_coord(round(self.get_current_value() / self.k))


    def button_down(self):
        self.need_move = True

    def button_up(self):
        self.need_move = False

    def get_current_coord(self):
        return self.current_coord

    def get_current_value(self):
        return self.current_value

    def get_slider_length(self):
        return self.slider_length

