
import operadores as op
import unicodedata

# NOMES:
# CAUA DA SILVA CICONELLI
# FILIPE FILIPUS GUIRALDINI
# FELIPE CORREA
# JOÃO GABRIEL 
# JOÃO SALES SANTANA

# Constantes
TESTE   = False

# caracteres usados em operadores
OPERADORES = "%*/+-!^="

# caracteres usados em números inteiros
DIGITOS = "0123456789"

# ponto decimal
PONTO = "."

# todos os caracteres usados em um números float
FLOATS = DIGITOS + PONTO

# caracteres usados em nomes de variáveis
LETRAS  = "_abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ@?.,~-|:·"

# abre e fecha parenteses
ABRE_FECHA_PARENTESES = "()"

# categorias
OPERADOR   = 1 # para operadores aritméticos e atribuição
NUMERO     = 2 # para números: todos são considerados float
VARIAVEL   = 3 # para variáveis
PARENTESES = 4 # para '(' e ')

# Whitespace characters: space, newline, horizontal tab,
# vertical tab, form feed, carriage return
BRANCOS    = [' ', '\n', '\t', '\v', '\f', '\r']

# caractere que indica comentário
COMENTARIO = "#"

def normaliza(texto):
    """Normaliza os caracteres especiais para suas versões básicas."""
    texto_normalizado = unicodedata.normalize('NFKD', texto)
    texto_sem_acento = ''.join(
        c for c in texto_normalizado
        if not unicodedata.combining(c)
    )
    return texto_sem_acento

#------------------------------------------------------------
def tokeniza(exp):
    """(str) -> list

    Recebe uma string exp representando uma expressão e cria 
    e retorna uma lista com os itens léxicos que formam a
    expressão.

    Cada item léxico (= token) é da forma
       
        [item, tipo]

    O componente item de um token é 

        - um float: no caso do item ser um número; ou 
        - um string no caso do item ser um operador ou 
             uma variável ou um abre/fecha parenteses.

    O componente tipo de um token indica a sua categoria
    (ver definição de constantes acima). 

        - OPERADOR;
        - NUMERO; 
        - VARIAVEL; ou 
        - PARENTESES

    A funçao ignora tudo que esta na exp apos o caractere
    COMENTARIO (= "#").
    """
    # escreva o seu código abaixo
    exp = normaliza(exp)
    tokens = []
    i = 0
    while i < len(exp):
        if exp[i] == COMENTARIO:
            break
        elif exp[i] in OPERADORES:
            tokens.append([exp[i], OPERADOR])
        elif exp[i] in DIGITOS:
            num_str = ""
            while i < len(exp) and exp[i] in FLOATS:
                num_str += exp[i]
                i += 1
            if PONTO in num_str:
                tokens.append([float(num_str), NUMERO])
            else:
                tokens.append([int(num_str), NUMERO])
            i -= 1
        elif exp[i] in LETRAS:
            var_str = ""
            while i < len(exp) and exp[i] in LETRAS + DIGITOS:
                var_str += exp[i]
                i += 1
            tokens.append([var_str, VARIAVEL])
            i -= 1
        elif exp[i] in ABRE_FECHA_PARENTESES:
            tokens.append([exp[i], PARENTESES])
        elif exp[i] in BRANCOS:
            pass
        else:
            raise ValueError("Caractere não reconhecido: " + exp[i])
        i += 1
    return tokens

# Lista de palavras positivas e negativas para análise de sentimento
PALAVRAS_POSITIVAS = ["saudavel", "nutritivo", "fertil", "forte", "resistente", "produtivo", "bem-cuidado",
                     "bem-alimentado", "vigoroso", "sadio", "prospero", "reprodutivo", "robusto", "fortalecido",
                     "florescente", "sustentavel", "desenvolvido", "vital", "energico", "vitalidade",
                     "crescente", "abundante", "frutifero", "prazeroso", "harmonioso", "saude", "lucrativo"]

# Palavras negativas relacionadas à criação de gado
PALAVRAS_NEGATIVAS = ["doente", "contagioso", "parasitario", "infeccao", "mortal", "epidemia", "praga", "prejudicial",
                     "debilitado", "definhando", "contaminado", "fraco", "prejudicado", "doenca", "morto", "fracasso",
                     "perda", "desnutrido", "enfraquecido", "instavel", "destrutivo", "falencia", "estressante", "caotico"]

def analisar_sentimento(frase):
    """(str) -> str

    Recebe uma frase e determina se o sentimento geral é positivo,
    negativo ou neutro com base na contagem de palavras positivas e negativas.
    """
    frase = frase.lower()
    palavras = frase.split()
    contagem_positiva = sum(palavra in PALAVRAS_POSITIVAS for palavra in palavras)
    contagem_negativa = sum(palavra in PALAVRAS_NEGATIVAS for palavra in palavras)
    
    if contagem_positiva > contagem_negativa:
        return "Positiva"
    elif contagem_negativa > contagem_positiva:
        return "Negativa"
    else:
        return "Neutra"
