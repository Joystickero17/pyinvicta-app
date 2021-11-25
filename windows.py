from PySide2.QtWidgets import QApplication, QPushButton, QVBoxLayout, QWidget, QLabel, QMainWindow
from utils import get_price, HiloPrecio

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("Invicta App")
        self.dolar_label = QLabel("Cargando")

        self.hilo_precio = HiloPrecio(self.change_price)
        self.hilo_precio.start()

        # boton para actualizar
        button = QPushButton("Actualizar")

        # asignaciones del layout
        layout = QVBoxLayout()
        layout.addWidget(self.dolar_label)
        layout.addWidget(button)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)


    def change_price(self, precio):
        """  
            funcion que se ejecuta dentro del hilo HiloPrecio para poder cambiar el texto de dolar_label
            en el mismo instante en que se descarga
        """
        self.dolar_label.setText(precio)
        


        