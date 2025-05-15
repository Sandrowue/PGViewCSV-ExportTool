# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PGViewExportTool.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QFrame,
    QHeaderView, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QTableWidget, QTableWidgetItem, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(962, 998)
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(80, 80, 791, 371))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame.setLineWidth(3)
        self.palvelinLabel = QLabel(self.frame)
        self.palvelinLabel.setObjectName(u"palvelinLabel")
        self.palvelinLabel.setGeometry(QRect(30, 20, 130, 20))
        font = QFont()
        font.setPointSize(14)
        self.palvelinLabel.setFont(font)
        self.porttiLabel = QLabel(self.frame)
        self.porttiLabel.setObjectName(u"porttiLabel")
        self.porttiLabel.setGeometry(QRect(30, 80, 130, 20))
        self.porttiLabel.setFont(font)
        self.tietokantaLabel = QLabel(self.frame)
        self.tietokantaLabel.setObjectName(u"tietokantaLabel")
        self.tietokantaLabel.setGeometry(QRect(30, 140, 130, 20))
        self.tietokantaLabel.setFont(font)
        self.kayttajatunnusLabel = QLabel(self.frame)
        self.kayttajatunnusLabel.setObjectName(u"kayttajatunnusLabel")
        self.kayttajatunnusLabel.setGeometry(QRect(30, 200, 130, 20))
        self.kayttajatunnusLabel.setFont(font)
        self.salasanaLabel = QLabel(self.frame)
        self.salasanaLabel.setObjectName(u"salasanaLabel")
        self.salasanaLabel.setGeometry(QRect(30, 260, 130, 20))
        self.salasanaLabel.setFont(font)
        self.yhteysPushButton = QPushButton(self.frame)
        self.yhteysPushButton.setObjectName(u"yhteysPushButton")
        self.yhteysPushButton.setGeometry(QRect(30, 320, 140, 30))
        self.yhteysPushButton.setFont(font)
        self.palvelinLineEdit = QLineEdit(self.frame)
        self.palvelinLineEdit.setObjectName(u"palvelinLineEdit")
        self.palvelinLineEdit.setGeometry(QRect(170, 20, 450, 24))
        self.palvelinLineEdit.setFont(font)
        self.porttiLineEdit = QLineEdit(self.frame)
        self.porttiLineEdit.setObjectName(u"porttiLineEdit")
        self.porttiLineEdit.setGeometry(QRect(170, 80, 450, 24))
        self.porttiLineEdit.setFont(font)
        self.tietokantaLineEdit = QLineEdit(self.frame)
        self.tietokantaLineEdit.setObjectName(u"tietokantaLineEdit")
        self.tietokantaLineEdit.setGeometry(QRect(170, 140, 450, 24))
        self.tietokantaLineEdit.setFont(font)
        self.kayttajatunnusLineEdit = QLineEdit(self.frame)
        self.kayttajatunnusLineEdit.setObjectName(u"kayttajatunnusLineEdit")
        self.kayttajatunnusLineEdit.setGeometry(QRect(170, 200, 450, 24))
        self.kayttajatunnusLineEdit.setFont(font)
        self.salasanaLineEdit = QLineEdit(self.frame)
        self.salasanaLineEdit.setObjectName(u"salasanaLineEdit")
        self.salasanaLineEdit.setGeometry(QRect(170, 260, 450, 24))
        self.salasanaLineEdit.setFont(font)
        self.yhteysLabel = QLabel(Dialog)
        self.yhteysLabel.setObjectName(u"yhteysLabel")
        self.yhteysLabel.setGeometry(QRect(110, 30, 280, 30))
        font1 = QFont()
        font1.setPointSize(16)
        self.yhteysLabel.setFont(font1)
        self.esitkatseluLabel = QLabel(Dialog)
        self.esitkatseluLabel.setObjectName(u"esitkatseluLabel")
        self.esitkatseluLabel.setGeometry(QRect(110, 580, 130, 30))
        self.esitkatseluLabel.setFont(font1)
        self.esikatseluTableWidget = QTableWidget(Dialog)
        self.esikatseluTableWidget.setObjectName(u"esikatseluTableWidget")
        self.esikatseluTableWidget.setGeometry(QRect(80, 630, 791, 351))
        self.nimiLabel = QLabel(Dialog)
        self.nimiLabel.setObjectName(u"nimiLabel")
        self.nimiLabel.setGeometry(QRect(110, 470, 280, 30))
        font2 = QFont()
        font2.setPointSize(15)
        self.nimiLabel.setFont(font2)
        self.tauluTaiNakumaComboBox = QComboBox(Dialog)
        self.tauluTaiNakumaComboBox.setObjectName(u"tauluTaiNakumaComboBox")
        self.tauluTaiNakumaComboBox.setGeometry(QRect(110, 520, 150, 27))
        self.nimiComboBox = QComboBox(Dialog)
        self.nimiComboBox.setObjectName(u"nimiComboBox")
        self.nimiComboBox.setGeometry(QRect(350, 520, 450, 27))
        self.haePushButton = QPushButton(Dialog)
        self.haePushButton.setObjectName(u"haePushButton")
        self.haePushButton.setGeometry(QRect(350, 570, 140, 30))
        self.haePushButton.setFont(font)
        self.viePushButton = QPushButton(Dialog)
        self.viePushButton.setObjectName(u"viePushButton")
        self.viePushButton.setGeometry(QRect(510, 570, 140, 30))
        self.viePushButton.setFont(font)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.palvelinLabel.setText(QCoreApplication.translate("Dialog", u"Palvelin", None))
        self.porttiLabel.setText(QCoreApplication.translate("Dialog", u"Portti", None))
        self.tietokantaLabel.setText(QCoreApplication.translate("Dialog", u"Tietokanta", None))
        self.kayttajatunnusLabel.setText(QCoreApplication.translate("Dialog", u"K\u00e4ytt\u00e4j\u00e4tunnus", None))
        self.salasanaLabel.setText(QCoreApplication.translate("Dialog", u"Salasana", None))
        self.yhteysPushButton.setText(QCoreApplication.translate("Dialog", u"Testaa yhteys", None))
        self.palvelinLineEdit.setText("")
        self.palvelinLineEdit.setPlaceholderText(QCoreApplication.translate("Dialog", u"Palvelimen nimi tai IP-osoite", None))
        self.porttiLineEdit.setPlaceholderText(QCoreApplication.translate("Dialog", u"TCP-portin numero, oletus 5432", None))
        self.tietokantaLineEdit.setPlaceholderText(QCoreApplication.translate("Dialog", u"Tietokannan nimi, hallintatieokanta postgres", None))
        self.kayttajatunnusLineEdit.setPlaceholderText(QCoreApplication.translate("Dialog", u"K\u00e4ytt\u00e4j\u00e4tunnus, oletusp\u00e4\u00e4k\u00e4ytt\u00e4j\u00e4 postgres", None))
        self.salasanaLineEdit.setPlaceholderText(QCoreApplication.translate("Dialog", u"K\u00e4ytt\u00e4j\u00e4n salasana", None))
        self.yhteysLabel.setText(QCoreApplication.translate("Dialog", u"Tietokantayhteyden asetukset", None))
        self.esitkatseluLabel.setText(QCoreApplication.translate("Dialog", u"Esikatselu", None))
        self.nimiLabel.setText(QCoreApplication.translate("Dialog", u"Taulun tai n\u00e4kym\u00e4n nimi", None))
        self.haePushButton.setText(QCoreApplication.translate("Dialog", u"Hae", None))
        self.viePushButton.setText(QCoreApplication.translate("Dialog", u"Vie tiedostoon", None))
    # retranslateUi

