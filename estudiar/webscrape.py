# from requests import get

import requests
from bs4 import BeautifulSoup

all_job = []  #외부 리스트


#url 안에서 원하는것을 스크래핑 하는 함수
def sacrape_page(url):
    print(f"Scrapping{url}...")  #각 페이지를 잘 받아오나 확인 (디버깅)

    response = requests.get(url)  #requests 패키지를 통해 url의 정보를 get함

    # print(response.content)

    soup = BeautifulSoup(
        response.content,
        "html.parser",
    )  # BeautifulSoup 패키지를 사용하여 reponse의 content를 html.parser 기능을 사용하여 html 형식으로 가져옴 , 이걸 거치지 않으면 일반문자열 형식이 돼버림

    jobs = soup.find("section", class_="jobs").find_all(
        "li"
    )[1:
      -1]  #jobs 라는 클래스 이름을 가진 첫번째 section을 찾고 그중 모든 li(html 리스트 태그) 를 리스트 형태로 jobs 변수에 저장
    # 클래스 대신 id="category-2 로 사용가능
    # print(jobs)

    for job in jobs:
        title = job.find("span", class_="title"
                         ).text  # title 이라는 클래스를 가진 첫번째 span을 찾아서 title 변수를 만듬
        if len(job.find_all("span", class_="company")) == 3:
            company, position, region = job.find_all("span", class_="company")
        else:
            "N/A"
        url = job.find("div", class_="tooltip--flag-logo").next_sibling["href"]

        #url = job.find("a")["href"] 이렇게 썼을때 첫번째 앵커를 가져오기때문에 위에처럼 첫번째 앵커가 들어있는 div 를 건너뛰는 속성을 주고(툴팁 다음이 두번째 a가 있는자리) 그후에 href를 가져옴
        #url = job.find("a")
        #if url:
        #   url = url["href"]  이거랑 동일함 a 옆에 href 가 없을경우를 대비하여 href가 없으면 none 로 만들어줌

        # region = job.find("span", class_="region").text if job.find(
        #     "span", class_="region") else "N/A"
        # companies = job.find_all("span", class_="company")
        # company = companies[0].text if len(companies) > 0 else "N/A"
        # position = companies[1].text if len(companies) > 1 else "N/A"
        # company, position = job.find_all("span", class_="company") 이렇게하면 순서대로 각 변수에 리스트가 분할됨(unpack).
        # 리스트 개수와 변수의 개수가맞아야함 (그런데 이 경우에는 리스트 개수가 맞지않아서 저렇게 사용)
        # print(title, region, company, position, "--------\n")
        job_data = {
            "title": title,
            "company": company.text,
            "region": region.text,
            "position": position.text,
            "url": f"https://weworkremotely.com/{url}",
        }
        all_job.append(job_data)  # all_job 이라는 외부 빈 리스트에 job_data를 넣어줌


#페이지 길이를 찾아주는 함수
def get_pages(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    return len(
        soup.find("div", class_="pagination").find_all("span", class_="page"))


total_pages = get_pages(
    "https://weworkremotely.com/remote-full-time-jobs?page=1"
)  #페이지 길이를 저장 해주는 변수

#페이지 길이에 맞춰서 for문을 실행 후 scrape_page() 함수에 각 페이지 url을 넣어줌
for x in range(total_pages):
    url = f"https://weworkremotely.com/remote-full-time-jobs?page={x+1}"
    sacrape_page(url)  #각 페이지 마다 sacrape_page() 함수를 실행

print(len(all_job))  # all_job에 쌓인 리스트의 길이를 확인, 너무 길어서 다 출력해서 보기힘듬.
