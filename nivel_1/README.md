# PDV com Descontos (Desafio Nível 1)

## O que o código faz

Este programa simula o caixa de uma loja (PDV, Ponto de Venda). Para cada compra, ele recebe o valor e a idade do cliente, aplica descontos progressivos conforme as regras de negócio e mostra o valor final em reais. Ele aceita várias compras seguidas e, quando o caixa é fechado, mostra um resumo do dia com a quantidade de compras, o total bruto, o total de descontos e o total final.

## Como ele faz

1. Mostra o cabeçalho do caixa e entra em um loop (`while True`).
2. Pede o valor da compra. Se for negativo, mostra um aviso e pede de novo. Se for `0`, sai do loop.
3. Pede a idade do cliente. Se for negativa, mostra um aviso e pede de novo.
4. **Regra 1:** se a idade for maior ou igual a 65, aplica 20% de desconto.
5. **Regra 2:** se o valor **já descontado pela idade** for maior que R$ 100, aplica mais 10% sobre esse valor.
6. Arredonda o resultado para duas casas decimais e mostra os descontos e o valor final (ex.: `R$ 144.00`).
7. Guarda a compra numa lista com `.append()`.
8. Ao encerrar, percorre a lista com `for`, soma o total bruto e o total final, calcula o total de descontos (bruto menos final) e mostra o resumo do dia.
9. **Bônus:** grava o mesmo resumo no arquivo `resumo.txt` usando `open(..., "w")`.

## Como rodar

```bash
python pdv.py
```

(No macOS/Linux pode ser `python3 pdv.py`.)

## Tabela de exemplos (casos de teste)

| # | Valor (R$) | Idade | Desconto idade | Desconto valor | Valor final esperado |
|---|---|---|---|---|---|
| 1 | 50.00 | 30 | 0% | 0% | R$ 50.00 |
| 2 | 100.00 | 30 | 0% | 0% | R$ 100.00 |
| 3 | 80.00 | 65 | 20% | 0% | R$ 64.00 |
| 4 | 100.00 | 70 | 20% | 0% | R$ 80.00 |
| 5 | 125.00 | 70 | 20% | 0% | R$ 100.00 |
| 6 | 200.00 | 30 | 0% | 10% | R$ 180.00 |
| 7 | 101.00 | 30 | 0% | 10% | R$ 90.90 |
| 8 | 200.00 | 65 | 20% | 10% | R$ 144.00 |
| 9 | 1000.00 | 80 | 20% | 10% | R$ 720.00 |
| 10 | 200.00 | 64 | 0% | 10% | R$ 180.00 |

### Casos-limite

- **Caso 5:** 125 × 0,8 = 100. Como 100 não é **maior** que 100, os 10% não se aplicam.
- **Caso 10:** idade 64 não ganha desconto por idade, só o de valor.
- **Caso 7:** 101 × 0,9 = 90,90. O valor é arredondado para duas casas decimais.
