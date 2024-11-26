from avion_comercial import AvionComercial

class AvionRegional(AvionComercial):
    def __init__(self):
        super().__init__()
        AvionComercial.__init__(self)
        self._motorelices = 0

 # Getters y Setters

    def get_cantidad_asientos_clase_economica(self):
            return self._motorelices

    def set_cantidad_asientos_clase_economica(self, motorelices):
            self._motorelices = motorelices

    def mostrar_info_regional(self):
        base_info = super().mostrar_info_comercial()
        return f"{base_info} No motores de elices: {self._motorelices}"
