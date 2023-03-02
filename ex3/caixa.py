import math

def cedulas(valor):
    
    resultado = {
        "cedulas100": 0,
        "cedulas50" : 0,
        "cedulas20" : 0,
        "cedulas10" : 0,
        "cedulas5": 0,
        "cedulas2": 0,
        "moeda1": 0
    }
    
    if valor >= 100:
        resultado["cedulas100"] = math.trunc(valor/100)
        valor = valor % 100
    
    if valor >= 50:
        resultado["cedulas50"] = math.trunc(valor/50)
        valor = valor % 50
    
    if valor >= 20:
        resultado["cedulas20"] = math.trunc(valor/20)
        valor = valor % 20

    if valor >= 10:
        resultado["cedulas10"] = math.trunc(valor/10)
        valor = valor % 10
    
    if valor >= 5:
        resultado["cedulas5"] = math.trunc(valor/5)
        valor = valor % 5

    if valor >= 2:
        resultado["cedulas2"] = math.trunc(valor/2)
        valor = valor % 2
    
    if valor == 1:
        resultado["moeda1"] = 1
    
    return resultado