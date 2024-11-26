from aeronave import Aeronave
from cliente import AvionCarga
from avion_comercial import AvionComercial
from avion_regional import AvionRegional
from avion_internacional import AvionInternacional
from avion_carga import AvionMixto
from depositos import AvionMixtoEspecial

def main():
    aeronave = Aeronave ()
    aeronave.set_marca("azus")
    aeronave.set_modelo("zesna")
    aeronave.set_capacidad_combustible(2)
    aeronave.set_peso(12)

    avion_comercial = AvionComercial()
    avion_comercial.set_marca("azus")
    avion_comercial.set_modelo("Boeing 747")
    avion_comercial.set_capacidad_combustible(2)
    avion_comercial.set_peso(12)
    avion_comercial.set_capacidad_pasajeros(23)
    avion_comercial.set_rango_vuelo(12)

    avion_regional = AvionRegional()
    avion_regional.set_marca("azus")
    avion_regional.set_modelo("Embraer E175")
    avion_regional.set_capacidad_combustible(2)
    avion_regional.set_peso(12)
    avion_regional.set_capacidad_pasajeros(23)
    avion_regional.set_rango_vuelo(12)
    avion_regional.set_cantidad_asientos_clase_economica(23)

    avion_internacional = AvionInternacional()
    avion_internacional.set_marca("azus")
    avion_internacional.set_modelo("Airbus A380")
    avion_internacional.set_capacidad_combustible(2)
    avion_internacional.set_peso(12)
    avion_internacional.set_capacidad_pasajeros(23)
    avion_internacional.set_rango_vuelo(12)
    avion_internacional.set_numero_asientos_premium(56)

    avion_mixto = AvionMixto()
    avion_mixto.set_marca("azus")
    avion_mixto.set_modelo("Boeing 737 Combi")
    avion_mixto.set_capacidad_combustible(2)
    avion_mixto.set_peso(12)
    avion_mixto.set_capacidad_pasajeros(23)
    avion_mixto.set_rango_vuelo(12)
    avion_mixto.set_capacidad_carga(6)
    avion_mixto.set_capacidad_maxima_carga(12)

    avion_carga = AvionCarga()
    avion_carga.set_capacidad_maxima_carga(435)

    avion_mixto_especial = AvionMixtoEspecial()
    avion_mixto_especial.set_marca("azus")
    avion_mixto_especial.set_modelo("Boeing 757 Combi")
    avion_mixto_especial.set_capacidad_combustible(2)
    avion_mixto_especial.set_peso(12)
    avion_mixto_especial.set_capacidad_pasajeros(23)
    avion_mixto_especial.set_rango_vuelo(12)
    avion_mixto_especial.set_capacidad_maxima_carga(13)
    avion_mixto_especial.set_capacidad_carga(23)
    avion_mixto_especial.set_numero_cabinas_especiales(23)


    print("Aeronave")
    print(aeronave.mostrar_info())

    print("Avion comercial")
    print(avion_comercial.mostrar_info_comercial())

    print("Avion regional")
    print(avion_regional.mostrar_info_regional())

    print("Avion internacional")
    print(avion_internacional.mostrar_info_internacional())

    print("clientes")
    print(avion_carga.mostrar_info_carga())

    print("Avion de carga")
    print(avion_mixto.mostrar_info_mixto())

    print("Depositos")
    print(avion_mixto_especial.mostrar_info_especial())


if __name__ == "__main__":
    main()
