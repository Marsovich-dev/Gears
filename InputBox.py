from Element import Element
from TextButton import TextButton
from TextHandler import TextHandler
from Design import Style
from base_classes import Event

import pygame
class InputBox(Element):
    def __init__(self, surface, x, y, width, height, font_h):
        self.set_surface(surface)
        self.font_h = font_h
        self.x, self.y = x, y

        self.__btn = TextButton(surface, x, y, width, height, font_h=font_h)
        self.__btn.color.set_style_input_field()

        self.__btn.event_down += self.highlight
        self.__btn.event_down += self.need_input_true
        self.__btn.event_down_out += self.not_highlight
        self.__btn.event_down_out += self.need_input_false

        self.active_true()
        self.need_input_false()
        self.set_valid_characters()
        self.string = ''

    def set_valid_characters(self, valid_characters=None):
        if valid_characters:
            self.__valid_characters = valid_characters
        else:
            self.__valid_characters = ()

    def highlight(self):
        self.__btn.stroke = Style.Input_Field.bold_stroke

    def not_highlight(self):
        self.__btn.stroke = Style.Input_Field.stroke

    def need_input_false(self):
        self.need_input = False

    def need_input_true(self):
        self.need_input = True

    def active_true(self):
        self.active = True
        self.__btn.repaint_to_normal_color()

    def active_false(self):
        self.active = False
        self.__btn.repaint_to_lock_color()

    def event_handler(self, event, pos=None):
        if self.active:
            self.__btn.event_handler(event, pos)
            if self.need_input:

                self.__keyboard_handler(event)

    def draw(self, place_x=0, place_y=0, indent_x=0, indent_y=0):
        self.__btn.draw(place_x, place_y, indent_x, indent_y)

    def __keyboard_handler(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                self.__enter_handler(event)
            elif event.key == pygame.K_BACKSPACE:
                self.__backspace_handler(event)
            else:
                self.__keys_handler(event)

    def __enter_handler(self, event):
        if event.key == pygame.K_RETURN:
            self.need_input_false()
            self.not_highlight()

    def __backspace_handler(self, event):
        if event.key == pygame.K_BACKSPACE:
            if event.mod == 4224 or event.mod == 4160:  # 4224 - правая кнопка ctrl, 4160 - левая. Чисто опытным путём установил, какое значение выдаёт команда event.mod при нажатии этих клавиш
                while True:  # что тут происходит, лучше не знать, ибо какого-то хрена условие, записанное сразу после слова while тупо не работает (
                    self.string = self.string[:-1]
                    if len(self.string) == 0:
                        break
                    elif self.string[-1] == ' ':
                        break
            else:
                self.string = self.string[:-1]
            self.update_string()

    def __keys_handler(self, event):
        character = str(event.unicode)
        if self.__valid_characters:
            if character in self.__valid_characters:
                self.string += character
        else:
            self.string += character
        self.update_string()

    def update_string(self):
        self.__btn.set_text(self.string, self.font_h)

    def set_string(self, string):
        if string is None:
            self.string = ''
        else:
            self.string = str(string)
        self.update_string()

    def get_string(self):
        return str(self.string.replace(',', '.'))

    def get_size(self):
        return self.__btn.get_size()

    def set_xy(self, x: (int, float) = None, y: (int, float) = None, center=False):
        self.__btn.set_xy(x, y, center)
        self.__btn.update()
