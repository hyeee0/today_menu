# 단어를 벡터화 해주는 작업

import pandas as pd
from gensim.models import Word2Vec

review_word = pd.read_csv('./crawling_data/clean_menu_recipes_01-25_8.csv')
review_word.info()

clean_menu_recipes = list(review_word['clean_menu_recipes'])
cleaned_tokens = []

for recipe in clean_menu_recipes:
    token = recipe.split()
    cleaned_tokens.append(token)

# Word2Vec 단어를 벡터화 해주는 모델
embedding_model = Word2Vec(cleaned_tokens, vector_size=3,
                           window=4, min_count=2,
                           workers=8, epochs=100, sg=1)
# vector_size=100 -> 차원을 100개만 허용
# window=4 -> 4단어씩 잘라서 유사한 단어로 묶는다
# min_count=20 -> 최소 20번은 학습된 것만 사용
# workers=8 -> CPU 8개 사용
# sg=1 [skip gram] -> 학습 알고리즘 (cbow [Continuous Bag Of Word]또는 sg)
# [skip gram] 하나의 단어에서 여러 단어를 예측하는 방법이다. 즉 중심단어에서 주변단어를 예측하는 방식인데 CBOW보다 성능이 좋아 더 많이 쓰인다
embedding_model.save('./models/word2vec_menu_recipes_window=4_vector_size=3_8.model')
print(embedding_model.wv.index_to_key)
print(len(embedding_model.wv.index_to_key))