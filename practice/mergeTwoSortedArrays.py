lista1 = [1,2,3,4,5]
lista2 = [6,7,8,9,10,11]

def mergeTwoSortedArrays(lista1, lista2):
    if not lista1 and not lista2:
        return []
    res = []
    if len(lista1)>=len(lista2):
        for i in lista1:
            res.append(i)
            while lista2 and lista2[0]<=i:
                res.append(lista2[0])
                lista2 = lista2[1:]
    else: 
        for i in lista2:
            res.append(i)
            while lista1 and lista1[0]<=i:
                res.append(lista1[0])
                lista1= lista1[1:]
    return res


print(mergeTwoSortedArrays(lista1,lista2))