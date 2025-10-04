from Slider import Slider
from Scroll import Scroll
from base_classes import Event
import pygame

class SliderScroll():
    def __init__(self, slider, scroll):
        self.slider = slider
        self.scroll = scroll

        self.move_event = Event()

        self.scroll.move_event += self.update_slider
        self.scroll.move_event += self.move_event.invock
        self.slider.move_event += self.update_scroll
        self.slider.move_event += self.move_event.invock

    def event_handler(self, event, pos=None):
        self.__scroll_event_handler(event, pos)
        self.__slider_event_handler(event, pos)

    def __scroll_event_handler(self, event, pos=None):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button in (4, 5):
                self.scroll.event_handler(event, pos)

    def __slider_event_handler(self, event, pos=None):
        if event.type in (pygame.MOUSEBUTTONDOWN, pygame.MOUSEBUTTONUP, pygame.MOUSEMOTION):
            self.slider.event_handler(event, pos)

    def update_slider(self):
        self.slider.set_current_value(self.scroll.get_current_value())
        self.slider.calculate_current_coord()
        self.slider.update()

    def update_scroll(self):
        self.scroll.set_current_value(self.slider.get_current_value())
        self.scroll.update()

    def slider_draw(self):
        self.slider.draw()

    def get_current_value(self):
        return self.slider.get_current_value()

