import requests
from bs4 import BeautifulSoup
from PySide2.QtCore import QThread, Signal,Slot, QObject
import time

def get_price():
    # función para sacar los precios de la página del BCV
    response = requests.get("http://bcv.org.ve/")
    print("cargando precio")
    soup = BeautifulSoup(response.text, "html.parser")
    dolar_container =soup.find(id="dolar")
    dolar_price = dolar_container.find("strong")
    return dolar_price.text.replace(",", ".")

class HiloPrecio(QThread):
    precio_signal = Signal(str)

    def __init__(self, funcion):
        super(HiloPrecio, self).__init__()
        self.funcion = funcion

    def run(self):
        precio = get_price()
        self.funcion(precio)
        self.precio_signal.emit("hello")


        





