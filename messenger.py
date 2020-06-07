from datetime import datetime

import requests
from PyQt5 import QtWidgets, QtCore
import clientui


class ExampleApp(QtWidgets.QMainWindow, clientui.Ui_MainWindows):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton.pressed.connect(self.send_message)

        self.last_timestamp = 0
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update_message)
        self.timer.start(1000)

    def send_message(self):
        username = self.lineEdit_2.text()
        password = self.lineEdit_3.text()
        text = self.textEdit.toPlainText()

        requests.get(
            'http://127.0.0.1:5000/send_message',
            json={
                'username': username,
                'text': text,
                'password': password},
        )
        self.textEdit.setText('')
        self.textEdit.repaint()

    def update_message(self):

        response = requests.get(
            'http://127.0.0.1:5000/get_messages',
            params={'after': self.last_timestamp}
        )
        messages = response.json()['messages']

        for message in messages:
            dt = datetime.fromtimestamp(message['timestamp'])
            dt = dt.strftime('%H:%M:%S %d/%m/%y')
            self.textBrowser.append(dt + ' ' + message['username'])
            self.textBrowser.append(message['text'])
            self.textBrowser.append('')
            self.last_timestamp = message['timestamp']


app = QtWidgets.QApplication([])
window = ExampleApp()
window.show()
app.exec_()
