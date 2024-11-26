from avion_comercial import AvionComercial

class AvionInternacional(AvionComercial):
    def __init__(self):
        super().__init__()
        AvionComercial.__init__(self)
        self._numero_asientos_premium = 0

    def get_numero_asientos_premium(self):
        return self._numero_asientos_premium

    def set_numero_asientos_premium(self, numero_asientos_premium):
        self._numero_asientos_premium = numero_asientos_premium


    def mostrar_info_internacional(self):
        base_info = super().mostrar_info_comercial()
        return f"{base_info} clase premium: {self._numero_asientos_premium}"
