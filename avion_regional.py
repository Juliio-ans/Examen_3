# avion_regional.py
from avion_comercial import AvionComercial

class AvionRegional(AvionComercial):
    def __init__(self):
        super().__init__()
        AvionComercial.__init__(self)
        self._cantidad_asientos_clase_economica = 0

 # Getters y Setters

    def get_cantidad_asientos_clase_economica(self):
            return self._cantidad_asientos_clase_economica

    def set_cantidad_asientos_clase_economica(self, cantidad_asientos_clase_economica):
            self._cantidad_asientos_clase_economica = cantidad_asientos_clase_economica

    def mostrar_info_regional(self):
        base_info = super().mostrar_info_comercial()
        return f"{base_info} Asientos clase económica: {self._cantidad_asientos_clase_economica}"
