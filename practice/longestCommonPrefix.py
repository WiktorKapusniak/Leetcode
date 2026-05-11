lista = ["flower","flow","flight"]
def longestCommonPrefix(lista):
    if not lista:
        return ""
    for i in range(len(lista[0])):
        current_char = lista[0][i]
        for word in lista[1:]:
            if i>=len(word) or word[i] != current_char:
                return lista[0][:i]
    return lista[0]

print(longestCommonPrefix(lista))