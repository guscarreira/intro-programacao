print("Atividade de sala - Messias | Questão 6")
qtd_atual = int(input("Diga a quantidade atual de seu estoque: "))
qtd_maxima = int(input("Diga a quantidade máxima de seu estoque: "))
qtd_minima = int(input("Diga a quantidade mínima de seu estoque: "))
qtd_media = (qtd_maxima + qtd_minima) // 2
if qtd_atual >= qtd_media:
    print("Não efetuar compra.")
else:
    print("Efetuar compra.")