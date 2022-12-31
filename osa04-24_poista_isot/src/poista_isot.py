# tee ratkaisu tänne
def poista_isot(mjono:list):
    lista = []
    for sana in mjono:
        pienet = sana.isupper()
        if pienet == False:
            lista.append(sana)

    return lista


if __name__ == "__main__":
    lista = ["ABC", "def", "ISO", "TOINENISO", "pieni", "toinen pieni", "Osittain Iso"]
    karsittu_lista = poista_isot(lista)
    print(karsittu_lista)