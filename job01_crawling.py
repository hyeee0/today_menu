import re
import pandas as pd
import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from bs4 import BeautifulSoup
import requests

pages = [13, 9, 5, 16, 7, 6, 7, 9, 9, 4, 8, 5, 7, 6, 3, 16, 4, 14, 5, 5, 9, 4, 2, 3, 9]

options = webdriver.ChromeOptions()
options.add_argument('lang=kr_KR')
driver = webdriver.Chrome('./chromedriver', options=options)
df_title = pd.DataFrame()

for i in range(1, 7): # 1페이지 부터 25페이지
    try:
        for j in range(1, pages[i-1]):
            url = 'https://2bob.co.kr/recipe.php?id=list&fKeyList=&fKeyValue=&eTheme={}&OrderCondition=&OrderBy=&page={}'.format(i,j)

            menu_urls = []
            menu_titles = []
            menu_recipes = []
            menu_ingredients = []

            driver.get(url)
            try:
                for k in range(1, 21):
                    url_xpath = '//*[@id="con_wrapper"]/div[5]/div[2]/div[2]/ul/li[{}]/a'.format(k) # url패스
                    link_url = driver.find_element('xpath', url_xpath).get_attribute('href')

                    menu_xpath1 = '//*[@id="con_wrapper"]/div[5]/div[2]/div[2]/ul/li[{}]/a/div[2]/p[2]'.format(k)  # 음식명
                    menu_title = driver.find_element('xpath', menu_xpath1).text # 음식명 텍스트로 저장
                    driver.find_element('xpath', menu_xpath1).click() # 음식명 클릭해서 상세페이지 들어감
                    time.sleep(0.1)
                    driver.page_source
                    menu_xpath2 = '//*[@id="con_wrapper"]/div[5]/div[2]/div[2]/div[2]'
                    menu_xpath3 = '//*[@id="con_wrapper"]/div[5]/div[2]/div[2]/div[2]/div[3]/div[2]/p' # 필수재료
                    menu_recipe = driver.find_element('xpath', menu_xpath2).text # 음식명 텍스트로 저장
                    menu_ingredient = driver.find_element('xpath', menu_xpath3).text

                    driver.back() # text 딴 뒤에 뒤로가기
                    menu_titles.append(menu_title)
                    menu_recipes.append(menu_recipe)
                    menu_urls.append(link_url)
                    menu_ingredients.append(menu_ingredient)

                    if k % 4 == 0: # 메뉴4개마다 저장해주기 -> 페이지가 적은 메뉴는 저장이 안되기에 4개마자 저장해준다
                        df = pd.DataFrame({'menu_titles': menu_titles, 'menu_recipes': menu_recipes, 'menu_urls':menu_urls, 'menu_ingredients':menu_ingredients})
                        df.to_csv('./crawling_data/recipe_{}_{}page_{}.csv'.format(i, j, k), index=False)
            except:
                print('review button', k, j)
    except:
        print('review button', k, j)