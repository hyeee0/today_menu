import re
from konlpy.tag import Okt
import pandas as pd
from sklearn.metrics.pairwise import linear_kernel
from scipy.io import mmread
import pickle
from gensim.models import Word2Vec

def getRecommendation(cosin_sim):
    simScore = list(enumerate(cosin_sim[-1])) #
    simScore = sorted(simScore, key=lambda x:x[1], reverse=True)
    simScore = simScore[:5] # 11개를 추출해준다 / 왜냐면 10개를 추천해줄텐데 첫번째는 자기자신이기에 나중에 빼주기 위해
    movie_idx = [i[0] for i in simScore] #
    recMovieList = df_menu_recipes.iloc[movie_idx, 0] # 0번 컬럼은 타이틀만 인덱싱
    return recMovieList

df_menu_recipes = pd.read_csv('./crawling_data/clean_menu_recipes_01-25_8.csv')
tfidf_matrix = mmread('./models/tfidf_menu_recipes_review.mtx').tocsr()
with open('./models/tfidf.pickle', 'rb') as f:
    tfidf = pickle.load(f)

# 메뉴명 이용
# recipe_idx = df_menu_recipes[df_menu_recipes['menu_titles']=='두부 장조림'].index[0] # '' 안에 영화의 인덱스를 찾아준다
# cosin_sim = linear_kernel(tfidf_matrix[recipe_idx], tfidf_matrix) # 두 벡터 사이의 각도가 1일수록 유사도가 높다(코사인심 -> 코사인 유사도)
# recommendation = getRecommendation(cosin_sim)
# print(recommendation[1:4]) # 0번 제외하고(0번은 자기자신) 1부터 10번까지

# key_word 이용
embedding_model = Word2Vec.load('./models/word2vec_menu_recipes_window=4_vector_size=3_4.model')
key_word = '돈가스'
sim_word = embedding_model.wv.most_similar(key_word, topn=10)
words = [key_word]
for word, _ in sim_word:
    words.append(word)
print(words)

sentence = []
count = 11

for word in words:
    sentence = sentence + [word] * count
    count -= 1
sentence = ' '.join(sentence)
sentence_vec = tfidf.transform([sentence])
cosin_sim = linear_kernel(sentence_vec, tfidf_matrix)
recommendation = getRecommendation(cosin_sim)
print(recommendation)

# 문장을 이용
# sentence = '쌀쌀한 날씨에 어울리는 음식'
# review = re.sub('[^가-힣 ]', ' ', sentence)
# okt = Okt()
# token = okt.pos(review, stem=True)
# df_token = pd.DataFrame(token, columns=['word', 'class'])
# # df_token = df_token[(df_token['class'] == 'Noun') |
# #                     (df_token['class'] == 'Verb') |
# #                     (df_token['class'] == 'Adjective')]
# words = []
# for word in df_token.word:
#     if len(word) > 1:  # 단어길이가 1보다 크고 -> 2글자 이상
#         words.append(word)  # 리스트에 추가해준다
# cleaned_sentence = ' '.join(words)  # 포함시키지 않은 단어는 공백으로 만든다.
# print(cleaned_sentence)
# sentence_vec = tfidf.transform([cleaned_sentence])
# cosin_sim = linear_kernel(sentence_vec, tfidf_matrix)
# recommendation = getRecommendation(cosin_sim)
# print(recommendation)
