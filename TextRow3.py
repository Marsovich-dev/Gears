
import pygame
from Cell import TextCell
from Color import Color
from Element import Element
from Design import Style


class TextRow3(Element):
    def __init__(self, surface, x, y, width_columns: (list, tuple), texts: (list, tuple), bold=False):
        self.surface = surface
        self._width_columns = tuple(width_columns)
        self._texts = tuple(texts)
        self.set_xy(x, y)
        height = self.get_height()
        self.set_size(sum(self._width_columns), height)
        self._my_surf = pygame.Surface(self.get_size())
        x = 0
        self._cells = []
        for i in range(3):
            self._cells.append(TextCell(self._my_surf, x, 0, self._width_columns[i], height, string=self._texts[i], bold=bold))
            x += self._cells[i].get_size()[0]
        self.color = Color()
        self.color.set_style_surface()

    def update_color(self):
        for i in self._cells:
            i.color = self.color

    def draw(self):
        self._my_surf.fill(Style.background)
        for i in self._cells:
            i.draw()
        self.surface.blit(self._my_surf, self.get_xy())

    def get_height(self):
        heightss = []
        for i in range(3):
            cell = TextCell(None, 0, 0, self._width_columns[i], string=self._texts[i])
            heightss.append(cell.get_size()[1])
        return max(heightss)
