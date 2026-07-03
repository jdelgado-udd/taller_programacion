class Arma:
    nombre: str
    daño: int
    
    def __init__(self, daño: int, nombre: str):
        self.daño = daño
        self.nombre = nombre

class Melee(Arma):
    alcance: int
    
    def __init__(self, daño: int, nombre: str, alcance: int):
        super().__init__(daño, nombre)
        self.alcance = alcance

class Rango(Arma):
    potenciador: float # por distancia
    cargador: int
    
    def __init__(self, daño: int, nombre: str, potenciador: float, cargador: int):
        super().__init__(daño, nombre)
        self.potenciador = potenciador
        self.cargador = cargador

cheese: Melee = Melee(0, "Cheese", 3)
glock: Rango = Rango(18, "Glock", 0.02, 12)

def imprimir_arma(arma: Arma):
    print(f"Esta arma se llama {arma.nombre} y hace {arma.daño} puntos de daño.")
    
    if isinstance(arma, Melee):
        print(f"Se clasifica como un melee con alcance de {arma.alcance}")
    
    if isinstance(arma, Rango):
        print(f"Se clasifica como un arma de rango con potenciador {arma.potenciador * 100}% y cargador de {arma.cargador} unidades.")

imprimir_arma(glock)
imprimir_arma(cheese)