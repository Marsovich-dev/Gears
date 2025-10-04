import pygame
from Element import Element
from base_classes import Event
from Color import Color
from Design import Style

class Button(Element):
    def __init__(self, surface, x, y, width, height,
                 mouse_hover=False,
                 stroke=Style.Button.stroke):
        self.set_surface(surface)
        self.set_stroke(stroke)

        self.press = False

        self.color = Color()
        self.color.set_style_button()
        self.set_mouse_hover(mouse_hover)

        self.set_size(width, height)
        self.x, self.y = x, y   # тут нельзя использовать метод set_xy, потому что в TextButton он переопределяется и там потом не хватает атрибутов.
        self.set_rect()

        self.event_down = Event()
        self.event_down_out = Event()
        self.event_up = Event()

    def draw_rect(self):
        pygame.draw.rect(self.surface, self.color.color_main, self.rect)

    def draw_stroke(self):
        if self.stroke and self.color.color_stroke:
            pygame.draw.rect(self.surface, self.color.color_stroke, self.rect, self.stroke)

    def update(self):
        self.set_rect()

    def draw(self):
        self.draw_rect()
        self.draw_stroke()

    def event_handler(self, event, pos=None):
        self._event_handler_button_down(event, pos)
        self._event_handler_button_up(event, pos)
        if self.mouse_hover:
            self._event_handler_mousemotion(event, pos)

    def _event_handler_button_down(self, event, pos):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pos is None:
                pos = event.pos
            if self.rect.collidepoint(*pos):
                if event.button == 1:
                    self.press = True
                    self.event_down.invock()
            else:
                if event.button == 1:
                    self.event_down_out.invock()

    def _event_handler_button_up(self, event, pos):
        if event.type == pygame.MOUSEBUTTONUP:
            if pos is None:
                pos = event.pos
            if self.rect.collidepoint(*pos):
                if event.button == 1:
                    self.press = False
                    self.event_up.invock()

    def _event_handler_mousemotion(self, event, pos):
        if event.type == pygame.MOUSEMOTION:
            if pos is None:
                pos = event.pos
            if self.rect.collidepoint(*pos):
                self.repaint_to_mouse_hover_color()
            else:
                self.repaint_to_normal_color()

    def set_mouse_hover(self, mouse_hover):
        self.mouse_hover = mouse_hover

    def repaint_to_mouse_hover_color(self):
        self.color.repaint_to_mouse_hover_color()

    def repaint_to_normal_color(self):
        self.color.repaint_to_normal_color()

    def repaint_to_click_color(self):
        self.color.repaint_to_click_color()

    def repaint_to_lock_color(self):
        self.color.repaint_to_lock_color()

    def set_stroke(self, stroke):
        self.stroke = stroke

    def set_bold_stroke(self):
        self.set_stroke(Style.Button.bold_stroke)

    def set_normal_stroke(self):
        self.set_stroke(Style.Button.stroke)

    def get_pressed(self):
        return self.press
