import sys

from PySide2.QtWidgets import *

from gui.main_window import MainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setApplicationName("RuDok")
    main_window = MainWindow(None)
    main_window.show()
    sys.exit(app.exec_())
