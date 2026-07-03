from random import randint

POSIBLES_PINTAS = ["♦️", "♥️", "♣️", "♠️"]
POSIBLES_TIPOS = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

class Carta:
    pinta: str
    tipo: str
    
    def __init__(self, pinta: str, tipo: str):
        if pinta not in POSIBLES_PINTAS or tipo not in POSIBLES_TIPOS:
            raise ValueError
        
        self.pinta = pinta
        self.tipo = tipo

    def valor(self) -> int:
        return POSIBLES_TIPOS.index(tipo) + 1
    
    def ver(self) -> str:
        return f"[{self.pinta}  {self.tipo}]"
    
    def __str__(self) -> str:
        return self.ver()

class Baraja:
    cartas: list[Carta] = []
    
    def __init__(self):
        for pinta in POSIBLES_PINTAS:
            for tipo in POSIBLES_TIPOS:
                self.cartas.append(Carta(pinta, tipo))
    
    def quitar_cartas(self, cantidad: int) -> list[Carta]:
        cartitas: list[Carta] = []
        
        for _ in range(cantidad):
            cartitas.append(self.cartas.pop(randint(0, len(self.cartas))))
        
        return cartitas
    
    def mostrar(self):
        print(*self.cartas)

baraja: Baraja = Baraja()
baraja.quitar_cartas(3)
baraja.mostrar()