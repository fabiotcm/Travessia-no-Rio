from condicionais_logicas import *


def validar_regras(lado_esquerdo, lado_direito, barco):

    if not piloto_no_barco(barco):
        return "O barco está sem piloto."

    if mae_sozinha_com_filhos(lado_esquerdo):
        return "A Mãe não pode ficar sozinha com os filhos."
    if mae_sozinha_com_filhos(lado_direito):
        return "A Mãe não pode ficar sozinha com os filhos."

    if pai_sozinho_com_filhas(lado_esquerdo):
        return "O Pai não pode ficar sozinho com as filhas."
    if pai_sozinho_com_filhas(lado_direito):
        return "O Pai não pode ficar sozinho com as filhas."

    if prisioneiro_sozinho_sem_policial(lado_esquerdo):
        return "O prisioneiro não pode ficar sozinho com nenhum integrante da família sem o policial."
    if prisioneiro_sozinho_sem_policial(lado_direito):
        return "O Prisioneiro não pode ficar sozinho com nenhum integrante da família sem o policial."

    if limite_pessoas_barco(barco):
        return "O barco só pode transportar no máximo duas pessoas por viagem."

    return None
