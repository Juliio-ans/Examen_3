from aeronave import Aeronave

class AvionCarga(Aeronave):
    def __init__(self):
        super().__init__()
        Aeronave.__init__(self)
        self.capacidad_maxima_carga = 0

    def get_capacidad_maxima_carga(self):
        return self.capacidad_maxima_carga

    def set_capacidad_maxima_carga(self, capacidad):
        self.capacidad_maxima_carga = capacidad

    def mostrar_info_carga(self):
        return f" Capacidad máxima de carga: {self.capacidad_maxima_carga} kg"
