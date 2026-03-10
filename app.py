from datetime import datetime, timedelta

nome = input("Digite o nome do profissional: ")
data_inicio = input("Digite a data do primeiro plantão (AAAA-MM-DD): ")

data = datetime.strptime(data_inicio, "%Y-%m-%d")

print(f"\nEscala de plantão de {nome}:\n")

for i in range(10):
    print(data.strftime("%d/%m/%Y"))
    data += timedelta(days=2)
