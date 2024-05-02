import csv



dados = [["id_registro","data","horario"]]

nome_arquivo = "dados_sensores.csv"

with open(nome_arquivo, "w", newline="") as arquivo_csv:
    escritor = csv.writer(arquivo_csv)
    for linha in dados:
        escritor.writerow(linha)