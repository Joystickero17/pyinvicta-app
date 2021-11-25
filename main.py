"""
    aplicación para hacer cálculos en función del precio del dólar, 
    para facilitar los procesos de los pagos    
"""


from PySide2.QtWidgets import QApplication, QWidget

import sys


app = QApplication(sys.argv)


window = QWidget()
window.show()


app.exec_()

