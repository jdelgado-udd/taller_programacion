def eficiencia(distancia_km, combustible_litros):
    return (combustible_litros / distancia_km) * 100

def velocidad_promedio(distancia_km, tiempo_horas):
    return distancia_km / tiempo_horas

def carga_relativa(peso_carga_ton, capacidad_max=20):
    return (peso_carga_ton / capacidad_max) * 100