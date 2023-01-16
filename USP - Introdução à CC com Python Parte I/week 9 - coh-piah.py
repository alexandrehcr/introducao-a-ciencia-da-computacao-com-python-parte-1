import re


def le_assinatura():
    """Lê os valores dos traços linguísticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos"""
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("\nInforme a assinatura típica de um aluno infectado: ")

    wal = float(input("Entre o tamanho médio de palavra: "))
    ttr = float(input("Entre a relação Type-Token: "))
    hlr = float(input("Entre a Razão Hapax Legomana: "))
    sal = float(input("Entre o tamanho médio de sentença: "))
    sac = float(input("Entre a complexidade média da sentença: "))
    pal = float(input("Entre o tamanho medio de frase: "))

    return [wal, ttr, hlr, sal, sac, pal]


def le_textos():
    """Lê todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento"""
    i = 1
    textos = []
    texto = input("\nDigite o texto " + str(i) + " (aperte enter para sair): ")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("\nDigite o texto " + str(i) +
                      " (aperte enter para sair): ")

    return textos


def separa_sentencas(texto):
    """Recebe um texto e devolve uma lista das sentenças dentro do texto"""
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas


def separa_frases(sentenca):
    """Recebe uma sentenca e devolve uma lista das frases dentro da sentenca"""
    return re.split(r'[,:;]+', sentenca)


def separa_palavras(frase):
    """Recebe uma frase e devolve uma lista das palavras dentro da frase"""
    return frase.split()


def n_palavras_unicas(lista_palavras):
    """Recebe uma lista de palavras e devolve o número de palavras que aparecem uma única vez"""
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas


def n_palavras_diferentes(lista_palavras):
    """Recebe uma lista de palavras e devolve o número de palavras diferentes utilizadas"""
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)


def compara_assinatura(as_a, as_b):
    """Recebe duas assinaturas de texto e retorna o grau de similaridade nas assinaturas."""
    # Sab = (∑ [i = 1, 6] || (as_a - as_b)) || / 6
    S = 0  # Grau de similaridade
    for i in range(0, 6):
        S += abs(as_a[i] - as_b[i]) / 6
    return S


def n_total_palavras(texto):
    """ Recebe um texto e retorna o número total de palavras"""
    n_total_palavras = 0
    sentencas = separa_sentencas(texto)
    for sentenca in sentencas:
        frases = separa_frases(sentenca)
        for frase in frases:
            palavras = separa_palavras(frase)
            for palavra in palavras:
                n_total_palavras += 1

    return n_total_palavras


def soma_tamanho_palavras(texto):
    soma_tamanho_palavras = 0
    sentencas = separa_sentencas(texto)
    for sentenca in sentencas:
        frases = separa_frases(sentenca)
        for frase in frases:
            palavras = separa_palavras(frase)
            for palavra in palavras:
                soma_tamanho_palavras += len(palavra)

    return soma_tamanho_palavras


def tamanho_medio_palavras(texto):
    """Recebe um texto e retorna a soma dos tamanhos das palavras dividida pelo número total de palavras"""
    return soma_tamanho_palavras(texto) / n_total_palavras(texto)


def type_token(texto):
    """Relação Type-Token é o número de palavras diferentes dividido pelo número total de palavras"""
    palavras_diferentes = 0
    palavras = []
    sentencas = separa_sentencas(texto)
    for sentenca in sentencas:
        frases = separa_frases(sentenca)
        for frase in frases:
            palavras += separa_palavras(frase)

    palavras_diferentes += n_palavras_diferentes(palavras)
    return palavras_diferentes / n_total_palavras(texto)


def hapax_legomana(texto):
    """Número de palavras utilizadas uma única vez dividido pelo número total de palavras"""
    palavras = []
    palavras_unicas = 0
    sentencas = separa_sentencas(texto)
    for sentenca in sentencas:
        frases = separa_frases(sentenca)
        for frase in frases:
            palavras += separa_palavras(frase)

    palavras_unicas += n_palavras_unicas(palavras)
    return palavras_unicas / n_total_palavras(texto)


def tamanho_medio_sentenca(texto):
    """Recebe um texto e retorna a soma dos números de caracteres em todas as sentenças dividida pelo número de sentenças"""
    n_caracteres = 0

    sentencas = separa_sentencas(texto)
    n_sentencas = len(sentencas)
    for sentenca in sentencas:
        n_caracteres += len(sentenca)

    return n_caracteres / n_sentencas


def complexidade_sentenca(texto):
    """Recebe um texto e retorna o número total de frases divido pelo número de sentenças"""
    n_sentencas = 0
    n_frases = 0
    sentencas = separa_sentencas(texto)
    n_sentencas = len(sentencas)
    for sentenca in sentencas:
        frases = separa_frases(sentenca)
        for frase in frases:
            n_frases += 1

    return n_frases / n_sentencas


def tamanho_medio_frase(texto):
    """Recebe um texto e retorna a soma do número de caracteres em cada frase dividida pelo número de frases no texto"""
    n_caracteres = 0
    n_frases = 0
    sentencas = separa_sentencas(texto)
    for sentenca in sentencas:
        frases = separa_frases(sentenca)
        n_frases += len(frases)
        for frase in frases:
            n_caracteres += len(frase)

    return n_caracteres / n_frases


def calcula_assinatura(texto):
    """Essa função recebe um texto e retorna a assinatura do texto"""
    palavra_tamanho_medio = tamanho_medio_palavras(texto)
    relacao_type_token = type_token(texto)
    relacao_hapax = hapax_legomana(texto)
    sentenca_tamanho_medio = tamanho_medio_sentenca(texto)
    complexidade = complexidade_sentenca(texto)
    frase_tamanho_medio = tamanho_medio_frase(texto)

    assinatura = [palavra_tamanho_medio, relacao_type_token, relacao_hapax,
                  sentenca_tamanho_medio, complexidade, frase_tamanho_medio]

    return assinatura


def avalia_textos(textos, ass_cp):
    """Recebe uma lista de textos e uma assinatura ass_cp e retorna o número (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH"""
    assinaturas = []
    for texto in textos:
        assinaturas.append(calcula_assinatura(texto))

    maior_similaridade = compara_assinatura(assinaturas[0], ass_cp)
    n_texto_infectado = 1
    for i in range(len(assinaturas)):
        grau_similaridade = compara_assinatura(assinaturas[i], ass_cp)
        if grau_similaridade < maior_similaridade:
            maior_similaridade = grau_similaridade
            n_texto_infectado = i + 1

    return n_texto_infectado


def main():
    ass_cp = le_assinatura()
    textos = le_textos()
    infectado = avalia_textos(textos, ass_cp)

    print(f"\nO autor do texto {infectado} está infectado com COH-PIAH")


main()
