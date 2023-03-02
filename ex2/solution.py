from votos import calcula_votos
votosc1 = int(input('Votos do candidato 1: '))
votosc2 = int(input('Votos do candidato 2: '))
votosc3 = int(input('Votos do candidato 3: '))
votosb = int(input('Votos brancos: '))
votosn = int(input('Votos nulos: '))

print(calcula_votos(votosc1,votosc2,votosc3,votosb,votosn))