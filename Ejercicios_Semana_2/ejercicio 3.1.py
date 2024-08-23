'''
Ejemplo 3.1

Se desea implementar un algoritmo para determinar cuál de dos valores proporcionados es el mayor. 

## Representarlo con pseudocódigo, diagrama de flujo y diagrama N/S.
'''

def cualEsMayor(valorA, valorB):
    if valorA > valorB:
        return valorA
    elif valorB > valorA:
        return valorB
    else:
        return "Los valores son iguales"
    
print(cualEsMayor(5, 6))
print(cualEsMayor(7, 6))
print(cualEsMayor(5, 5))
    