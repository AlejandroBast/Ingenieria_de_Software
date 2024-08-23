# convertimos los litros a galones
class ProductorLeche:
    def __init__(self, litros, pagoPorGalon):
        self.litros = litros
        self.pagoPorGalon = pagoPorGalon
        
    def convertirLitrosAGalones(self):
        galones = self.litros / 3.785
        return galones
    # calculamos el pago total
    def calcularPago(self):
        pagoTotal = self.convertirLitrosAGalones() * self.pagoPorGalon
        return pagoTotal
    
test = ProductorLeche(545, 200)
print(test.convertirLitrosAGalones())
print(test.calcularPago())