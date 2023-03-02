def calcula_votos(c1,c2,c3,b,n):
    total = c1+c2+c3+b+n

    retorno ={
        "total": total,
        "pc1": f'{((c1/total)*100):.2f}',
        "pc2": f'{((c2/total)*100):.2f}',
        "pc3": f'{((c3/total)*100):.2f}',
        "pb": f'{((b/total)*100):.2f}',
        "pn": f'{((n/total)*100):.2f}'
    }

    return retorno