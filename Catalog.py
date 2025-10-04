
from Color import Color
from Design import Style
from SliderScroll import Slider, Scroll, SliderScroll
from Element import Element
import pygame
import numpy


class Catalog(Element):
    """Штука, которая создаёт прокрутку для big_surf. Не придумал, как по-другому можно назвать такой класс"""

    def __init__(self, surface, x, y, width, height, big_surf: Element):
        self.surface = surface
        self.set_xy(x, y)
        self.set_size(width, height)

        self.color = Color()
        self.color.set_style_surface()

        self.my_surf = pygame.Surface((width, height))
        self.big_surf = big_surf
        self.big_surf.set_surface(self.my_surf)

        self.update_big_surf_size()

    def update_big_surf_size(self):
        if self.my_surf.get_height() >= self.big_surf.get_size()[1]:
            self.slider_scroll = None
        else:
            s = Slider(self.my_surf, self.my_surf.get_width() - Style.Slider.width, 0, self.my_surf.get_height(),
                                 (0, -self.big_surf.get_size()[1]), 1)  # создание объекта слайдера для снятия размеров и передачи их в настоящий слайдер. Работает не всегда хорошо, что было ожидаемо. Без этого объекта нужно подбирать число коррекции слайдера вручную
            slider = Slider(self.my_surf, self.my_surf.get_width() - Style.Slider.width, 0, self.my_surf.get_height(),
                                 (0, -self.big_surf.get_size()[1] - s.get_slider_length()), 1)
            scroll = Scroll(self.my_surf, (0, -self.big_surf.get_size()[1]), 50)
            self.slider_scroll = SliderScroll(slider, scroll)
            self.slider_scroll.move_event += self.update

    def draw(self):
        self.my_surf.fill(self.color.color_main)
        if self.slider_scroll:
            self.slider_scroll.slider_draw()
        self.big_surf.draw()
        self.surface.blit(self.my_surf, (self.x, self.y))

    def event_handler(self, event, pos=None):
        ev_pos = self.get_event_pos(event, pos)
        if ev_pos is not None:
            if self.get_rect().collidepoint(*ev_pos):
                if self.slider_scroll is not None:
                    self.slider_scroll.event_handler(event, tuple(numpy.array(ev_pos) - numpy.array(self.get_xy())))
                self.big_surf.event_handler(event, tuple(numpy.array(ev_pos) - numpy.array(self.get_xy())))
            else:
                if self.slider_scroll is not None:
                    self.slider_scroll.slider.event_handler(event, tuple(numpy.array(ev_pos) - numpy.array(self.get_xy())))
        else:
            self.big_surf.event_handler(event, None)

    def update(self):
        if self.slider_scroll:
            self.big_surf.set_xy(y=self.slider_scroll.get_current_value())

    def get_my_surf(self):
        return self.my_surf
