import pygame

def get_ev_pos(function):
    def f(self, event, pos=None):
        if pos is None:
            pos = event.pos
        result = function(self, event, pos)
        return result
    return f

class Element():
    def draw(self):
        pass

    def event_handler(self, event, pos=None):
        pass

    def update(self):
        self.set_rect()

    def set_xy(self, x=None, y=None, center=False):
        self.center = center
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    def set_size(self, width, height):
        self.width = width
        self.height = height

    def set_rect(self):
        self.rect = pygame.Rect(*self.get_xy(), *self.get_size())

    def set_surface(self, surface):
        self.surface = surface

    def get_size(self):
        return self.width, self.height

    def get_surface(self):
        return self.surface

    def get_rect(self):
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        return self.rect

    def get_xy(self):
        return self.x, self.y

    @staticmethod
    def get_event_pos(event, pos):
        if event.type in (pygame.MOUSEBUTTONDOWN, pygame.MOUSEBUTTONUP, pygame.MOUSEMOTION):
            if pos is not None:
                event_pos = pos
            else:
                event_pos = event.pos
            return event_pos
        else:
            return None



