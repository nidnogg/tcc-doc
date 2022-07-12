def shuffle_bases(payload):

    # Do payload atual, busca-se pela regex [0-9] todos os caracteres que sao numericos 
    # Estes serao os candidatos a sofrerem uma mudanca
    candidates = list(re.finditer(r'[0-9]+', payload))

    # Nao havendo números, nao ocorre mutacao
    if not candidates:
        return payload

    # A posicao de cada candidato e seu conteudo sao armazenados
    candidate_pos = random.choice(candidates).span()
    candidate = payload[candidate_pos[0]:candidate_pos[1]]

    # Uma lista de possiveis mutações a serem realizadas - todas sao conversoes 
    # entre bases binarias, octais e hexadecimais.
    replacements = [
        bin(int(candidate)),
        int(candidate),
        oct(int(candidate)),
        hex(int(candidate)),
    ]

    # Uma mutacaoo e aleatoriamente selecionada
    replacement = random.choice(replacements)

    # Se ela nao altera o candidato, nao ha mutacao
    if (str(candidate) == str(replacement)):
        return payload

    # Payload e modificado na posicao do candidato com a mutacao selecionada
    return payload[:candidate_pos[0]] + str(replacement) + payload[candidate_pos[1]:]