from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pyautogui
import tokeniza as tk
import operadores as op
import levenshtein as lv

def get_tweets(query, num_tweets):
    tweets = []
    
    # Configurações do Selenium
    driver = webdriver.Chrome()  # Você precisa ter o ChromeDriver instalado
    driver.get(f"https://twitter.com/search?q={query}&src=typed_query&lang=pt")
    time.sleep(30)  # Espera alguns segundos para a página carregar
    # pyautogui.hotkey('ctrl', 'shift', 'c')
    # time.sleep(5)  
    # driver.find_element(By.XPATH, 
    #                     '//*[@id="react-root"]/div/div/div/main/div/div/div/div[2]/div[2]/div/div[4]/label/div/div[2]/div/input').send_keys("joao.conceicao@sptech.school")
    # time.sleep(2)
    # driver.find_element(By.XPATH, 
    #                     '//*[@id="react-root"]/div/div/div/main/div/div/div/div[2]/div[2]/div/button[2]').click()
    # time.sleep(3)
    
    # Rolar a página para baixo para carregar mais tweets
    for _ in range(5):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
    
    # Encontrar e extrair os tweets
    tweet_divs = driver.find_elements(By.XPATH, '//div[@data-testid="cellInnerDiv"]')
    for tweet_div in tweet_divs[:num_tweets]:
        tweet_text = tweet_div.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/section/div/div/div[1]/div/div/article').text
        tweets.append(tweet_text)
    
    # Fechar o navegador
    driver.quit()
    
    return tweets

def main():
    # Palavra-chave para busca
    query = input("Digite o termo que deseja buscar no Twitter: ")

    # Número de tweets a serem coletados
    num_tweets = int(input("Quantos tweets você deseja coletar? "))

    PALAVRAS_POSITIVAS = ["saudavel", "nutritivo", "fertil", "forte", "resistente", "produtivo", "bem-cuidado",
                     "bem-alimentado", "vigoroso", "sadio", "prospero", "reprodutivo", "robusto", "fortalecido",
                     "florescente", "sustentavel", "desenvolvido", "vital", "energico", "vitalidade",
                     "crescente", "abundante", "frutifero", "prazeroso", "harmonioso", "saude", "lucrativo"]

# Palavras negativas relacionadas à criação de gado
    PALAVRAS_NEGATIVAS = ["doente", "contagioso", "parasitario", "infeccao", "mortal", "epidemia", "praga", "prejudicial",
                     "debilitado", "definhando", "contaminado", "fraco", "prejudicado", "doenca", "morto", "fracasso",
                     "perda", "desnutrido", "enfraquecido", "instavel", "destrutivo", "falencia", "estressante", "caotico"]
    # Coletar tweets
    tweets = get_tweets(query, num_tweets)
    for tweet in tweets:
        lista_tokens = tk.tokeniza(tweet)
        for token in lista_tokens:
            for p in PALAVRAS_POSITIVAS:
                token[0] = lv.did_you_mean(p,token[0])
            for p in PALAVRAS_NEGATIVAS:
                token[0] = lv.did_you_mean(p,token[0])

            
        print(f' Resultado do Tweet {tk.analisar_sentimento(tweet)}')
        
        for token in lista_tokens:
            # pegue item e tipo
            item, tipo = token

            # cri string com a descriçao
            if tipo in [tk.OPERADOR, tk.PARENTESES]:
                descricao = "'%s' : %s" %(item,op.DESCRICAO[item])
            elif tipo == tk.VARIAVEL:
                descricao = "'%s' : nome de variável" %item
            elif tipo == tk.NUMERO:
                descricao = "%f : constante float" %item
            else:
                descricao = "'%s' : categoria desconhecida" %item

            # imprima a descriçao
            print(descricao)
        # print(tweets)
        # # Exibir os tweets coletados
        # for i, tweet in enumerate(tweets):
        #     print(f"Tweet {i+1}: {tweet}")
        #     print()

if __name__ == "__main__":
    main()
