def primos(n):
    resposta = []
    
    for numero in range(2,n):
        primo = True
        
        for x in range(2,numero-1):
            if numero % x == 0:
                primo = False
                break

        if primo:
            resposta.append(numero)
    return resposta