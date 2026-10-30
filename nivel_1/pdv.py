# PDV com Descontos - Desafio Nivel 1
# Aplica desconto por idade (20% para 65+) e, depois, desconto por valor
# (10% se o valor ja descontado passar de R$ 100). Ao digitar 0 no valor,
# encerra e mostra o resumo do dia.

DESCONTO_IDADE = 0.20
IDADE_MINIMA = 65
DESCONTO_VALOR = 0.10
VALOR_MINIMO = 100

compras = []

print("=" * 40)
print("        PDV - CAIXA COM DESCONTOS")
print("=" * 40)
print("Digite 0 no valor da compra para encerrar.")

while True:
    print()

    # Valor da compra (pede de novo enquanto for negativo)
    valor = float(input("Valor da compra (R$): ").replace(",", "."))
    while valor < 0:
        print("Aviso: o valor nao pode ser negativo. Tente novamente.")
        valor = float(input("Valor da compra (R$): ").replace(",", "."))

    if valor == 0:
        break

    # Idade do cliente (pede de novo enquanto for negativa)
    idade = int(input("Idade do cliente: "))
    while idade < 0:
        print("Aviso: a idade nao pode ser negativa. Tente novamente.")
        idade = int(input("Idade do cliente: "))

    # Regra 1: desconto por idade
    valor_final = valor
    desc_idade = 0
    if idade >= IDADE_MINIMA:
        desc_idade = DESCONTO_IDADE
        valor_final = valor_final * (1 - DESCONTO_IDADE)

    # Regra 2: desconto por valor, sobre o valor ja descontado pela idade
    desc_valor = 0
    if valor_final > VALOR_MINIMO:
        desc_valor = DESCONTO_VALOR
        valor_final = valor_final * (1 - DESCONTO_VALOR)

    valor_final = round(valor_final, 2)

    compras.append({
        "valor": valor,
        "idade": idade,
        "desc_idade": desc_idade,
        "desc_valor": desc_valor,
        "final": valor_final,
    })

    print(f"Desconto por idade: {desc_idade * 100:.0f}%")
    print(f"Desconto por valor: {desc_valor * 100:.0f}%")
    print(f"Valor final: R$ {valor_final:.2f}")

# Resumo do dia
total_bruto = 0
total_final = 0
for compra in compras:
    total_bruto = total_bruto + compra["valor"]
    total_final = total_final + compra["final"]
total_descontos = total_bruto - total_final

linhas = []
linhas.append("=" * 40)
linhas.append("            RESUMO DO DIA")
linhas.append("=" * 40)
numero = 1
for compra in compras:
    linhas.append(f"Compra {numero}: R$ {compra['valor']:.2f} -> R$ {compra['final']:.2f}")
    numero = numero + 1
linhas.append("-" * 40)
linhas.append(f"Compras registradas: {len(compras)}")
linhas.append(f"Total bruto:         R$ {total_bruto:.2f}")
linhas.append(f"Total de descontos:  R$ {total_descontos:.2f}")
linhas.append(f"Total final:         R$ {total_final:.2f}")
linhas.append("=" * 40)

print()
for linha in linhas:
    print(linha)

# Bonus 3: salva o resumo em resumo.txt
arquivo = open("resumo.txt", "w", encoding="utf-8")
for linha in linhas:
    arquivo.write(linha + "\n")
arquivo.close()
print("Resumo salvo em resumo.txt")
