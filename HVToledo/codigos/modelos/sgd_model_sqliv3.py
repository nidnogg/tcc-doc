# Stochastic Gradient Descent Classifier
pipe = make_pipeline(
    TfidfVectorizer(input = 'content', lowercase = True, analyzer = 'char', max_features = 1024, ngram_range = (1, 2)), 
    # Nota-se a funcao modified_huber de perda, requerida para fazer uso da predict_proba() no wafamole++
    # e de fato usar o modelo no mesmo
    SGDClassifier(loss="modified_huber", penalty="l2", max_iter=500))
