import time
import random
import mysql.connector
import datetime

config = {
    'user': 'root',
    'password': 'root',
    'host': 'localhost',
    'database': 'gado',
    'port': '3306',
}
connection = mysql.connector.connect(**config)
cursor = connection.cursor()
numero_ant = 0
while(True):
    state = 'segura'
    numero = random.randint(numero_ant,numero_ant+100)
    if(numero > 600):
        state='perigosa'
        if random.random() < 0.2:
            numero=random.randint(200,600)
            state='segura'
    numero_ant=numero    
    cursor.execute(f'INSERT INTO tds_sensor VALUES (null, "{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",{numero})')
    connection.commit()
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    print(f'a água está com o valor de TDS de {numero}/L, {state} para o consumo')
    time.sleep(5)