'''
Ejemplo 2.11

La conagua requiere determinar el pago que debe realizar una persona por el total de metros cúbicos
que consume de agua al llenar una alberca (ver figura 2.5).

## Realice un algoritmo y reperséntelo mediante un diagrama de flujo y el pseudocódigo
que permita determinar ese pago. 
Las variables requeridas para la solución de este problema se muestran en la tabla 2.12.
'''

def calcularMetrosCubicosAlberca(ancho, largo, profundidad):
    precioPorMetroCubico = 5600
    
    volumenAlberca = ancho * largo * profundidad
    precioTotalPagar = volumenAlberca * precioPorMetroCubico
    return precioTotalPagar

print(calcularMetrosCubicosAlberca(4, 7, 2))