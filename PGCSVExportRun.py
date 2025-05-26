import os # polkumääritykset
import sys # käynnistysargumentit

from PySide6 import QtWidgets 

import dbOperations

from PGCSVExportTool import Ui_MainWindow

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()

        # Kutsutaan käyttöliittymän muodostusmetodia setupUi
        self.ui.setupUi(self)

        # Tietokantayhteys
        self.serverName = ''
        self.portNumber = ''
        self.databaseName = ''
        self.userName = ''
        self.password = ''

        # Tietokantaobjekti
        self.dbObjectType = ''
        self.dbObjectName = ''

        # SIGNAALIT
        self.ui.yhteysPushButton.clicked.connect(self.connectDb)
        self.ui.tyyppiComboBox.currentIndexChanged.connect(self.getObjectNames)
        self.ui.nimiComboBox.currentIndexChanged.connect(self.updatePreview)

        # Tietokantayhteys
        # self.serverName = self.ui.palvelinLineEdit.text()
        # self.portNumber = self.ui.porttiLineEdit.text()
        # self.databaseName = self.ui.tietokantaLineEdit.text()
        # self.userName = self.ui.kayttajatunnusLineEdit.text()
        # self.password = self.ui.salasanaLineEdit.text()
        self.serverName = '127.0.0.1'
        self.portNumber = '5432'
        self.databaseName = 'autolainaus'
        self.userName = 'postgres'
        self.password = 'Q2werty7'

        self.settingsDictionary = {
            'server': self.serverName,
            'port': self.portNumber,
            'database': self.databaseName,
            'userName': self.userName,
            'password': self.password
        }

    def connectDb(self):
        try:
            dbConnection = dbOperations.DbConnection(self.settingsDictionary)
            table = 'information_schema.tables'
            column = ['table_type']
            filterText = f"table_schema NOT IN ('information_schema', 'pg_catalog')"

            objectTypes = dbConnection.filterColumnsFromTable(table, column, filterText)
            self.ui.statusbar.showMessage('Yhteyden muodostus tietokantaan onnistui', 10000)

            # tehtään monikkolistasta merkkijonolista
            self.ui.tyyppiComboBox.clear()
            cleanedObjectTypeList = ['Tietokantaobjektin tyyppi']
            for value in objectTypes:
                objectType = value[0]
                if objectType not in cleanedObjectTypeList:
                    cleanedObjectTypeList.append(objectType)
            self.ui.tyyppiComboBox.addItems(cleanedObjectTypeList)

        except Exception as e:
            errorDetails = str(e)
            self.openWarning('Tyhjä!', 'Taulukkotyyppejä ei löytynyt.', errorDetails)

    def getObjectNames(self):
        try:
            dbConnection = dbOperations.DbConnection(self.settingsDictionary)
            table = 'information_schema.tables'
            columns = ['table_schema', 'table_name']
            tableType = self.ui.tyyppiComboBox.currentText()

            filterText = f"table_type = '{tableType}' AND table_schema NOT IN ('information_schema', 'pg_catalog')"

            objectNames = dbConnection.filterColumnsFromTable(table, columns, filterText)
            self.ui.statusbar.showMessage('Haettiin tietokantaobjektien nimet')

            self.ui.nimiComboBox.clear()
            cleanedObjectNameList = ['Tietokantaobjektin nimi']
            for value in objectNames:
                objectSchema = value[0]
                objectName = value[1]
                objectFullName = f'{objectSchema}.{objectName}'
                cleanedObjectNameList.append(objectFullName)

            self.ui.nimiComboBox.addItems(cleanedObjectNameList)

        except Exception as e:
            errorDetails = str(e)
            self.openWarning('Tyhjä!', 'Taulukkonimiä ei löytynyt.', errorDetails)

    def updatePreview(self):
        selectedObject = self.ui.nimiComboBox.currentText()

        if selectedObject == 'Tietokantaobjektin nimi' or '':
            self.ui.esikatseluTableWidget.clear()
            self.ui.esikatseluTableWidget.setColumnCount(0)
            self.ui.esikatseluTableWidget.setRowCount(0)
            
        else:

            try:
                dbConnection = dbOperations.DbConnection(self.settingsDictionary)
                self.resultSet = dbConnection.readAllColumnsFromTable(selectedObject)
                print(self.resultSet)
                self.ui.esikatseluTableWidget.clear()
                self.ui.esikatseluTableWidget.setColumnCount(0)
                self.ui.esikatseluTableWidget.setRowCount(0)              
                numberOfRows = len(self.resultSet)
                columnCount = len(self.resultSet[0])
                self.ui.esikatseluTableWidget.setRowCount(numberOfRows)
                self.ui.esikatseluTableWidget.setColumnCount(columnCount)
                headerRow = dbConnection.getColumnNames(selectedObject)
                print(headerRow)
                self.ui.esikatseluTableWidget.setHorizontalHeaderLabels(headerRow)
                for row in range(numberOfRows):
                    for column in range(columnCount):
                        data = QtWidgets.QTableWidgetItem(str(self.resultSet[row][column]))
                        self.ui.esikatseluTableWidget.setItem(row, column, data)
                
            except Exception as e:
                errorDetails = str(e)
                self.openWarning('Tyhjä!', 'Tauluun ei saatu yhteyttä', errorDetails)


    def openWarning(self, title, message, detailedMessage):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Critical)
        msgBox.setWindowTitle(title)
        msgBox.setText(message)
        msgBox.setDetailedText(detailedMessage)
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')
    window = MainWindow()
    window.show()
    app.exec()