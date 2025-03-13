def piloto_no_barco(barco):
    pilotos = ["Pai", "Mãe", "Policial"]
    for pessoa in barco:
        if pessoa in pilotos:
            return True
    return False


def mae_sozinha_com_filhos(lado):
    if "Mãe" in lado and "Pai" not in lado:
        if "Filho1" in lado or "Filho2" in lado:
            return True
    return False


def pai_sozinho_com_filhas(lado):
    if "Pai" in lado and "Mãe" not in lado:
        if "Filha1" in lado or "Filha2" in lado:
            return True
    return False


def prisioneiro_sozinho_sem_policial(lado):
    if "Prisioneiro" in lado and "Policial" not in lado:
        if len(lado) >= 2:
            return True
    return False


def limite_pessoas_barco(barco):
    return len(barco) > 2
