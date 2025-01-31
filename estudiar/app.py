
from playwright.sync_api import sync_playwright
import time
from bs4 import BeautifulSoup
import csv


'''
from playwright.sync_api import sync_playwright
import time

from bs4 import BeautifulSoup

p = sync_playwright().start()

browser = p.chromium.launch(headless=False)

page=browser.new_page()

page.goto("https://www.wanted.co.kr/search?query=flutter&tab=position")

# time.sleep(5)

# # page.screenshot(path="screenshot.png")

# page.click("button.Aside_searchButton__rajGo")

# time.sleep(5)

# page.get_by_placeholder("검색어를 입력해 주세요.").fill("flutter")
# #get_by_### id,label,text,attribute 등으로 가져올 수 있음

# time.sleep(5)

# page.keyboard.down("Enter")

# time.sleep(5)

# page.click("a#search_tab_position")



for pressend in range(5):
    time.sleep(5)
    page.keyboard.down("End")

time.sleep(5)

content=page.content()

p.stop()

soup = BeautifulSoup(content,"html.parser")

jobs = soup.find_all("div",class_="JobCard_container__REty8")

jobs_db = []

for job in jobs:
    link = f"https://www.wanted.co.kr/{job.find('a')['href']}" #href가 아니더라도 a(앵커) 안에있는 어떠한 atrribute(속성)도 설정 가능 
    title = job.find("strong", class_="JobCard_title__HBpZf").text
    company_name = job.find("span",class_="JobCard_companyName__N1YrF").text
    reword = job.find("span",class_="JobCard_reward__cNlG5").text
    job = {"title":title,"company_name":company_name,"reword":reword,"link":link}
    jobs_db.append(job)

print(jobs_db)
print(len(jobs_db))

'''

class studyClass:
    def __init__(self,url,looprange,delay,main_url):
        self.url = url
        self.looprange = looprange
        self.delay = delay
        self.main_url = main_url
        self.jobs_db = []
        self.keywords = ["flutter","python","java"]

    def playWright(self):

        p = sync_playwright().start()

        browser = p.chromium.launch(headless=False)

        self.page=browser.new_page()

        self.page.goto(self.url)

        for press_end in range(self.looprange):
            time.sleep(self.delay)
            self.page.keyboard.down("End")
        content = self.page.content()
        p.stop()
        return content
      


    def parSer(self,content):
        soup = BeautifulSoup(content,"html.parser")
        jobs = soup.find_all("div",class_="JobCard_container__REty8")
        for job in jobs:
            link = f"{self.main_url}{job.find('a')['href']}" #href가 아니더라도 a(앵커) 안에있는 어떠한 atrribute(속성)도 설정 가능 
            title = job.find("strong", class_="JobCard_title__HBpZf").text
            company_name = job.find("span",class_="JobCard_companyName__N1YrF").text
            reword = job.find("span",class_="JobCard_reward__cNlG5").text
            job ={
              "title": title,
              "company_name": company_name,
              "reward": reword,
              "link": link,}
            self.jobs_db.append(job)

    def keywordFind(self):
        for keyword in self.keywords:
            self.jobs_db = []
            self.url = f"https://www.wanted.co.kr/search?query={keyword}&tab=position"
            content = self.playWright()
            self.parSer(content)
            file = open(f"{keyword}.csv","w")
            writer = csv.writer(file)
            writer.writerow(["Title","Company","Reword","Link"])
            for job in self.jobs_db:
                writer.writerow(job.values())
            file.close()
        return
    
    def allSave(self):
        for keyword in self.keywords:
            self.url = f"https://www.wanted.co.kr/search?query={keyword}&tab=position"
            content = self.playWright()
            self.parSer(content)
            file = open("all_job.csv","w")
            writer = csv.writer(file)
            writer.writerow(["Title","Company","Reword","Link"])
            for job in self.jobs_db:
                writer.writerow(job.values())
            file.close()
        return
    
        

scraper = studyClass(url=f"https://www.wanted.co.kr/search?query=flutter&tab=position",looprange=4,delay=5,main_url="https://www.wanted.co.kr/")
scraper.keywordFind()
scraper.allSave()