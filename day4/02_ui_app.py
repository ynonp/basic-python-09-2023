from PySide6.QtWidgets import *
import app_ui

def button_1_clicked():
    ui.label_2.setText(str(int(ui.label_2.text()) + 1))


app = QApplication()
w = QMainWindow()
ui = app_ui.Ui_MainWindow()
ui.setupUi(w)
w.show()

ui.pushButton.clicked.connect(button_1_clicked)

app.exec()

