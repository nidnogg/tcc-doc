# Support Vector Classification
pipe = make_pipeline(
    # Vetorizador Tfidf para trabalhar com numpy arrays compatíveis com o dataset, com parametros otimizados via paramgrid
    TfidfVectorizer(input = 'content', lowercase = True, analyzer = 'char', max_features = 1024, ngram_range = (1, 2)), 
    # Classe do Classificador Support Vector Machine e seus parametros finais otimizados. 
    # Nota-se o parametro probability=true, essencial para o modelo funcionar no wafamole++ fazendo uso da funcao predict_proba().
    SVC(C = 10, kernel = 'rbf', probability=True, gamma='scale'))

# Variaveis trainX e trainY estao devidamente documentadas nos notebooks.
print(pipe.fit(trainX, trainY))
