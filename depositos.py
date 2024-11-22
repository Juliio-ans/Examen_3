# depositos.py
from avion_carga import AvionMixto

class AvionMixtoEspecial(AvionMixto):
    def __init__(self):
        super().__init__()
        self._numero_cabinas_especiales = 0

    def get_numero_cabinas_especiales(self):
        return self._numero_cabinas_especiales

    def set_numero_cabinas_especiales(self, numero_cabinas):
        self._numero_cabinas_especiales = numero_cabinas

    def mostrar_info_especial(self):
        base_info = super().mostrar_info_mixto()
        return f" {base_info} Número de cabinas especiales: {self._numero_cabinas_especiales}"
