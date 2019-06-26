from te_controller import Controller
from te_autoplayer import AutoPlayer


class Game:
    def __init__(self):
        self.controller = Controller()
        self.autoplayer = AutoPlayer(self.controller)

    def run(self):
        self.controller.run(self.autoplayer)


Game().run()
