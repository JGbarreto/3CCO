def levenshtein (str1, str2):
    len1 = len(str1)
    len2 = len(str2)
    matrix = [[0 for x in range(len2+1)] for y in range(len1+1)]
    for i in range(len1+1):
        for j in range(len2+1):
            if i == 0: 
                matrix[0][j] = j
            elif j == 0:
                matrix[i][0] = i
            else:
                cost = 0 if str1[i-1] == str2[j-1] else 1
                matrix[i][j] = min(matrix[i-1][j] + 1, matrix[i][j-1] + 1, matrix[i-1][j-1] + cost)
    return matrix[len1][len2]

def did_you_mean(main_word, input_word):
    if(isinstance(input_word, str)):
        iterations = levenshtein(main_word, input_word)
        if  iterations <= len(main_word)/2 and iterations != 0:
            print(f'Você quis dizer "{main_word}"?\n')
            return main_word
        print("Nome correto!\n")
        return input_word

