### EJEMPLO 2.5 ---------------------------------------------------
## ingresar las medidas del terreno altura total(A), base(b) y altura menor(C)
class CalcularArea:
    def __init__(self):
        self.A = int(input("Ingrese la altura total del terreno: "))
        self.B = int(input("Ingrese la medida de la base del terreno: "))
        self.C = int(input("Ingrese la altura menor del terreno: "))
        self.opciones()

# Podemos hacerlo de 2 formas
    def opciones(self):
        opcion = input("de que forma lo hacemos? Forma 1 o Forma 2: ")
        if opcion == "1":
            print("El area total es: ", self.calcularPorPartes())
        elif opcion == "2":
            print("El area total es: ", self.calcularConFormula())
            
# dividiendo la figura en un rectangulo y un triangulo calcular sus areas por separado y sumar sus areas
    def calcularPorPartes(self):
        # calcular el area del rectangulo
        areaRectangulo = self.B * self.C
        # calcular areal del triangulo
        areaTriangulo = (self.A - self.C) * self.B / 2
        # ahora sumamos las 2 areas
        areaTotal = areaRectangulo + areaTriangulo
        return  areaTotal
    
    def calcularConFormula(self):
        # calcular el area total con la formula
        areaTotal = (self.A + self.C) * self.B / 2
        return areaTotal

    
test = CalcularArea()