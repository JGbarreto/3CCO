
#Nomes: João Gabriel, Cauã Ciconelli, Filipe Filipus
def levenshtein(s1, s2):
    
    matriz = []
    for _ in range(len(s1) + 1):
        linha = []
        for _ in range(len(s2) + 1):
            linha.append(0)
        matriz.append(linha)

 
    for i in range(len(s1) + 1):
        matriz[i][0] = i
    for j in range(len(s2) + 1):
        matriz[0][j] = j

    
    for i in range(1, len(s1) + 1):
        for j in range(1, len(s2) + 1):
            if s1[i - 1] == s2[j - 1]:
                custo_substituicao = 0
            else:
                custo_substituicao = 1
            delecao = matriz[i - 1][j] + 1
            insercao = matriz[i][j - 1] + 1
            substituicao = matriz[i - 1][j - 1] + custo_substituicao
            matriz[i][j] = min(delecao, insercao, substituicao)

    
    return matriz[-1][-1]


while(True):
    palavra_predefinida = "Saphnelo"

    palavra_usuario = input("Digite uma palavra para comparar com '{}': ".format(palavra_predefinida))

    distancia = levenshtein(palavra_predefinida, palavra_usuario)

    print("A distância de Levenshtein entre '{}' e '{}' é: {}".format(palavra_predefinida, palavra_usuario, distancia))