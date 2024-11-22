# avion_comercial.py
from aeronave import Aeronave

class AvionComercial(Aeronave):
    def __init__(self):
        super().__init__()
        Aeronave.__init__(self)
        self._capacidad_pasajeros = 0
        self._rango_vuelo = 0

    # Getters y Setters

    def get_capacidad_pasajeros(self):
        return self._capacidad_pasajeros

    def set_capacidad_pasajeros(self, capacidad_pasajeros):
        self._capacidad_pasajeros = capacidad_pasajeros

    def get_rango_vuelo(self):
        return self._rango_vuelo


    def set_rango_vuelo(self, rango_vuelo):
        self._rango_vuelo = rango_vuelo

    def mostrar_info_comercial(self):
        base_info = super().mostrar_info()
        return f"{base_info} Capacidad para {self._capacidad_pasajeros} pasajeros, rango de vuelo: {self._rango_vuelo} km"
