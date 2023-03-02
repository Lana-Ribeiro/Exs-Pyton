def ordena_numeros(l):
    pos = 0
    it = 1
    while pos < len(l):
        while it < len(l):
            if l[pos] > l[it]:
                temp = l[pos]
                l[pos] = l[it]
                l[it] = temp
            it+=1

        pos+=1
        it=pos+1

    return l



        