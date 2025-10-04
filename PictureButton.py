from Button import Button
from Picture import Picture
from Design import Style

class PictureButton(Button):
    def __init__(self, surface, x, y, width, height,
                 img_directory=None, mouse_hover=False,
                 stroke=Style.Button.stroke, colorkey=None):
        super().__init__(surface, x, y, width, height, mouse_hover, stroke)
        self.img_directory = img_directory
        self.colorkey = colorkey
        self.set_picture()

    def set_picture(self):
        x = self.x + self.width / 2
        y = self.y + self.height / 2
        width_lim = self.width - 4 * self.stroke
        height_lim = self.height - 4 * self.stroke
        self.picture = Picture(self.surface, x, y, width_lim, height_lim, self.img_directory, center=True, colorkey=self.colorkey)

    def draw(self):
        super().draw()
        self.picture.draw()

    def update(self):
        super().update()
        self.picture.update()

    def set_xy(self, x=None, y=None, center=False):
        super().set_xy(x, y, center)
        self.set_picture()

