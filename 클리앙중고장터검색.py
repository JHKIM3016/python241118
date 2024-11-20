# coding:utf-8
from bs4 import BeautifulSoup
import urllib.request
import re 

#User-Agent를 조작하는 경우(아이폰에서 사용하는 사파리 브라우져의 헤더) 
hdr = {'User-agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/603.1.23 (KHTML, like Gecko) Version/10.0 Mobile/14E5239e Safari/602.1'}

for n in range(0,10):
        #클리앙의 중고장터 주소 
        data ='https://www.clien.net/service/board/sold?&od=T31&po=' + str(n)
        #웹브라우져 헤더 추가 
        req = urllib.request.Request(data, headers = hdr)
        data = urllib.request.urlopen(req).read()
        page = data.decode('utf-8', 'ignore')
        soup = BeautifulSoup(page, 'html.parser')
        list = soup.find_all('a', attrs={'class':'list_subject'})
"""
<span class="subject_fixed" data-role="list-title-text" title="서피스프로9 75만에 팝니다.키보드 및 펜 포함 16/256 윈도우 11 (작년8월 구입)">
서피스프로9 75만에 팝니다.키보드 및 펜 포함 16/256 윈도우 11 (작년8월 구입)
						</span>
                                                """
        for item in list:
                try:
                        #<a class='list_subject'><span>text</span><span>text</span>
                        title=item.find("span",attrs={"data-role":"list-title-text"})
                        title=title.text.strip()
                        if (re.search('아이폰', title)):
                                print(title)
                except:
                        pass
        
