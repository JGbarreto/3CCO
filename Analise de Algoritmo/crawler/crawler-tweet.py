from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pyautogui

def get_tweets(query, num_tweets):
    tweets = []
    
    # Configurações do Selenium
    driver = webdriver.Chrome()  # Você precisa ter o ChromeDriver instalado
    driver.get(f"https://twitter.com/search?q={query}&src=typed_query&lang=pt")
    time.sleep(5)  # Espera alguns segundos para a página carregar
    pyautogui.click(1497,778)
    pyautogui.typewrite('joao.conceicao@sptech.school')
    print(pyautogui.position())
    time.sleep(10)  # Espera alguns segundos para a página carregar
    print(pyautogui.position())
    time.sleep(10)  # Espera alguns segundos para a página carregar
    print(pyautogui.position())
    time.sleep(10)  # Espera alguns segundos para a página carregar
    print(pyautogui.position())
    time.sleep(10)  # Espera alguns segundos para a página carregar
    print(pyautogui.position())
    
    
    # Rolar a página para baixo para carregar mais tweets
    for _ in range(5):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
    
    # Encontrar e extrair os tweets
    tweet_divs = driver.find_elements(By.XPATH, '//div[@data-testid="cellInnerDiv"]')
    for tweet_div in tweet_divs[:num_tweets]:
        tweet_text = tweet_div.find_element(By.XPATH, './/div[@lang="pt"]').text
        tweets.append(tweet_text)
    
    # Fechar o navegador
    driver.quit()
    
    return tweets

def main():
    # Palavra-chave para busca
    query = input("Digite o termo que deseja buscar no Twitter: ")

    # Número de tweets a serem coletados
    num_tweets = int(input("Quantos tweets você deseja coletar? "))

    # Coletar tweets
    tweets = get_tweets(query, num_tweets)
    print(tweets)
    # Exibir os tweets coletados
    for i, tweet in enumerate(tweets):
        print(f"Tweet {i+1}: {tweet}")
        print()

if __name__ == "__main__":
    main()
