from Element import Element
import pygame
class Picture(Element):
    def __init__(self, surface, x, y, width_lim, height_lim, img_directory, center=False, colorkey=None):
        self.set_surface(surface)
        self.img_directory = img_directory
        self.colorkey = colorkey

        self.set_size(width_lim, height_lim)
        self.set_xy(x, y, center)
        self.update()

    def draw(self):
        self.surface.blit(self.end_surf, self.blit_pos)

    def update(self):
        self.scale(self.get_size())
        self.blit_pos = self.get_blit_pos()

    def get_blit_pos(self):
        if self.center:
            blit_pos = self.end_surf.get_rect(center=(self.x, self.y))
        else:
            blit_pos = (self.x, self.y)
        return blit_pos

    def scale(self, end_size: (tuple, list)):
        self.img_surf = pygame.image.load(self.img_directory)
        if self.colorkey:
            self.img_surf.set_colorkey(self.colorkey)
        self.img_size = self.img_surf.get_size()
        if self.img_size[0] == end_size[0] and self.img_size[1] == end_size[1]:
            self.end_surf = self.img_surf
        else:
            kx = 0
            ky = 0
            if self.img_size[0] != end_size[0]:
                kx = self.img_size[0] / end_size[0]
            if self.img_size[1] != end_size[1]:
                ky = self.img_size[1] / end_size[1]

            if kx >= ky:
                k = kx
            else:
                k = ky
            self.end_surf = pygame.transform.scale(self.img_surf, (self.img_size[0] // k, self.img_size[1] // k))

    def get_real_size(self):
        return self.end_surf.get_size()
