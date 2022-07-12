def shuffle_integers(payload):

    # Numeros sao selecionados pela regex como candidatos para mutação
    candidates = list(re.finditer(r'[0-9]', payload))

    if not candidates:
        return payload

    # Um e aleatoriamente escolhido e sua posicaoo armazenada
    candidate_pos = random.choice(candidates).span()

    # Um inteiro aleatorio entre 0 e 9 e selecionado para substitui-lo
    return payload[:candidate_pos[0]] + str(random.choice(range(10))) + payload[candidate_pos[1]:]