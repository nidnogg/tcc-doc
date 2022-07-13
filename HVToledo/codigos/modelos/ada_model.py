# Ada Boost Classifier
pipe = make_pipeline(
    TfidfVectorizer(input = 'content', lowercase = True, analyzer = 'char', max_features = 1024, ngram_range = (1, 2)), 
    # O classificador AdaBoost foi otimizado com esses parametros, e nenhum parametro extra 
    # e requerido para uso da funcao predict_proba()
    AdaBoostClassifier(n_estimators=100, random_state=0))

# a seguinte funcao encapsula o treinamento no backend de paralelizacao ray,
# consideravelmente reduzindo o tempo de execucao. Tambem utilizado no modelo SGD
register_ray()
with joblib.parallel_backend('ray'):
  pipe.fit(trainX, trainY)
  pipe.score(testX, testY)
  joblib.dump(pipe, 'drive/My Drive/@tcc/test_qda_classifier.dump')
