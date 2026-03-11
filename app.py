from datetime import datetime
import calendar

nome_escala = input("Nome da escala/setor: ")
responsavel = input("Nome do enfermeiro responsável: ")
autor = input("Quem elaborou a escala: ")

tipo = input("Plantão PAR ou IMPAR: ").lower()
turno = input("Turno (DIA ou NOITE): ").upper()

hoje = datetime.today()
ano = hoje.year
mes = hoje.month
dias_mes = calendar.monthrange(ano, mes)[1]

qtd = int(input("Quantos funcionários na escala? "))

funcionarios = []
i = 0

while i < qtd:

    print(f"\nCadastro do funcionário {i+1}")

    nome = input("Nome: ")
    folga1 = int(input("Primeira folga extra (dia): "))
    folga2 = int(input("Segunda folga extra (dia): "))

    print("\nConfirmar dados?")
    print("C - Confirmar")
    print("R - Refazer")
    print("V - Voltar funcionário anterior")

    opcao = input("Escolha: ").lower()

    if opcao == "c":

        funcionarios.append({
            "nome": nome,
            "folga1": folga1,
            "folga2": folga2
        })

        i += 1

    elif opcao == "v":

        if funcionarios:
            funcionarios.pop()
            i -= 1
            print("Voltando para o funcionário anterior...")
        else:
            print("Não há funcionário anterior.")

    elif opcao == "r":

        print("Refazendo cadastro...")

    else:
        print("Opção inválida")

print("\n")

print(f"ESCALA: {nome_escala} | TURNO: {turno}")
print(f"Responsável: {responsavel}")
print(f"Mês: {mes}/{ano}\n")

cabecalho = "Nome".ljust(12)

for dia in range(1, dias_mes+1):
    cabecalho += f"{dia:02d}".rjust(3)

print(cabecalho)
print("-"*len(cabecalho))

for func in funcionarios:

    linha = func["nome"].ljust(12)

    for dia in range(1, dias_mes+1):

        if dia == func["folga1"] or dia == func["folga2"]:
            status = "F"

        else:

            if tipo == "par":
                status = "P" if dia % 2 == 0 else "F"
            else:
                status = "P" if dia % 2 != 0 else "F"

        linha += status.rjust(3)

    print(linha)

print("\nLegenda:")
print("P = Plantão")
print("F = Folga 12x36")
print("F = Folga")

data = hoje.strftime("%d/%m/%Y")

print(f"\nEscala elaborada por: {autor}")
print(f"Data: {data}")
print("\nAssinatura: ______________________________")
