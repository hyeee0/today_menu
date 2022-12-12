import re
import pandas as pd
import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException

# category = []
pages = [13, 9, 5, 16, 7, 6, 7, 9, 9, 4, 8, 5, 7, 6, 3, 16, 4, 14, 5, 5, 9, 4, 2, 3, 9]

options = webdriver.ChromeOptions()
options.add_argument('lang=kr_KR')
driver = webdriver.Chrome('./chromedriver', options=options)
df_title = pd.DataFrame()

for i in range(1, 26): # 1페이지 부터 25페이지
    for j in range(1, pages[i-1]):
        url = 'https://2bob.co.kr/recipe.php?id=list&fKeyList=&fKeyValue=&eTheme={}&OrderCondition=&OrderBy=&page={}'.format(i,j)

        menu_titles = []
        menu_recipes = []
        # summary = []
        driver.get(url)
        for k in range(1, 21):
            menu_xpath1 = '//*[@id="con_wrapper"]/div[5]/div[2]/div[2]/ul/li[{}]/a/div[2]/p[2]'.format(k)  # 음식명
            menu_title = driver.find_element('xpath', menu_xpath1).text # 음식명 텍스트로 저장
            driver.find_element('xpath', menu_xpath1).click() # 음식명 클릭해서 상세페이지 들어감
            time.sleep(0.1)

            menu_xpath2 = '//*[@id="con_wrapper"]/div[5]/div[2]/div[2]/div[2]'
            menu_recipe = driver.find_element('xpath', menu_xpath2).text # 음식명 텍스트로 저장
            #print(menu_recipe)
            driver.back()
            menu_titles.append(menu_title)
            menu_recipes.append(menu_recipe)


        df = pd.DataFrame({'menu_titles':menu_titles, 'menu_recipes':menu_recipes})
        df.to_csv('./crawling_data/recipe_{}page.csv'.format(j), index=False)