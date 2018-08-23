
from PyQt4.Qt import Qt
from PyQt4 import QtGui, QtCore
from views.ui_sources import main
from views.ui_sources.helpers import ComponentView
from models.component import get_all
from config.loader import GCLIENT_CONFIG_PATH, load, save, is_root


class Main(QtGui.QMainWindow, main.Ui_MainWindow):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)

        scroll_hardware = QtGui.QScrollArea(self.hardwareTab)
        scroll_hardware.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        scroll_hardware.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        scroll_hardware.setMinimumWidth(self.inventoryTabView.width())
        scroll_hardware.setWidgetResizable(True)

        scroll_software = QtGui.QScrollArea(self.softwareTab)
        scroll_software.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        scroll_software.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        scroll_software.setMinimumWidth(self.inventoryTabView.width())
        scroll_software.setWidgetResizable(True)

        layout = {'hardware': QtGui.QVBoxLayout(),
                  'software': QtGui.QVBoxLayout()}
        inventory = get_all()
        for key, components in inventory.iteritems():
            for component in components:
                layout[key].addWidget(ComponentView(component))

        hardware = QtGui.QWidget()
        software = QtGui.QWidget()
        scroll_hardware.setWidget(hardware)
        scroll_software.setWidget(software)
        hardware.setLayout(layout['hardware'])
        software.setLayout(layout['software'])

        self.load_config()
        self.connect(self.enter, QtCore.SIGNAL('clicked()'), self.save_config)

    def load_config(self):
        config = load(GCLIENT_CONFIG_PATH)
        self.id_collector.setText(QtCore.QString(config['id']))
        self.server_host.setText(QtCore.QString(config['request.host']))
        self.server_port.setValue(int(config['request.port']))
        self.httpscheckBox.setChecked(config['request.https'] == 'true')
        if not is_root():
            self.id_collector.setDisabled(True)
            self.server_host.setDisabled(True)
            self.server_port.setDisabled(True)
            self.httpscheckBox.setDisabled(True)
            self.enter.setDisabled(True)

    def save_config(self):
        config = load(GCLIENT_CONFIG_PATH)
        config['id'] = str(self.id_collector.toPlainText())
        config['request.host'] = str(self.server_host.toPlainText())
        config['request.port'] = str(self.server_port.value())
        val = 'false'
        if self.httpscheckBox.isChecked():
            val = 'true'
        config['request.https'] = val
        save(config, GCLIENT_CONFIG_PATH)

    def closeEvent(self, event):
        event.ignore()
        self.hide()
