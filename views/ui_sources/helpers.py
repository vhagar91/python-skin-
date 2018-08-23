
from PyQt4 import QtCore
from PyQt4.Qt import Qt
from PyQt4 import QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s


class ComponentView(QtGui.QWidget):

    def __init__(self, component):
        QtGui.QWidget.__init__(self)
        self.component = component
        self.qlayout = QtGui.QVBoxLayout()
        self.qgroup_box = QtGui.QGroupBox()
        self.qgroup_box.setTitle(self.component.title)
        self.qgroup_box.setMaximumHeight(20)
        self.qtable = QtGui.QTableView()

        qmodel = QtGui.QStandardItemModel()
        qmodel.setHorizontalHeaderLabels(self.component.columns)

        for row in self.component.rows:
            qmodel.appendRow(row)

        rows_t = len(self.component.rows)
        self.qtable.setModel(qmodel)
        self.qtable.verticalHeader().setVisible(False)
        self.qtable.verticalHeader().setDefaultSectionSize(25)
        self.qtable.setSelectionMode(QtGui.QTableView.NoSelection)
        self.qtable.setMinimumHeight(rows_t*25 + 31)
        self.qtable.horizontalHeader().setResizeMode(QtGui.QHeaderView.Stretch)

        self.qlayout.addWidget(self.qgroup_box)
        self.qlayout.addWidget(self.qtable)
        self.setLayout(self.qlayout)





