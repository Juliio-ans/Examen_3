# avion_carga.py
from avion_comercial import AvionComercial
from cliente import AvionCarga

class AvionMixto(AvionComercial, AvionCarga):
    def __init__(self):
        super().__init__()
        AvionComercial.__init__(self)
        AvionCarga.__init__(self)
        self.capacidad_carga = 0

    def get_capacidad_carga(self):
        return self.capacidad_carga

    def set_capacidad_carga(self, capacidad_carga):
        self.capacidad_carga = capacidad_carga

    def mostrar_info_mixto(self):
        base_info_carga = super().mostrar_info_carga()
        base_info = super().mostrar_info_comercial()
        return f"{base_info} {base_info_carga} Capacidad de carga: {self.capacidad_carga} kg"
