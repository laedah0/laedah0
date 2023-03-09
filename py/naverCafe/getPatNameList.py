import re
import csv
import time

from datetime import datetime
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

names = ['공모명', '검단 제일풍경채 2차 에듀&파크', '풍경채 그랑 에듀', '검단 센트럴파크펠라 (제일풍경채)', '검단 제일풍경채 그랑포레', '검단 제일풍경채 에듀포레', '검단 제일풍경채2차 온새미로', '검단 제일풍경채 그랜드 노블(grand noble)', '검단 제일풍경채 더에듀포레', '검단 제일풍경채 센트럴포레', '풍경채 그리니티 (Greenity)', '제일풍경채 센트럴파크', '제일풍경채 오투그란데', '검단 제일풍경채 그랑트리니티', '풍경채 라 그란데', '제일풍경채2차 그랜드파크', '검단 제일풍경채 더 오메가포레', '○○역 제일풍경채', '검단 풍경채 원베일리', '검단 풍경채 그랑디움', '검단 풍경채 헤리티지', 'the PungKyeongChae life(더 풍경채 라이프)', '제일풍경채 그란뜰 GRANDLE', '검단 제일풍경채 2차 아띠마을', '검단 풍경채 어바니티', '풍경채 그레이스풀 (graceful)', '풍경채 에르모소 (hermoso)', '제일풍경채 데 트라움(Ter Traum)', '검단 제일풍경채 트리플스퀘어', '검단 풍경채 더 트 리니티 (The Trinity)', '제일풍경채 엘리니티', '풍경채 클로리스 (Chloris)', '제일풍경채 더 레인보우스퀘어', 'Pung Kyeong Chae The Grand (풍경채 더 그랜드)', '검단 풍경채 그린시티', '더 풍경채 웜빌리지(warm village)', '검단 월드클래스 풍경채 2', '풍경채2차 퍼스티지', '검단 제일풍경채 더 그랜드', '검단의 두번째 풍경채 더그랜드', '검단 제일풍경채2차 트리플에듀', '검단 제일풍경채 2차 에듀포레', '제일풍경채 로얄트리플에듀', '제 일 좋은 풍경채 2차', '검단 제일풍경채2 프리미아(Premia)', '제일풍경채 라온제나', '제일 풍경채 더 포레스트', "풍경채 더 숨 [THE S'oom]", '제일풍경채 그랜드 포레', '검단 제일풍경채2차 트리플에듀파크', '제일풍경채 트리플에듀', '제일풍경채 걸작', '제일 풍경채 그린나래', '검단 풍경채 로', '검단 제일 풍경채 2차 다온', '제일풍경채 엘리시움', '검단 제일풍경채 가온누리', '제일 풍경채 더 숲', '검단 제일풍경채 그랜드1734', '검단 제일풍경채 에듀&포레', '검단 제일풍경채 더 프라임', '검단제일풍경채더베스트', '검단 (제일)풍경채 II 빅라이프', '검단 풍경채 그래비티 [Gravity]', '풍경채 두리', '검단 제일풍경채 G1', '풍경채:움', '제일풍경채 더올림 (The Ollim)', '검단 유포리아 풍경채', '검단 늘(Neul) 풍경채', '검단 풍경채 그리너스(GREEN-US)', '검단 풍경채 팰리스카운티(PALACE COUNTY)', '풍경채 1734', '숲속의 풍경채', '검단 풍경채 (더) 클래식', '제일풍경채 더 그 랜드', '풍경채 더 MQV(엠큐브이)', '풍경채 커넥션(connection)']
# subs = ['의미', '횡단보도 앞 유/초/중/고교 학세권, 아파트 단지 뒤 황화산 근린공원 및 검단신도시, U자형 공원으로 이뤄지는 파크를 더했음', '쾌적한 환경 혹은 강점인 교육', '숲속의 진주, 펠라(스페인어로 진주)', '검단 최대규모 단지와 산, 공원이 옆에 있는 맑고 쾌적한 아파트', '에듀+포레스트의 합성어, 학세권과 숲(산, 공원)', '자연 그대로, 언제나 변함없이', '거대한 상류층/검단 제일 큰 대단지의 그랜드, 검단 제일 상류층이 되길 바람', '학 군, 숲 조성단지 강조', '검단의 중심에 있으면서 공원의 장점을 강조', '풍경채=아름다운 풍경이 있는 집, 그린+트리니티(Green+trinity) 합성어 / 팍세권, 학세권, 역세권의 장점을 내포하는 합성어', '중심가를 뜻하는 형용사 Central과 자연과의 조화를 뜻하는 Park, 초/중/고를 품은 아파트이지만 에듀는 교육 쪽으로만 초점을 두는 것 같아 다른 장점을 가릴 수 있을 것 같음', "102역 및 단지주변으로 학원가 형성으로 역세권 및 학세권이며, 단지 옆 의 황화산 및 근린공원의 숲세권으로서 맑은 공기, 즉, 산소를 뜻하는 화학 원소기호 O2와, 넓다, 많다는 의미의 이태리어 그란데를 써서 '학교(학원)와 산소가 많다 것과 대단지'라는 의미가 담겨있음.", '세 가지 좋은 환경(숲 세권, 역세권, 학세권)을 갖춘 대단지 제일풍경채', '검단에서 제일 큰 대단지', '황화산 숲세권 대단지', '검단 내 숲세권 끝판왕(Omega)의 의미를 담았음', '단지의 가장 큰 특징인 서울과 가까운 역세권이라는 점을 강조, 가까운 미래에 GTX나 5호선이 102역으로 유치된다면 이름 자체가 브랜드가 될 것으로 생각', '베일리는 중세시대 영주들이 살던 성의 중심부를 뜻함, 그 중 최고인 ONE을 합쳤음, 중심중의 중심, 예부터 가장 큰 건물이 중심이 됨, 검단에서 큰 단지임을 뜻함', '대단지 Grand, 공간이라는 뜻의 독일어 Raum을 합침, 검단 신도시 내 최고 대단지, 트리플세권(숲, 학교, 역), 대단지 커뮤니티 시설 등 모든 것이 최고라는 의미', '아파트가 위치한 불로동의 지명  유래를 본따 오래오래 살면서 자식들에게 유산(Heritage)으로 남겨줄 수 있는 멋진 아파트가 되자는 의미', '심플하게 누구나 알고 있고, 살고 싶다는 의미, 외우기 쉬움', '큰 뜰이라는 의미', '아띠가 사랑이라는 뜻의 순 우리 말', '완벽한 도시의, 세련된이라는 뜻, 판교 풍경채 어바니티의 고급스러움을 함께 가져가고 싶음을 담았음', '우아하고 고급진 풍경채, 늘 품위를 지키는 검단의 중심이 되자는 의미', '스페인어로 아름다운, 예쁜, 고운이라는 뜻으로 한글로 4글자라 예쁠 것 같음, 문주로 만들어도 깔끔하고 고급져보일 것 같음, 보이는 디자인이 깔끔한 단어', '검단 트라움 혹은 트라움검단으로 간소화, 트라움은 독일어로 꿈, 환상과 소원을 뜻함, 풍경채에 당첨되길  꿈꾸었고 앞으로 꿈을 위해 살아갈 것이라며 우리 모두의 소원이 이루어지길 바라는 의미', '학세권, 숲세권, 역세권 3가지 장점들이 한 곳에 모여있는 아파트', '‘학세권, 숲세권, 역세권’ 삼위일체된 살기 좋은 단지라는 의미. 판교 풍경채 어바니티와 유사한 발음의 단어를 차용한 고급화 전략.', '최고의 품위와 무한한 가능성이 있는 분들이 모여산다는 의미, Elite+Dignity+Infinity+Community', '그리스 신화의 꽃과 봄의 여신, 클로리스는 그리스어로 노란빛이 도는 녹색을 의미', '행복 가득 다채롭고 아름답게 빛나라는 의미로 조합', '대규모 단지', '1700세대 큰 단지가 녹색 푸르름으로 가득 찬 뒷동산이 있고 주변에 녹지 조성이 잘 되어 있어 대단지 느낌도 살려 그린과  시티를 합쳤음', '삭막한 세상에 누구나 마음이 따뜻해지는, 어느 가정이나 따뜻하고 포근한 그런 마을 혹은 공동체였으면 하는 바람을 담았음', '\u3000', '가장 앞서길 희망하는 의미', '검단신도시 가장 많은 세대수를 보유하 고 있는 제일풍경채 2차의 특성을 담았음', '대단지를 의미, 2차 단지 표기의 수요가 있는 것 같아 포함', '아파트 장점 중 하나인 초/중/고 학세권을 강조할 수 있음', '초중고에 산, 근린공원을 강조', '지하철 3개 상가지역이 유흥시설업 제한지역이니 자연적으로 학원가 형성이 될 예정이라 지리적 가치를 담아보았음', '뒤에 산과 공원을 두고 앞에 학교를 둔 검단에서 제일 좋은 아파트라는 의미', '프리미아는 폴란드어로 보너스라는 의미, 우리 아파 트는 공원/학교/지하철을 모두 포함하고 있는 삶의 보너스가 되는 의미를 담고 있음', '라온제나는 순 우리말로 즐거운 나라는 뜻, 모두 즐거운 삶을 살 수 있는 아파트가 되길 바라는 바램을 담았음', '우리 아파트 최대 장점인 숲을 강조', '검단은 검붉은 갯벌을 뜻함, 갯벌은 숨쉬는 자연', '단지가 제일 크고 사람도 많고 옆에 산이 있음을 의미', '학세권, 팍세권을 모두 충족하는 아파트라는 의미', '\u3000', '매우 뛰어난 작품, 훌륭한 우리 아파트 가 되길 바라는 마음을 담았음', '그린나래는 순 우리말로 아름다운 날개를 뜻함, 날개는 비상을 뜻하니 가치가 돋보이는 아파트 이미지로 괜찮을 것 같음', "한자 '길 로' 자를 뜻하며, 모든 것(학교, 공원, 사람 등)은 풍경채로 통한다는 의미", '온새미로는 자연 그대로, 다온은 좋은 모든 일들이 다 오는 이라는 뜻을 가진 순 우리말', '지상의 행복으로 제일풍경채에 사는 사람들이 모두 행복하길 바라는 바램을 담았음', '가온누리는 세상의 중심이라는 뜻의 순 우리말', '숲이 가깝다는 장점을 심플하게 나타내보았음', '타 아파트와 비교했을 때 가장 큰 장점이 세대 수인 듯 하여 대단지를 강조한 그랜드와 세대 수인 1734를 합쳤음', '학세권, 숲세권을 직설적인 단어로 표현', '\u3000', '제일건설이고, 제일 좋은 아파트, 타 아파트에 비해 더 좋고 제일 좋다는 이미지를 담았음', '2등, 두번째라는 아라비아 숫자 2 대신 큰 숫자의 의미로 로마자 II로 표현, 분양 시 내세운 슬로건 빅라이프가 우리 단 지에 가장 잘 어울리고 함축적으로 표현하고 있다고 생각함', '우리 삶의 중대한 빅라이프의 시작, 교통/교육/녹지 무엇 하나 빼놓을 수 없는 웅장하고 엄숙한 대단지 아파트, 마음을 끌어당기는 절대적인 힘을 상징', "둘째라는 의미로 2차를 표현, 두리는 하나로 뭉치게 되는 중심의 둘레라는 뜻의 순 우리말, 검단신도시의 중심을 뜻하고자 하고 '둘이'라는 타인들과 함께 한다는 느낌의 표현을 더함", 'Great One을 뜻함', '채움은 가득 채우다는 뜻으로 모든 것이 풍족하게 가득 채운 공간, ium(움)은 공간이라는 뜻으로 이중적인 의미가 담겨있음', '인생, 가치, 아파트 품격, 교육, 삶의 질을 어느 아파트보다도 더 올림이라는 의미', '가슴 벅찬, 행복한, 희열이라는 뜻, 청약당 첨의 가슴 벅찬 마음과 앞으로 풍경채에서 보낼 행복한 하루하루, 트리플세권에서의 생활을 통해 희열을 느끼며 건강하게 성장하기를 소망하는 의미', "언제나라는 뜻으로 '늘'이라는 단어 뒤에 붙는 문장들은 모두 긍정을 의미함", '풍경채를 뒷받칠만한 원초적이고 간결한 의미의 Green, 입주민과 우리 모두를 뜻하는 US를 합쳤음, 아직 그리너스라는 펫네임을 사용하는 아파트가 없어서 우리가 사용할 경우 최초가 될 수 있음', '궁전같은 집이 모여있는  주를 뜻함, 풍경이 있는 궁전같은 대단지', '1734세대의 풍경채를 의미', '공원과 동산이 둘러쌓여있음을 의미, 풍경채라는 회사 네임을 필수로 가져가야 할 경우 이국적인 펫네임과 풍경채는 조화롭지 못함', '풍경채 자체가 자 연친화적인 의미라 별도의 단어는 생략, 세월이 흘러도 격조와 품격을 유지한다는 느낌, 클래식한 아파트를 의미', '검단에서 세대 수가 가장 많다는 점을 뜻함', '더 나은 삶의 질을 뜻하는 프랑스어들을 합성하여 표현, meilleure(더 나은, 더 좋은 등) qualite(특성, 장점, 품질 등) de vie(생명, 목숨 등)', '5차까지 있는 풍경채를 이어주고, 1차부터 3차까지 신도시를 이어준다는 것을 의미']

# Chrome 드라이버 실행 파일 경로
chrome_driver_path = '/path/to/chromedriver'

# Chrome 드라이버 실행
service = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service)

# webdriver로 크롬 브라우저 실행
#driver = webdriver.Chrome('/path/to/chromedriver')

# 네이버 로그인 페이지로 이동
driver.get('https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com')

# 아이디와 비밀번호 입력
# driver.find_element(By.NAME, 'id').send_keys('laedah0')
# driver.find_element(By.NAME, 'pw').send_keys('Spdlqj@83')

# 로그인 버튼 클릭
# driver.find_element(By.ID, 'log.login').click()

# 페이지 이동 대기
# time.sleep(1)

input('로그인 완료 후 엔터를 입력해 주세요...')  # 엔터 입력을 대기

#driver.find_element(By.NAME, 'pw').send_keys('Spdlqj@83')

# 카페 페이지로 이동
driver.get('https://cafe.naver.com/gdjp2')

# 페이지 이동 대기
# time.sleep(3)
# 이동할 페이지 주소 입력받기
#urlKey_input = input("게시물 번호를 입력하세요(예 5225): ")
input("댓글집계를 원하는 게시물로 이동 후 엔터를 입력해 주세요...")

# 게시물 클릭
#driver.find_element(By.XPATH, f'//a[contains(@href,"{urlKey_input}")]')\
#    .send_keys(Keys.RETURN)



# 문자열에서 숫자만 추출하여 배열에 담을 리스트 생성
numbers = []

# 댓글들 수집 리스트 생성
comments = []

#문자열에서 숫자만 추출하여 배열에 담기
def extract_numbers(_string):
    """
    Given a string, extracts all numbers separated by ",", ".", or whitespace characters and returns them as a list.
    """
    if _string is None:
        return 

    #numbers = []
    
    # 문자열을 "," "." 혹은 공백으로 분리하여 리스트에 담기
    parts = re.split('[,.\\s]+', _string)
    
    # 리스트에 담긴 문자열들 중에서 숫자인 것만 추출하여 숫자로 변환하여 numbers 리스트에 추가
    for part in parts:
        if part.isdigit():
            numbers.append(int(part))
    
    return

# csv파일로 저장하기
def save_to_csv(data, filename):
    now = datetime.now()
    timestamp = now.strftime("%Y-%m-%d_%H-%M-%S")
    filename_with_timestamp = f"{filename}_{timestamp}.csv"
    
    with open(filename_with_timestamp, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(data)


driver.switch_to.frame('cafe_main') #iframe으로 접근

# 총 댓글 페이지 
totalPage = 3
# 넘길 댓글 페이지 넘버
page = 1

nextPageKey = True

while nextPageKey:
    # 댓글 로딩 대기
    time.sleep(3)

    # 댓글 html 파싱
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    #print("0--------------------------------------")
    #print(soup)
    #with open('filename.txt', 'w', encoding='utf-8') as file:
    #    file.write(str(soup))
    #comments = soup.find_all('span', class_='comment_box')

    # 댓글단 아이디를 담고있는 a 추출
    a_tags = soup.find_all('a', class_='comment_nickname')
    # 댓글들을 담고있는 span 추출
    span_tags = soup.find_all('span', class_='text_comment')

    
    # 추출된 댓글들 중 숫자만 정제하여 numbers에 담기
    for span, a in zip(span_tags, a_tags):
        # 추출된 내용을 확인할 수 있도록 아이디 : 댓글 출력
        a_text = a.get_text().replace("            ", "").replace("\n        ", "").replace("\n", "")
        span_text = span.get_text()
        comments.append([f"{a_text},{span_text}"])
        #print(f"{a.get_text()}: {span.get_text()}")
        extract_numbers(span_text)
    
    # print(comments)
    save_to_csv(comments, "comments")

    page += 1
    xpath = f'//*[@id="app"]/div/div/div[2]/div[2]/div[5]/div[2]/button[{page}]'
    
    try:
        button = driver.find_element(By.XPATH, xpath)
    except NoSuchElementException:
        nextPageKey = False
    else:
        button.click()

# 입력된 배열에 숫자 출현 횟수를 세어 숫자와 각 출현 횟수를 출력하기
def count_numbers(numbers):
    """
    Given a list of numbers, counts the occurrences of each number and prints the counts.
    """
    # 딕셔너리 생성
    counts = {}
    num = 0
    
    # 배열에서 각 숫자의 출현 횟수 세기
    for number in numbers:
        if number in counts:
            counts[number] += 1
        else:
            counts[number] = 1
    
    # 각 숫자와 출현 횟수 출력
    for number, count in sorted(counts.items(), key=lambda x: x[1], reverse=True):
        num += 1
        print(f"{num}. {names[number]}: {count}")


print("-----------------------------------------------")
count_numbers(numbers)

# webdriver 종료
driver.quit()

print("--------------------------------------집계 완료.")
# 스크립트 코드
input("Press enter to exit")