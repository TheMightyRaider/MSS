# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_mscolab_version_history.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MscolabVersionHistory(object):
    def setupUi(self, MscolabVersionHistory):
        MscolabVersionHistory.setObjectName("MscolabVersionHistory")
        MscolabVersionHistory.resize(1090, 797)
        self.centralwidget = QtWidgets.QWidget(MscolabVersionHistory)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.usernameLabel = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.usernameLabel.sizePolicy().hasHeightForWidth())
        self.usernameLabel.setSizePolicy(sizePolicy)
        self.usernameLabel.setObjectName("usernameLabel")
        self.horizontalLayout_3.addWidget(self.usernameLabel)
        self.operationNameLabel = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.operationNameLabel.sizePolicy().hasHeightForWidth())
        self.operationNameLabel.setSizePolicy(sizePolicy)
        self.operationNameLabel.setObjectName("operationNameLabel")
        self.horizontalLayout_3.addWidget(self.operationNameLabel)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 1)
        self.horizontalLayout_3.setStretch(2, 2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_3.addWidget(self.line)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.versionFilterCB = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.versionFilterCB.sizePolicy().hasHeightForWidth())
        self.versionFilterCB.setSizePolicy(sizePolicy)
        self.versionFilterCB.setObjectName("versionFilterCB")
        self.versionFilterCB.addItem("")
        self.versionFilterCB.addItem("")
        self.horizontalLayout.addWidget(self.versionFilterCB)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.changes = QtWidgets.QListWidget(self.centralwidget)
        self.changes.setTextElideMode(QtCore.Qt.ElideNone)
        self.changes.setWordWrap(True)
        self.changes.setObjectName("changes")
        self.verticalLayout_2.addWidget(self.changes)
        self.horizontalLayout_4.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.currentWaypointsTable = QtWidgets.QTableView(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.currentWaypointsTable.sizePolicy().hasHeightForWidth())
        self.currentWaypointsTable.setSizePolicy(sizePolicy)
        self.currentWaypointsTable.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.currentWaypointsTable.setObjectName("currentWaypointsTable")
        self.verticalLayout.addWidget(self.currentWaypointsTable)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.changePreviewTable = QtWidgets.QTableView(self.centralwidget)
        self.changePreviewTable.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.changePreviewTable.setObjectName("changePreviewTable")
        self.verticalLayout.addWidget(self.changePreviewTable)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.deleteVersionNameBtn = QtWidgets.QPushButton(self.centralwidget)
        self.deleteVersionNameBtn.setObjectName("deleteVersionNameBtn")
        self.horizontalLayout_2.addWidget(self.deleteVersionNameBtn)
        self.nameVersionBtn = QtWidgets.QPushButton(self.centralwidget)
        self.nameVersionBtn.setObjectName("nameVersionBtn")
        self.horizontalLayout_2.addWidget(self.nameVersionBtn)
        self.checkoutBtn = QtWidgets.QPushButton(self.centralwidget)
        self.checkoutBtn.setAutoDefault(False)
        self.checkoutBtn.setDefault(False)
        self.checkoutBtn.setObjectName("checkoutBtn")
        self.horizontalLayout_2.addWidget(self.checkoutBtn)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.verticalLayout.setStretch(2, 1)
        self.verticalLayout.setStretch(4, 1)
        self.horizontalLayout_4.addLayout(self.verticalLayout)
        self.horizontalLayout_4.setStretch(0, 1)
        self.horizontalLayout_4.setStretch(1, 4)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.gridLayout.addLayout(self.verticalLayout_3, 0, 0, 1, 1)
        MscolabVersionHistory.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MscolabVersionHistory)
        self.statusbar.setObjectName("statusbar")
        MscolabVersionHistory.setStatusBar(self.statusbar)
        self.actionCloseWindow = QtWidgets.QAction(MscolabVersionHistory)
        self.actionCloseWindow.setObjectName("actionCloseWindow")
        MscolabVersionHistory.addAction(self.actionCloseWindow)

        self.retranslateUi(MscolabVersionHistory)
        self.actionCloseWindow.triggered.connect(MscolabVersionHistory.close) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MscolabVersionHistory)

    def retranslateUi(self, MscolabVersionHistory):
        _translate = QtCore.QCoreApplication.translate
        MscolabVersionHistory.setWindowTitle(_translate("MscolabVersionHistory", "Version History"))
        self.usernameLabel.setText(_translate("MscolabVersionHistory", "Logged In: "))
        self.operationNameLabel.setText(_translate("MscolabVersionHistory", "Operation:"))
        self.label.setText(_translate("MscolabVersionHistory", "Viewing:"))
        self.versionFilterCB.setItemText(0, _translate("MscolabVersionHistory", "All Changes"))
        self.versionFilterCB.setItemText(1, _translate("MscolabVersionHistory", "Named Versions"))
        self.label_3.setText(_translate("MscolabVersionHistory", "Current Waypoints:"))
        self.label_2.setText(_translate("MscolabVersionHistory", "Version Preview:"))
        self.deleteVersionNameBtn.setToolTip(_translate("MscolabVersionHistory", "Delete the name of the selected version"))
        self.deleteVersionNameBtn.setText(_translate("MscolabVersionHistory", "Delete Version Name"))
        self.nameVersionBtn.setToolTip(_translate("MscolabVersionHistory", "Give name to the selected version"))
        self.nameVersionBtn.setText(_translate("MscolabVersionHistory", "Name Version"))
        self.checkoutBtn.setToolTip(_translate("MscolabVersionHistory", "Checkout to the selected version"))
        self.checkoutBtn.setText(_translate("MscolabVersionHistory", "Checkout"))
        self.actionCloseWindow.setText(_translate("MscolabVersionHistory", "actionCloseWindow"))
        self.actionCloseWindow.setShortcut(_translate("MscolabVersionHistory", "Ctrl+W"))
