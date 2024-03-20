import time
import datetime
import random
import mysql.connector

# Conectando ao banco de dados
conexao = mysql.connector.connect(
    host="3.95.13.190",
    user="root",
    password="root",
    database="gado",
)

# Criando um cursor
cursor = conexao.cursor()


print("iniciando simulação")


comida=1000.0
print(comida)
while(comida >0):
    if(random.randint(0,9) ==4):
        comida-=3.2
        query = f"insert into balanca (horario, qtd_comida) values ('{datetime.datetime.now()}',{comida})"
        cursor.execute(query)
        conexao.commit()
        print(comida)
    time.sleep(1)
    

print("Acabou a comida")
