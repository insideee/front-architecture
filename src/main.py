from PySide6.QtWidgets import QApplication, QMainWindow

import sys
from ui import UiApp
from resources import resource

class App(QMainWindow):

    def __init__(self):
        super(App, self).__init__()
        self._ui = UiApp()
        self._ui.init_gui(self)

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = App()
    sys.exit(app.exec())