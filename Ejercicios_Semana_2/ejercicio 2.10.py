'''
Ejemplo 2.10

Una modista, para realizar sus prendas de vestir, encarga las telas al extranjero.
Para cada pedido, tiene que proporcionar las medidas de la tela en pulgadas, 
pero ella generalmente las tiene en metros. Realice un algoritmo para ayudar a resolver el problema, 
determinando cuántas pulgadas debe pedir con base en los metros que requiere. 

## Represéntelo mediante el diagrama de flujo y el pseudocódigo (1 pulgada = 0.0254 m).
'''
class Modista:
    def __init__(self, metros):
        self.metros  = metros
        
        # constantes
        self.PULGADA = 0.0254
        self.METRO = 39.37
        
    def determinarPulgadasNecesarias(self):
        pulgadasNecesarias = 0
        pulgadasNecesarias = self.metros / self.PULGADA
        return pulgadasNecesarias

    # metodo extra, pasa de pulgadas a metros    
    def pasarPulgadasA_metros(self, nPulgadas):
        nMetros = 0
        nMetros = nPulgadas / self.METRO
        return nMetros
    
test = Modista(45)
print(test.determinarPulgadasNecesarias())
print(test.pasarPulgadasA_metros(1771.6535433070867))
    
