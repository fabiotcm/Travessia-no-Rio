from movimentacao import mover_personagens
from estado_jogo import exibir_estado_jogo


lado_esquerdo = ["Mãe", "Pai", "Filha1", "Filho1", "Filha2", "Filho2", "Policial", "Prisioneiro"]
lado_direito = []
barco_lado_esquerdo = True  # Qual lado está o barco
historico = []  # Pilha

while True:
    exibir_estado_jogo(lado_esquerdo, lado_direito, barco_lado_esquerdo)

    if not lado_esquerdo:
        print("Parabéns! Você venceu!")
        contador = 1
        for passo in historico:
            print(f"{contador}° passo: {passo}")
            contador += 1
        break

    personagem1 = input("Qual primeiro personagem vai atravessar?: ")
    personagem2 = input("Qual segundo personagem vai atravessar?: ")

    if personagem1 == "" and personagem2 == "":
        print("Você precisa escolher pelo menos um personagem.")
        continue

    if personagem1 == personagem2:
        print("Você não pode escolher o mesmo personagem duas vezes")
        continue

    movimentacao_barco = mover_personagens(personagem1, personagem2, lado_esquerdo, lado_direito, barco_lado_esquerdo,
                                           historico)

    if movimentacao_barco:
        print(movimentacao_barco)
        continue

    barco_lado_esquerdo = not barco_lado_esquerdo
