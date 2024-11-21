#ChatGPT네이버기사크롤링.py
import requests
from bs4 import BeautifulSoup

# 대상 URL
url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EB%B0%98%EB%8F%84%EC%B2%B4"

# 요청 보내기
response = requests.get(url)

# 응답 성공 여부 확인
if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    
    # 기사 제목 크롤링 (네이버 뉴스의 제목 구조에 맞게 선택자 설정)
    # 예: 'list_title' 클래스가 기사 제목일 수 있음
    titles = soup.select('.news_tit')  # 네이버 뉴스 검색 결과 제목 CSS 선택자
    
    # 크롤링 결과 출력
    print("뉴스 기사 제목:")
    for idx, title in enumerate(titles, start=1):
        print(f"{idx}. {title.get_text()}")
else:
    print(f"요청 실패: 상태 코드 {response.status_code}")
