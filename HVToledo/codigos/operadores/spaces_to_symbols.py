def spaces_to_symbols(payload):

    # Caracteres alfanumericos com excecao de espacos sao excluidos
    excluded_characters = '[^a-zA-Z0-9]'

    # Regex para tal
    r = re.compile(excluded_characters)

    # Lista de simbolos a serem considerados para substituirem espacos
    symbols_to_try = []

    # Sao adicionados sinais de pontuacao
    for symbol in string.punctuation:
        symbols_to_try.append(symbol)

    
    symbols_to_try = list(filter(r.match, symbols_to_try))

    # Espacos serao trocados por symbols_to_try
    symbols = {" ": symbols_to_try}

    # Funcao filter_candidates filtra payload para encontrar espacos
    symbols_in_payload = filter_candidates(symbols, payload)

    # Sem espacos nao ha mutacao
    if not symbols_in_payload:
            return payload

    # Aleatoriamente escolhe um espaco para ser substituido
    candidate_symbol = random.choice(symbols_in_payload)
    # Checa por possiveis trocas
    replacements = symbols[candidate_symbol]
    # Escolhe uma troca aleatoriamente
    candidate_replacement = random.choice(replacements)

    # Aplica mutacao na posicao, via funcao do wafamole replace_random que realiza a troca
    # em payload de candidate_symbol (espaco) por seu substituto, candidate_replacement
    return replace_random(payload, candidate_symbol, candidate_replacement)
