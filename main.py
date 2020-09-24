# This is a sample Python script.
from urllib.request import urlopen
import json
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(100, 100, 1000, 1000)
    win.setWindowTitle("Test run")

    label = QtWidgets.QLabel(win)
    label.setText("My first label")
    label.move(50, 50)

    win.show()
    sys.exit(app.exec_())
# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    request = 'https://api.jikan.moe/v3/user/ZeboFTW/animelist/watching'

    json_obj = urlopen(request)
    data = json.load(json_obj)
    for anime in data['anime']:
        print(anime['title'])

    window()