print("TED 04 - MESSIAS - QUESTÃO 2")
compras = float(input("Quantas maçãs você comprou? "))
if compras >= 12:
    print("O custo total foi ",compras * 1.00, " reais.")
elif compras < 12:
    print("O custo total foi ", compras * 1.30, " reais.")