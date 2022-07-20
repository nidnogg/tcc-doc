def SGD(funcao_otimizada, theta_ini, alpha, iter):
    # funcao_otimizada e a funcao a ser otimizada, 
    # recebe um argumento e devolve um custo e um gradiente
    # theta_ini e o ponto inicial
    # iter e o numero de iteracoes
    inicio = 0
    theta = theta_ini
    for iter in xrange(inicio + 1, iter + 1):
        _, grad = funcao_otimizada(theta)
        theta = theta - (alpha * grad)