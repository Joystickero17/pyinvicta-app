from PySide2 import QtCore
from PySide2.QtCore import QSize, Qt
from PySide2.QtGui import QFont, QIntValidator, QMovie
from PySide2.QtWidgets import QApplication, QHBoxLayout, QLineEdit, QPushButton, QSpacerItem, QVBoxLayout, QWidget, QLabel, QMainWindow
from utils import HiloPrecio


class Boton(QPushButton):
    def __init__(self, text, color_number=0, *args):
        super(Boton, self).__init__(text)
        colorList = ("#2B308C", "#151340")
        self.setFixedHeight(60)
        self.setStyleSheet("QPushButton { background-color: "+colorList[color_number]+" ; color: white; border-radius: 7px;}")
        self.setFont(QFont("Arial", 22))


class TextBox(QLineEdit):
    def __init__(self, place_holder):
        super(TextBox, self).__init__()
        self.setStyleSheet("QLineEdit {border-radius:7px; border: 0.5px solid gray}")
        self.setPlaceholderText(place_holder)
        self.setFixedHeight(40)
        self.setFont(QFont("Arial", 18))
        self.setValidator(QIntValidator(0,1000000000,))


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        # variable para guardar el precio
        self._precio = float()

        # gif para loading
        self.loading = QMovie("img/caracol.gif")

        # colorear de blanco el fondo de la ventana
        self.setAutoFillBackground(True)
        pallete = self.palette()
        pallete.setColor(self.backgroundRole(), Qt.white)
        self.setPalette(pallete)

        self.setWindowTitle("Invicta App")

        # etiqueta secundaria del dolar
        dolar_description = QLabel("Precio del día: ")
        dolar_description.setFont(QFont("Arial", 20))
        dolar_description.setFixedHeight(30)

        # etiqueta que contiene el precio del dolar
        self.dolar_label = QLabel()
        self.dolar_label.setMovie(self.loading)
        self.dolar_label.setFont(QFont("Arial", 23))
        self.dolar_label.setFixedHeight(200)
        
        # layout que contiene a la descripción del dolar
        dolar_layout = QHBoxLayout()
        dolar_layout.addWidget(dolar_description)
        dolar_layout.addWidget(self.dolar_label)

        # label de dolares a bolivares
        lbl_dollarbs = QLabel("Conversión de Dólares a Bolívares:")

        # label de bolívares a dólar
        lbl_bsdollar = QLabel("Conversión de Bolívares a Dólares")

        # Texto Dolares - Bolivares
        self.txt_dolares = TextBox("$")
        self.txt_dolares.textChanged.connect(self.calculo_dolarbs)

        # Texto Dolares - bolivares result
        self.txt_dolarbs_result = TextBox("Bs")
        self.txt_dolarbs_result.setReadOnly(True)

        # Texto Bolívares
        self.txt_bolivares = TextBox("Bs")
        self.txt_bolivares.textChanged.connect(self.calculo_bsdolar)

        # Texto Bolívares - Dolares result
        self.txt_bsdolar_result = TextBox("$")
        self.txt_bsdolar_result.setReadOnly(True)
        
        # inicialización de hilo que cambia el precio
        self.hilo_precio = HiloPrecio(self.change_price)
        self.update_price()

        self.setFixedSize(QSize(600,450))
        
        # boton para actualizar
        button = Boton("Actualizar", 0)
        button.clicked.connect(self.update_price)

        # boton para cerrar
        btn_Exit = Boton("Salir", 1)
        btn_Exit.clicked.connect(self.close)        

        # asignaciones del layout principal
        main_layout = QVBoxLayout()
        main_layout.addLayout(dolar_layout)

        # layout de los botones
        button_layout = QHBoxLayout()
        button_layout.addWidget(button)
        button_layout.addWidget(btn_Exit)        

        # layout de TXTs izquierdo
        left_v_txt_layout = QVBoxLayout()
        left_v_txt_layout.addWidget(lbl_dollarbs)
        left_v_txt_layout.addWidget(self.txt_dolares)
        left_v_txt_layout.addWidget(lbl_bsdollar)
        left_v_txt_layout.addWidget(self.txt_bolivares)

        # layouts de TXTs derecho
        right_v_txt_layout = QVBoxLayout()
        right_v_txt_layout.addItem(QSpacerItem(0,20))
        right_v_txt_layout.addWidget(self.txt_dolarbs_result)
        right_v_txt_layout.addItem(QSpacerItem(0,40))
        right_v_txt_layout.addWidget(self.txt_bsdolar_result)
        right_v_txt_layout.setContentsMargins(0,23,10,0)
        
        # right_v_txt_layout.setAlignment(Qt.AlignCenter)
        
        # layout que contiene los layouts de los TXT
        main_txt_layout = QHBoxLayout()

        main_layout.addLayout(main_txt_layout)
        main_txt_layout.addLayout(left_v_txt_layout)
        main_txt_layout.addLayout(right_v_txt_layout)
        main_layout.addLayout(button_layout)

        widget = QWidget()
        widget.setLayout(main_layout)
        self.setCentralWidget(widget)

    def calculo_dolarbs(self):
        result = round(self.get_precio() * float(self.txt_dolares.text() or 0.0), 2)
        self.txt_dolarbs_result.setText(str(result))
    
    def calculo_bsdolar(self):
        result = round(float(self.txt_bolivares.text() or 0.0)/self.get_precio() , 2)
        self.txt_bsdolar_result.setText(str(result))

    def set_precio(self, precio):
        self._precio = precio

    def get_precio(self):
        return self._precio
        
    def update_price(self):
        self.dolar_label.setMovie(self.loading)
        self.loading.stop()
        self.loading.start()
        self.hilo_precio.start()

    def change_price(self, precio):
        """  
            funcion que se ejecuta dentro del hilo HiloPrecio para poder cambiar el texto de dolar_label
            en el mismo instante en que se descarga
        """
        self.dolar_label.setText(str(precio))
        self.set_precio(precio)
        


