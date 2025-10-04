import pygame
from Element import Element
from base_classes import Event
pygame.init()

class Scroll():
    def __init__(self, zone, diapason: (list, tuple), speed=1):
        self.set_zone(zone)
        self.set_diapason(diapason)
        self.current_value = self.diapason[0]
        self.speed = speed
        self.vector = 0

        self.move_event = Event()

    def set_diapason(self, diapason: (list, tuple)):
        self.diapason = [*diapason]
        self.reverse = self.get_reverse()

    def get_reverse(self):
        if self.diapason[0] < self.diapason[1]:
            return False
        elif self.diapason[0] == self.diapason[1]:
            raise ValueError('Диапазон не диапазон')
        else:
            return True

    def update(self):
        self.set_current_value(self.current_value)

    def event_handler(self, event, pos=None):
        event_pos = Element.get_event_pos(event, pos)
        self.vector = 0
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.zone.collidepoint(*event_pos):
                if event.button == 5:    # вниз - 5, вверх - 4
                    self.vector = -1
                elif event.button == 4:
                    self.vector = 1
                self.update_current_value()

    def update_current_value(self):
        if self.vector == -1:
            self.set_current_value(self.current_value - self.speed)
        elif self.vector == 1:
            self.set_current_value(self.current_value + self.speed)
        else:
            pass
        self.move_event.invock()

    def set_current_value(self, current_value):
        if not self.reverse:
            if current_value > self.diapason[1]:
                self.current_value = self.diapason[1]
            elif current_value < self.diapason[0]:
                self.current_value = self.diapason[0]
            else:
                self.current_value = current_value
        else:
            if current_value > self.diapason[0]:
                self.current_value = self.diapason[0]
            elif current_value < self.diapason[1]:
                self.current_value = self.diapason[1]
            else:
                self.current_value = current_value

    def set_zone(self, zone):
        if type(zone) is pygame.Rect:
            self.zone = zone
        else:
            self.zone = zone.get_rect()

    def get_zone(self):
        return self.zone

    def get_current_value(self):
        return self.current_value

