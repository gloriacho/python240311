import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook

def naver_blog_crawler(search_keyword):
    wb = Workbook()
    ws = wb.active
    ws.append(['블로그명', '글 제목', '날짜'])  # 엑셀 파일 헤더 추가

    for page in range(1, 101):  # 1부터 100까지 페이지 순회
        url = f"https://search.naver.com/search.naver?where=view&sm=tab_jum&query={search_keyword}&start={((page-1)*10)+1}"
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')

        blog_posts = soup.find_all('li', class_='bx _svp_item')

        for post in blog_posts:
            blog_name = post.find('a', class_='sub_txt sub_name').text.strip()
            post_title = post.find('a', class_='api_txt_lines total_tit').text.strip()
            post_date = post.find('span', class_='sub_time').text.strip()

            # 결과를 엑셀 파일에 추가
            ws.append([blog_name, post_title, post_date])

    # 결과를 파일로 저장
    wb.save("result.xlsx")

# 키워드 설정
search_keyword = input("검색할 항목:")
naver_blog_crawler(search_keyword)
