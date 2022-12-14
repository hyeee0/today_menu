import pandas as pd
from konlpy.tag import Okt
import re

df = pd.read_csv('./crawling_data/menu_recipes_01-25_1.csv')
df.info()
print(df.head())

df_stopwords = pd.read_csv('./stopwords.csv', index_col=0)
stopwords = list(df_stopwords['stopword'])

okt = Okt()
df['clean_menu_recipes'] = None
count = 0
for idx, menu_recipe in enumerate(df.menu_recipes):
    count += 1
    if count % 10 == 0:
        print('.', end='')
    if count % 1000 == 0:
        print()
    menu_recipe = re.sub('[^가-힣 ]', ' ', menu_recipe)
    df.loc[idx, 'clean_menu_recipes'] = menu_recipe
    token = okt.pos(menu_recipe, stem=True)
    # okt.pos를 사용하면 단어의 품사를 알 수 있고 'Verb', 'Noun', 'Josa' 등으로 출력되어 원하는 쓰임새만 추출할 수 있다
    # stem=True 원형으로 변경해준다 -> 차원을 축소해준다
    # 우리가 사용하는 품사는 'Verb', 'Noun', 'Adjective' / 동사, 명사, 형용사
    df_token = pd.DataFrame(token, columns=['word', 'class']) # 데이터 프레임으로 만들어주자
    # df_token = df_token[(df_token['class']=='Noun') |
    #                     (df_token['class']=='Verb') |
    #                     (df_token['class']=='Adjective')]

    words = [] # 여기부터 불용어 제거하는 과정
    for word in df_token.word:
        if len(word) > 0: # 단어길이가 1보다 크고 -> 2글자 이상
            if word not in list(df_stopwords.stopword): # stopwords파일에 포함하지 않는 단어일때만
                words.append(word) #리스트에 추가해준다
    cleaned_menu_recipes = ' '.join(words) #포함시키지 않은 단어는 공백으로 만든다.
    df.loc[idx, 'clean_menu_recipes'] = cleaned_menu_recipes
print(df.head(30))
df.dropna(inplace=True)
df.to_csv('./crawling_data/clean_menu_recipes_01-25_8.csv', index=False)