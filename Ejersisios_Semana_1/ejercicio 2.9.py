class Trabajador:
    def __init__(self, horasTrabajadas, PagoPorHora):
        self.horasTrabajadas = horasTrabajadas
        self.PagoPorHora = PagoPorHora
    
    def calcularSueldoSemanal(self):
        sueldoSemanal = self.horasTrabajadas * self.PagoPorHora
        return sueldoSemanal
    

test = Trabajador(45, 5)
print(test.calcularSueldoSemanal())