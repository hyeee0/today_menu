import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import collections
from matplotlib import font_manager, rc
from PIL import Image
import matplotlib as mpl

# 한글을 쓰기위한 폰트를 불러오는 작업
font_path = './malgun.ttf'
font_name = font_manager.FontProperties(fname=font_path).get_name()
mpl.rcParams['axes.unicode_minus']=False
rc('font', family=font_name)

df = pd.read_csv('./crawling_data/clean_menu_recipes_01-25_8.csv')
words = df[df['menu_titles']=='묵은지 참치김밥']['clean_menu_recipes']
print(words.iloc[0])
words = words.iloc[0].split()
print(words)

worddict = collections.Counter(words)
worddict = dict(worddict)
print(worddict)

# 키워드를 시각화 해주는 작업
# 단어의 빈도가 높으면 시각화 되는 단어의 크기가 크다 -> 두 영화의 단어를 비교하면서 왜 추천됐는지 확인해보자
wordcloud_img = WordCloud(background_color='white', max_words=2000,
                          font_path=font_path).generate_from_frequencies(worddict)
plt.figure(figsize=(12, 12))
plt.imshow(wordcloud_img)
plt.axis('off')

words = df[df['menu_titles']=='생와사비 참치마요김밥']['clean_menu_recipes']
words = words.iloc[0].split()
worddict = collections.Counter(words)
worddict = dict(worddict)
wordcloud_img = WordCloud(background_color='white', max_words=2000,
                          font_path=font_path).generate_from_frequencies(worddict)
plt.figure(figsize=(12, 12))
plt.imshow(wordcloud_img)
plt.axis('off')
plt.show()