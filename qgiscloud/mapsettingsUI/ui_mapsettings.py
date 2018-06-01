# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mapsettings.ui'
#
# Created by: PyQt5 UI code generator 5.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_map_settings(object):
    def setupUi(self, map_settings):
        map_settings.setObjectName("map_settings")
        map_settings.resize(695, 730)
        self.gridLayout = QtWidgets.QGridLayout(map_settings)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox_2 = QtWidgets.QGroupBox(map_settings)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.search_db_combobox = QtWidgets.QComboBox(self.groupBox_2)
        self.search_db_combobox.setObjectName("search_db_combobox")
        self.gridLayout_4.addWidget(self.search_db_combobox, 2, 1, 1, 1)
        self.search_type_list = QtWidgets.QListWidget(self.groupBox_2)
        self.search_type_list.setObjectName("search_type_list")
        self.gridLayout_4.addWidget(self.search_type_list, 0, 1, 1, 1)
        self.search_type_lbl = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.search_type_lbl.setFont(font)
        self.search_type_lbl.setObjectName("search_type_lbl")
        self.gridLayout_4.addWidget(self.search_type_lbl, 0, 0, 1, 1)
        self.search_sql_textedit = QgsCodeEditorSQL(self.groupBox_2)
        self.search_sql_textedit.setObjectName("search_sql_textedit")
        self.gridLayout_4.addWidget(self.search_sql_textedit, 3, 1, 1, 1)
        self.search_sql_lbl = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.search_sql_lbl.setFont(font)
        self.search_sql_lbl.setObjectName("search_sql_lbl")
        self.gridLayout_4.addWidget(self.search_sql_lbl, 3, 0, 1, 1)
        self.search_db_lbl = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.search_db_lbl.setFont(font)
        self.search_db_lbl.setObjectName("search_db_lbl")
        self.gridLayout_4.addWidget(self.search_db_lbl, 2, 0, 1, 1)
        self.sql_preview_btn = QtWidgets.QPushButton(self.groupBox_2)
        self.sql_preview_btn.setObjectName("sql_preview_btn")
        self.gridLayout_4.addWidget(self.sql_preview_btn, 3, 2, 1, 1)
        self.gridLayout.addWidget(self.groupBox_2, 5, 0, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(map_settings)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.delete_user_btn = QtWidgets.QPushButton(self.groupBox)
        self.delete_user_btn.setObjectName("delete_user_btn")
        self.gridLayout_3.addWidget(self.delete_user_btn, 1, 2, 1, 1)
        self.users_lineedit = QtWidgets.QLineEdit(self.groupBox)
        self.users_lineedit.setToolTipDuration(4)
        self.users_lineedit.setObjectName("users_lineedit")
        self.gridLayout_3.addWidget(self.users_lineedit, 0, 1, 1, 1)
        self.users_lbl = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.users_lbl.setFont(font)
        self.users_lbl.setObjectName("users_lbl")
        self.gridLayout_3.addWidget(self.users_lbl, 0, 0, 1, 1)
        self.add_users_btn = QtWidgets.QPushButton(self.groupBox)
        self.add_users_btn.setObjectName("add_users_btn")
        self.gridLayout_3.addWidget(self.add_users_btn, 0, 2, 1, 1)
        self.show_userlist_btn = QtWidgets.QPushButton(self.groupBox)
        self.show_userlist_btn.setObjectName("show_userlist_btn")
        self.gridLayout_3.addWidget(self.show_userlist_btn, 2, 2, 1, 1)
        self.gridLayout.addWidget(self.groupBox, 6, 0, 1, 1)
        self.settings_box = QtWidgets.QGroupBox(map_settings)
        self.settings_box.setObjectName("settings_box")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.settings_box)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.viewer_lbl = QtWidgets.QLabel(self.settings_box)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.viewer_lbl.setFont(font)
        self.viewer_lbl.setObjectName("viewer_lbl")
        self.gridLayout_2.addWidget(self.viewer_lbl, 10, 0, 1, 1)
        self.language_lbl = QtWidgets.QLabel(self.settings_box)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.language_lbl.setFont(font)
        self.language_lbl.setObjectName("language_lbl")
        self.gridLayout_2.addWidget(self.language_lbl, 3, 0, 1, 1)
        self.viewer_active_lbl = QtWidgets.QLabel(self.settings_box)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.viewer_active_lbl.setFont(font)
        self.viewer_active_lbl.setObjectName("viewer_active_lbl")
        self.gridLayout_2.addWidget(self.viewer_active_lbl, 0, 0, 1, 1)
        self.language_combobox = QtWidgets.QComboBox(self.settings_box)
        self.language_combobox.setObjectName("language_combobox")
        self.gridLayout_2.addWidget(self.language_combobox, 3, 1, 1, 1)
        self.viewer_combobox = QtWidgets.QComboBox(self.settings_box)
        self.viewer_combobox.setObjectName("viewer_combobox")
        self.gridLayout_2.addWidget(self.viewer_combobox, 10, 1, 1, 1)
        self.scales_lineedit = QtWidgets.QLineEdit(self.settings_box)
        self.scales_lineedit.setObjectName("scales_lineedit")
        self.gridLayout_2.addWidget(self.scales_lineedit, 8, 1, 1, 1)
        self.wms_public_lbl = QtWidgets.QLabel(self.settings_box)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.wms_public_lbl.setFont(font)
        self.wms_public_lbl.setObjectName("wms_public_lbl")
        self.gridLayout_2.addWidget(self.wms_public_lbl, 1, 0, 1, 1)
        self.map_public_lbl = QtWidgets.QLabel(self.settings_box)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.map_public_lbl.setFont(font)
        self.map_public_lbl.setObjectName("map_public_lbl")
        self.gridLayout_2.addWidget(self.map_public_lbl, 2, 0, 1, 1)
        self.generate_scales_btn = QtWidgets.QPushButton(self.settings_box)
        self.generate_scales_btn.setAcceptDrops(False)
        self.generate_scales_btn.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.generate_scales_btn.setAutoFillBackground(False)
        self.generate_scales_btn.setObjectName("generate_scales_btn")
        self.gridLayout_2.addWidget(self.generate_scales_btn, 8, 2, 1, 1)
        self.map_public_chkb = QtWidgets.QCheckBox(self.settings_box)
        self.map_public_chkb.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.map_public_chkb.setChecked(False)
        self.map_public_chkb.setAutoExclusive(False)
        self.map_public_chkb.setObjectName("map_public_chkb")
        self.gridLayout_2.addWidget(self.map_public_chkb, 2, 1, 1, 1)
        self.scales_lbl = QtWidgets.QLabel(self.settings_box)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.scales_lbl.setFont(font)
        self.scales_lbl.setObjectName("scales_lbl")
        self.gridLayout_2.addWidget(self.scales_lbl, 8, 0, 1, 1)
        self.viewer_active_chkb = QtWidgets.QCheckBox(self.settings_box)
        self.viewer_active_chkb.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.viewer_active_chkb.setChecked(False)
        self.viewer_active_chkb.setAutoExclusive(False)
        self.viewer_active_chkb.setObjectName("viewer_active_chkb")
        self.gridLayout_2.addWidget(self.viewer_active_chkb, 0, 1, 1, 1)
        self.wms_public_chkb = QtWidgets.QCheckBox(self.settings_box)
        self.wms_public_chkb.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.wms_public_chkb.setChecked(False)
        self.wms_public_chkb.setAutoExclusive(False)
        self.wms_public_chkb.setObjectName("wms_public_chkb")
        self.gridLayout_2.addWidget(self.wms_public_chkb, 1, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.settings_box)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 9, 1, 1, 1)
        self.gridLayout.addWidget(self.settings_box, 4, 0, 1, 1)
        self.save_settings_btn = QtWidgets.QDialogButtonBox(map_settings)
        self.save_settings_btn.setOrientation(QtCore.Qt.Horizontal)
        self.save_settings_btn.setStandardButtons(QtWidgets.QDialogButtonBox.Apply|QtWidgets.QDialogButtonBox.Close)
        self.save_settings_btn.setObjectName("save_settings_btn")
        self.gridLayout.addWidget(self.save_settings_btn, 7, 0, 1, 1)

        self.retranslateUi(map_settings)
        self.save_settings_btn.accepted.connect(map_settings.accept)
        self.save_settings_btn.rejected.connect(map_settings.reject)
        QtCore.QMetaObject.connectSlotsByName(map_settings)

    def retranslateUi(self, map_settings):
        _translate = QtCore.QCoreApplication.translate
        map_settings.setWindowTitle(_translate("map_settings", "Map Settings"))
        self.groupBox_2.setTitle(_translate("map_settings", "search settings"))
        self.search_type_lbl.setText(_translate("map_settings", "Search type"))
        self.search_sql_lbl.setText(_translate("map_settings", "Search SQL"))
        self.search_db_lbl.setText(_translate("map_settings", "Search DB"))
        self.sql_preview_btn.setText(_translate("map_settings", "preview"))
        self.groupBox.setTitle(_translate("map_settings", "user management"))
        self.delete_user_btn.setText(_translate("map_settings", "delete user"))
        self.users_lineedit.setToolTip(_translate("map_settings", "You can add only one user at a time"))
        self.users_lbl.setText(_translate("map_settings", "Users"))
        self.add_users_btn.setText(_translate("map_settings", "add user"))
        self.show_userlist_btn.setText(_translate("map_settings", "show user list"))
        self.settings_box.setTitle(_translate("map_settings", "general settings"))
        self.viewer_lbl.setText(_translate("map_settings", "Viewer"))
        self.language_lbl.setText(_translate("map_settings", "Language"))
        self.viewer_active_lbl.setText(_translate("map_settings", "Viewer active"))
        self.wms_public_lbl.setText(_translate("map_settings", "WMS public"))
        self.map_public_lbl.setText(_translate("map_settings", "Map public"))
        self.generate_scales_btn.setText(_translate("map_settings", "generate scales"))
        self.scales_lbl.setText(_translate("map_settings", "Scales"))
        self.label.setText(_translate("map_settings", "*only whole numbers are allowed"))

from qgis.gui import QgsCodeEditorSQL
