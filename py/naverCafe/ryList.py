import time
from selenium import webdriver
import csv
import pandas as pd
from bs4 import BeautifulSoup as bs
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

total_list=["제목","작성시간","조회"]

f=open('crawl.csv','w',encoding="utf-8",newline='')
wr=csv.writer(f)
wr.writerow([total_list[0],total_list[1],total_list[2]])
f.close()
i=0
while(True):
    origin_df=pd.read_csv('crawl.csv',encoding='utf-8')

    # 네이버 로그인 url
    url='https://nid.naver.com/nidlogin.login'
    id="laedah0"
    pw="Spdlqj@83"
    

    browser=webdriver.Chrome(ChromeDriverManager().install())
    browser.get(url)

    browser.implicitly_wait(2)

    # 로그인
    browser.execute_script("document.getElementsByName('id')[0].value=\'"+ id + "\'")
    browser.execute_script("document.getElementsByName('pw')[0].value=\'"+ pw + "\'")

    browser.find_element(by=By.XPATH,value='//*[@id="log.login"]').click()
    time.sleep(60)
	
    # 크롤링 하고자하는 url
    baseurl='https://cafe.naver.com/gdjp2/'
    browser.get(baseurl)
    
    i=i+1

    clubid=5225
    # 전체글
    boardtype="L"
    pageNum = i
    print(pageNum)
    userDisplay = 50

    browser.get(baseurl + 'ArticleList.nhn?search.clubid=' + str(clubid) + '&search.boardtype=' + str(boardtype) +'&search.page='+ str(pageNum) +'&userDisplay=' + str(userDisplay))
    browser.switch_to.frame('cafe_main') #iframe으로 접근

    soup = bs(browser.page_source ,'html.parser')
    soup = soup.find_all(class_ = 'article-board m-tcol-c')[1]# 네이버 카페 구조 확인후 게시글 내용만 가저오기

    datas = soup.select("#main-area > div:nth-child(4) > table > tbody > tr")
    
    for data in datas:
        article_title = data.find(class_= "article")
        article_date=data.find(class_='td_date')
        article_view=data.find(class_='td_view')

        if article_title == None :
             article_title = "null"
        else:
            article_title = article_title.get_text().strip() 

        if article_date ==None:
            article_date="null"
        else:
            article_date = article_date.get_text().strip()

        if article_view == None:
            article_view="null"
        else:    
            article_view = article_view.get_text().strip()

        f = open('crawl.csv', 'a+', newline='', encoding = "utf-8")# 문자 인코딩 -> euc-kr 형태로 변경하여 사용. 안되면 utf-8로 변경 후 진행
        wr = csv.writer(f)
        wr.writerow([article_title,article_date,article_view ])
        f.close()        
        
    print('종료')