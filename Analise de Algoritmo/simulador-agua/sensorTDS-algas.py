import time
import random
import mysql.connector
import datetime
import csv
#trocar por config do s3
config = {
    'user': 'root',
    'password': 'toor',
    'host': 'localhost',
    'database': 'sensores',
    'port': '3306',
}

numero_ant = 50
contador = 0
start = 10
step = 100
nome_arquivo = 'resultados_tds.csv'
with open(nome_arquivo, mode='w', newline='') as arquivo_csv:
  escritor_csv = csv.writer(arquivo_csv, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

for i in range(0,10,1):
    for i in range(start,10*start, step):
        # if contador >=7:
        #     contador=0
        #     numero_ant=0
        #     print("Limpeza")

        numero = random.randint(numero_ant,numero_ant+100)
        if(numero > 600):
            state='perigosa'
            if random.random() < 0.2:
                numero=random.randint(200,600)
                state='segura'
        numero_ant=numero    
        escritor_csv.writerow([id, datetime.datetime.now(), ])
        # print(f'a água está com o valor de TDS de {numero}mg/L, {state} para o consumo')
        time.sleep(5)
        contador +=1
        step+= 2 * start
    start *=random.randint(2,10)