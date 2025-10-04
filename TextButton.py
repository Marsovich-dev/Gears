import pygame
from Button import Button
from Text import Text
from Design import Style


class TextButton(Button):
    def __init__(self, surface, x, y, width, height, string=None, font_h=Style.Button.font_h,
                 mouse_hover=False, bold=False, italic=False,
                 stroke=Style.Button.stroke):
        super().__init__(surface, x, y, width, height, mouse_hover, stroke)
        if string:
            self.set_text(string, font_h, bold, italic)
        else:
            self.set_text('', font_h, bold, italic)

    def set_text(self, string, font_h=Style.Button.font_h, bold=False, italic=False):
        self.text = Text(self.surface, self.x, self.y, self.width, self.height, string=string,
                         font_h=font_h, bold=bold, italic=italic, bg_stroke=0)
        self.text.color = self.color
        self.text.update()

    def draw(self, place_x=0, place_y=0, indent_x=0, indent_y=0):
        self.draw_rect()
        if self.text:
            self.text.draw(place_x, place_y, indent_x, indent_y)
        self.draw_stroke()

    def set_xy(self, x=None, y=None, center=False):
        super().set_xy(x, y)
        self.text.set_xy(x, y)
        self.update()

    def update(self):
        super().update()
        self.text.update()

    def repaint_to_mouse_hover_color(self):
        self.color.repaint_to_mouse_hover_color()
        self.text.update()

    def repaint_to_normal_color(self):
        self.color.repaint_to_normal_color()
        self.text.update()

    def repaint_to_click_color(self):
        self.color.repaint_to_click_color()
        self.text.update()

    def repaint_to_lock_color(self):
        self.color.repaint_to_lock_color()
        self.text.update()
