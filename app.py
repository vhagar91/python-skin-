
import sys
from PyQt4 import QtGui
from views.main import Main
from views.ui_sources.main import _fromUtf8


class RightClickMenu(QtGui.QMenu):
    def __init__(self):
        QtGui.QMenu.__init__(self, "Exit", None)
        icon = QtGui.QIcon.fromTheme("application-exit")
        exit_action = QtGui.QAction(icon, "&Exit", self)
        exit_action.triggered.connect(QtGui.qApp.quit)
        self.addAction(exit_action)


class GskinTrayIcon(QtGui.QSystemTrayIcon):
    def __init__(self):
        super(QtGui.QSystemTrayIcon, self).__init__(None)
        self.setIcon(QtGui.QIcon(_fromUtf8(":/res/images/tray.png")))
        self.activated.connect(self.on_tray_icon_activated)
        self.setContextMenu(RightClickMenu())
        self.setToolTip('Sistema de Gestion de Hardware y Software [GRHS]')
        self.main = Main()

    def on_tray_icon_activated(self, reason):
        if reason == self.Trigger:
            self.main.show()


def main():
    app = QtGui.QApplication(sys.argv)
    tray = GskinTrayIcon()
    tray.show()
    app.exec_()

if __name__ == '__main__':
    main()
