import math

def calculaimc(peso,altura,sexo):
    
    resultado = {
        "imc": 0,
        "sexo": None,
        "cond": None
    }
    
    imc = peso/math.pow(altura,2)

    if sexo == 'F':
        
        resultado["imc"] = imc
        resultado["sexo"] = 'F'

        if imc < 19.1:
            resultado["cond"] = 'abaixo do peso'
        elif imc < 25.8:
            resultado["cond"] = 'no peso normal'
        elif imc < 27.3:
            resultado["cond"] = 'marginalmente acima do peso'
        elif imc < 32.3:
            resultado["cond"] = 'acima do peso ideal'
        else:
            resultado["cond"] = 'obeso'
    elif sexo == 'M':

        resultado["imc"] = imc
        resultado["sexo"] = 'F'

        if imc < 20.7:
            resultado["cond"] = 'abaixo do peso'
        elif imc < 26.4:
            resultado["cond"] = 'no peso normal'
        elif imc < 27.8:
            resultado["cond"] = 'marginalmente acima do peso'
        elif imc < 31.1:
            resultado["cond"] = 'acima do peso ideal'
        else:
            resultado["cond"] = 'obeso'
    return resultado
            
