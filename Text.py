import pygame
import statistics
from Element import Element
from Color import Color
from Design import Style    # style - это объект одного из классов внутри Design
pygame.init()

class Text(Element):
    def __init__(self, surface, x, y, width, height=None,
                 string=None, font_h=None, line_spacing=0,
                 font_style=Style.font_style, bg_stroke=0,
                 bold=False, italic=False):
        self.set_surface(surface)
        self.font_style = str(font_style)
        self.bold = bold
        self.italic = italic
        self.bg_stroke = bg_stroke
        self.line_spacing = line_spacing    # line spacing - межстрочный интервал (англ.)
        self.color = Color()
        self.color.set_style_text()
        self.set_xy(x, y)
        self.set_size(width, height)
        self.font_h = font_h
        self.set_string(string)
        self.update()

    def set_string(self, string):     # после этого метода нужно обязательно вызвать update.
        if string is not None:
            self.string = str(string)
        else:
            self.string = ''

    def create_normal_multiline(self):
        for i in range(1, 50):
            self.create_multiline(i)
            if self.get_multiline_height() > self.height:
                self.font_h = i - 1
                break

    def create_multiline(self, font_h):
        self.list_lines = []  # массив поверхностей строк (surface)
        self.font = pygame.font.SysFont(self.font_style, font_h, self.bold, self.italic)
        line = word = ''
        counter = 0
        for i in self.string:
            counter += 1
            if i == ' ':
                old_line = line
                word += i
                line += word
                line_surf = self.font.render(line, 1, self.color.color_text)
                if line_surf.get_size()[0] > self.width:
                    old_line_surf = self.font.render(old_line, 1, self.color.color_text)
                    self.list_lines.append(old_line_surf)
                    line = ""
                    line += word
                word = ""
            else:
                word += i
            if counter == len(self.string):
                if i != " ":
                    line += word
                line_surf = self.font.render(line, 1, self.color.color_text)
                self.list_lines.append(line_surf)

    def draw_rects(self):
        if self.color.color_main:
            pygame.draw.rect(self.surface, self.color.color_main, self.get_rect())
        if self.color.color_stroke and self.bg_stroke:
            pygame.draw.rect(self.surface, self.color.color_stroke, self.get_rect(), self.bg_stroke)

    def draw(self, place_x=-1, place_y=-1, indent_x=0, indent_y=0):
        if self.surface:
            self.draw_rects()
            # y = self.y + (self.height / 2)
            for i in self.list_lines:
                offset_x = (self.width - i.get_width()) / 2
                offset_y = (self.height - self.get_multiline_height()) / 2

                x = self.x + offset_x + offset_x * place_x + indent_x
                y = self.y + offset_y + offset_y * place_y + indent_y + self.list_lines.index(i)*(self.get_line_height()+self.line_spacing)
                self.surface.blit(i, (x, y))

    def set_width(self, width):
        self.width = width

    def update(self):
        if self.font_h and self.height:
            self.create_multiline(self.font_h)
            if self.get_multiline_height() > self.height:
                # print(self.get_multiline_height(), self.height)
                raise ValueError(f'Слишком большой размер шрифта относительно заданной высоты в тексте: {self.string}')
        elif self.height and not self.font_h:
            self.create_normal_multiline()
        elif self.font_h and not self.height:
            self.create_multiline(self.font_h)
            self.height = self.get_multiline_height()
        else:
            raise AttributeError(f'Не задан ни height, ни font_h в тексте: {self.string}')


    def get_rect(self):
        rect = pygame.Rect(self.x, self.y, self.width, self.height)
        return rect

    def get_multiline_height(self):
        height = self.line_spacing
        for i in self.list_lines:
            height += i.get_height() + self.line_spacing
        return height

    def get_line_height(self):
        heights = []  # список высот строк
        for i in self.list_lines:
            heights.append(i.get_height())
        return statistics.mean(heights)  # за высоту строки принимаем среднее арифмеическое (mean) высот всех строк

    def get_font_h(self):
        return self.font_h
