"""
        aplicación para hacer cálculos en función del precio del dólar, 
                para facilitar los procesos de los pagos    
"""
from windows import MainWindow, QApplication, QWidget
import sys

app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec_()

