from PyQt5.QtCore import pyqtSlot, QTimer
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout, QApplication

from api.WSService import WSService


class WeatherInformer(QWidget):

    def __init__(self):
        super().__init__()
        self.service = WSService()

        self.setWindowTitle("Weather controller v1.0")
        self.label_temp = QLabel("null")
        self.label_temp_name = QLabel("Температура:")
        self.h_layout_temp = QHBoxLayout()
        self.label_press = QLabel("null")
        self.label_press_name = QLabel("Давление:")
        self.h_layout_press = QHBoxLayout()
        self.label_humid = QLabel("null")
        self.label_humid_name = QLabel("Влажность:")
        self.h_layout_humid = QHBoxLayout()
        self.v_layout = QVBoxLayout()

        self.timer = QTimer()
        self.timer.timeout.connect(self.updateValues)
        self.timer.start(1000)

        self.setupUI()

    def setupUI(self):
        self.h_layout_temp.addWidget(self.label_temp_name)
        self.h_layout_temp.addWidget(self.label_temp)

        self.h_layout_press.addWidget(self.label_press_name)
        self.h_layout_press.addWidget(self.label_press)

        self.h_layout_humid.addWidget(self.label_humid_name)
        self.h_layout_humid.addWidget(self.label_humid)

        self.v_layout.addLayout(self.h_layout_temp)
        self.v_layout.addLayout(self.h_layout_press)
        self.v_layout.addLayout(self.h_layout_humid)

        self.setLayout(self.v_layout)
        self.setFixedSize(300, 200)
        self.show()

    @pyqtSlot()
    def updateValues(self):
        model = self.service.get_model()
        self.label_temp.setText(str(model.temperature))
        self.label_press.setText(str(model.pressure))
        self.label_humid.setText(str(model.humidity))


if __name__ == '__main__':
    app = QApplication([])
    w = WeatherInformer()
    app.exec_()
