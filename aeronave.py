class Aeronave:
    def __init__(self):
        self._marca = ""
        self._modelo = ""
        self._capacidad_combustible = 0
        self._peso = 0

    # Getters y Setters
    def get_marca(self):
        return self._marca

    def set_marca(self, marca):
        self._marca = marca

    def get_modelo(self):
        return self._modelo

    def set_modelo(self, modelo):
        self._modelo = modelo


    def get_capacidad_combustible(self):
        return self._capacidad_combustible


    def set_capacidad_combustible(self, capacidad_combustible):
        self._capacidad_combustible = capacidad_combustible


    def get_peso(self):
        return self._peso


    def set_peso(self, peso):
        self._peso = peso

    def mostrar_info(self):
        return f"Aeronave, Marca: {self._marca} Modelo: {self._modelo}, combustible: {self._capacidad_combustible}L, peso: {self._peso}kg"
