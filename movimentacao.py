from validacao_regras import validar_regras


def mover_personagens(personagem1, personagem2, lado_esquerdo, lado_direito, barco_lado_esquerdo, historico):
    barco = []
    if personagem1:
        barco.append(personagem1)
    if personagem2:
        barco.append(personagem2)

    if barco_lado_esquerdo:
        for pessoa in barco:
            if pessoa not in lado_esquerdo:
                return "Personagem não está no lado correto. Escolha um personagem do lado esquerdo!"
        for pessoa in barco:
            lado_esquerdo.remove(pessoa)
            lado_direito.append(pessoa)
        passo = f"{personagem1} e {personagem2} para a direita"
        historico.append(passo)
    else:
        for pessoa in barco:
            if pessoa not in lado_direito:
                return "Personagem não está no lado correto. Escolha um personagem do lado direito!"
        for pessoa in barco:
            lado_direito.remove(pessoa)
            lado_esquerdo.append(pessoa)
        passo = f"{personagem1} e {personagem2} para a esquerda"
        historico.append(passo)

    validacao = validar_regras(lado_esquerdo, lado_direito, barco)
    if validacao:
        historico.pop()
        if barco_lado_esquerdo:
            for pessoa in barco:
                lado_direito.remove(pessoa)
                lado_esquerdo.append(pessoa)
        else:
            for pessoa in barco:
                lado_esquerdo.remove(pessoa)
                lado_direito.append(pessoa)
        return validacao

    return None
