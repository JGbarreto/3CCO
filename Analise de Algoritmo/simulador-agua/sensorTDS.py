import time
import random
import mysql.connector
import datetime
from azure.iot.device import IoTHubDeviceClient, Message

# config = {
#     'user': 'root',
#     'password': 'toor',
#     'host': 'localhost',
#     'database': 'sensores',
#     'port': '3306',
# }
conn_str = "HostName=hub-g2.azure-devices.net;DeviceId=tds-sensor;SharedAccessKey=ZMrvYHdAIyPJ0W2ghOKXaZMH0GoeetMwPAIoTP7qSb4="
client = IoTHubDeviceClient.create_from_connection_string(conn_str)

# connection = mysql.connector.connect(**config)
# cursor = connection.cursor()
numero_ant = 50
contador = 0
dia = 1
mes = 3
ano = 2024
dia_str = f'0{dia}'
mes_str = f'0{mes}'
while(True):
    if contador >=7:
        contador=0
        numero_ant=0
        print("Limpeza")
    state = 'segura'
    numero = random.randint(numero_ant,numero_ant+100)
    if(numero > 600):
        state='perigosa'
        if random.random() < 0.2:
            numero=random.randint(200,600)
            state='segura'
    numero_ant=numero    
    # cursor.execute(f'INSERT INTO tds_sensor VALUES (null, "{ano}-{mes_str if mes<10 else mes}-{dia_str if dia<10 else dia}",{numero})')
    # connection.commit()
    # rows = cursor.fetchall()
    client.send_message(numero)
    print(f'a água está com o valor de TDS de {numero}mg/L, {state} para o consumo')
    
    contador +=1
    dia+=1
    if dia >30:
        dia =1
        mes+=1
    if mes >12:
        mes =1
        ano+=1
    dia_str = f'0{dia}'
    mes_str = f'0{mes}'
    time.sleep(5)