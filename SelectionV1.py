
from AbsMainClasses import Selection
from SelectViewV1 import SelectViewV1
from base_classes import Event
from Mech import Buttons_Dict

class SelectionV1(Selection):

    # функции кнопок выбора писать сюды:
    # -----------------
    def __cyl_geo(self):
        self.__mechanism = 'CylindricalGeometry' # совпадает с названием класса в библиотеке gears
        self.change_event.invock()

    def __cyl_solid(self):
        self.__mechanism = 'CylindricalGeometry' # совпадает с названием класса в библиотеке gears
        self.change_event.invock()

    def __conical_geo(self):
        self.__mechanism = 'ConicalGeometry'    # совпадает с названием класса в библиотеке gears
        self.change_event.invock()

    def __set_btns_functions(self):
        self.__dictionary['Цилиндрическая с внешним зацеплением:'][1]['Геометричекский расчёт'].event_down += self.__cyl_geo
        self.__dictionary['Коническая с внешними зубьями:'][1]['Геометричекский расчёт'].event_down += self.__conical_geo

        # self.__dictionary['Цилиндрическая с внешним зацеплением:'][1]['Прочностной расчёт'].event_down += self.__cyl_solid

    # -----------------

    def __init__(self, surface, x, y, width, height):
        self.view = SelectViewV1(surface, x, y, width, height, Buttons_Dict, 'Выполнить расчёт ')
        self.view.lock_finish_btn()
        self.__dictionary = self.view.get_dictionary()
        self.change_event = Event()
        self.change_event += self.view.dislock_finish_btn
        self.ready_event = self.view.finish_btn.event_down
        self.__mechanism = None
        self.__set_btns_functions()

    def draw(self):
        self.view.draw()

    def update(self):
        self.view.update()

    def event_handler(self, event, pos=None):
        self.view.event_handler(event, pos)

    def get_choice(self):
        return self.__mechanism
