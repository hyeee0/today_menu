# TF-IDF(Term Frequency - Inverse Document Frequency)
# 정보 검색과 텍스트 마이닝에서 이용하는 가중치로, 여러 문서로 이루어진 문서군이 있을 때
# 어떤 단어가 특정 문서 내에서 얼마나 중요한 것인지를 나타내는 통계적 수치이다.
# 문서의 핵심어를 추출하거나, 검색 엔진에서 검색 결과의 순위를 결정하거나, 문서들 사이의 비슷한 정도를 구하는 등의 용도로 사용할 수 있다.
import pickle
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from scipy.io import mmwrite, mmread

df_menu_recipes = pd.read_csv('./crawling_data/clean_menu_recipes_01-25_8.csv')
df_menu_recipes.info()

tfidf = TfidfVectorizer()
tfidf_matrix = tfidf.fit_transform(df_menu_recipes['clean_menu_recipes'])
print(tfidf_matrix[0].shape)
with open('./models/tfidf.pickle', 'wb') as f: # 저장은 wb -> write
    pickle.dump(tfidf, f)
mmwrite('./models/tfidf_menu_recipes_review.mtx', tfidf_matrix)