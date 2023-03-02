def maiormenor(numeros):
    
    maior = numeros[0]
    menor = numeros[0]
    
    for numero in numeros:
        if numero > maior:
            maior = numero
        elif numero < menor:
            menor = numero
    
    resposta = {
        "menor": menor,
        "maior": maior
    }

    return resposta

        
