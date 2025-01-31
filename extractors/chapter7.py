import requests
from bs4 import BeautifulSoup
import csv


class berlin:

    def __init__(self, url):
        self.url = url
        self.all_job = []
        self.keywords = ["python", "typescript", "javascript"]

    def scrape(self):
        self.response = requests.get(
            self.url,
            headers={
                "User-Agent":
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36"
            })
        self.soup = BeautifulSoup(self.response.content, "html.parser")

        self.jobs = self.soup.find_all("li", class_="bjs-jlid")
        print("Number of jobs found:", len(self.jobs))
        
        for job in self.jobs:
            title = job.find("a").text
            company = job.find("a", class_="bjs-jlid__b").text
            disc = job.find("div", class_="bjs-jlid__description").text.strip()
            link = job.find(
                "h4", class_="bjs-jlid__h").find_next_sibling("a")["href"]

            self.job_data = {
                "company": company,
                "title": title,
                "disc": disc,
                "link": link,
            }
            self.all_job.append(self.job_data)

            # if self.job_data not in self.all_job:
            #     self.all_job.append(self.job_data)

    def check_page(self):
        self.response = requests.get(
            self.url,
            headers={
                "User-Agent":
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36"
            })
        self.soup = BeautifulSoup(self.response.content, "html.parser")
        return len(
            self.soup.find("ul",
                           class_="bsj-nav").find_all(class_="page-numbers"))

    def change_page(self):
        total_page = self.check_page()
        for x in range(total_page):
            self.url = f"https://berlinstartupjobs.com/engineering/page/{x+1}/"
            self.scrape()
        return self.all_job

    def skill_page(self):
        for keyword in self.keywords:
            self.url = f"https://berlinstartupjobs.com/skill-areas/{keyword}/"
            self.scrape()
        return self.all_job

    def skill_page_keyword(self, keyword):
        self.url = f"https://berlinstartupjobs.com/skill-areas/{keyword}/"
        self.scrape()
        return self.all_job

    def saveCsv(self, filename, method):
        method()
        file = open(f"{filename}", "w")
        writer = csv.writer(file)
        writer.writerow(["Company", "Title", "Disc", "Link"])
        for job in self.all_job:
            writer.writerow(job.values())
        file.close()

    def saveForUser(self, filename, all_jobs):
        file = open(f"{filename}.csv", "w")
        writer = csv.writer(file)
        writer.writerow(["Company", "Title", "Disc", "Link"])
        for job in all_jobs:
            writer.writerow(job.values())
        file.close()

class web3(berlin):
    def scrape(self):
        self.response = requests.get(self.url,headers={"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36"})
        self.soup = BeautifulSoup(self.response.content, "html.parser")
        self.jobs = self.soup.find_all("tr",class_="table_row")
        # print(response.content)
        # print(response.status_code)
        print("Number of jobs found:", len(self.jobs))

        for job in self.jobs:
            if job.find("h2",class_="fs-6"):
                title = job.find("h2",class_="fs-6").text
            else:
                title = "N/A"
            if job.find("td",class_= "job-location-mobile") and job.find("td",class_= "job-location-mobile").find("h3"):
                company = job.find("td",class_= "job-location-mobile").find("h3").text
            else:
                company = "N/A"
            if job.find("a",href="/web3-jobs-paris"):
                loca = job.find("a",href="/web3-jobs-paris").text
            else:
                loca = "N/A"
            if job.find("td",class_="job-location-mobile") and job.find("td",class_="job-location-mobile").find("a")["href"]:
                link = job.find("td",class_="job-location-mobile").find("a")["href"]
            else:
                link = "N/A"

            self.job_data = {
            "company" : company,
            "title" : title,
            "disc or location" : loca,
            "link" : f"https://web3.career/{link}",}
            self.all_job.append(self.job_data)

    def skill_page_keyword(self, keyword):
        self.url = f"https://web3.career/{keyword}-jobs"
        self.scrape()
        return self.all_job

class wework(berlin):
    def scrape(self):
        self.response = requests.get(self.url,headers={"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36"})
        self.soup = BeautifulSoup(self.response.content, "html.parser")
        self.jobs = self.soup.find_all("li",class_="feature")
        print("Number of jobs found:", len(self.jobs))

        for job in self.jobs:
            if job.find("span",class_= "title"):
                title = job.find("span",class_= "title").text
            else:
                title = "N/A"
            if job.find("span",class_= "company"):
                company = job.find("span",class_= "company").text
            else:
                company = "N/A"
            if job.find("span",class_= "region"):
                loca = job.find("span",class_= "region").text
            else:
                loca = "N/A"
            if job.find("div",class_="tooltip--flag-logo") and job.find("div",class_="tooltip--flag-logo").find("a")["href"]:
                link = job.find("div",class_="tooltip--flag-logo").find("a")["href"]
            else:
                link = "N/A"

            self.job_data = {
            "company" : company,
            "title" : title,
            "disc or location" : loca,
            "link" : f"https://weworkremotely.com/remote-jobs/{link}",}
            self.all_job.append(self.job_data)

    def skill_page_keyword(self, keyword):
        self.url = f"https://weworkremotely.com/remote-jobs/search?utf8=%E2%9C%93&term={keyword}"
        self.scrape()
        return self.all_job
    
# 스크래퍼 인스턴스 생성
berlin_scrapper = berlin("https://berlinstartupjobs.com/engineering/")

# 데이터를 먼저 가져옴
jobs1 = berlin_scrapper.skill_page_keyword("python")

# 가져온 데이터를 저장
berlin_scrapper.saveForUser("berlin_jobs", jobs1)

# 스크래퍼 인스턴스 생성
web3_scrapper = web3("https://web3.career/python-jobs")

# 데이터를 먼저 가져옴
jobs2 = web3_scrapper.skill_page_keyword("python")

# 가져온 데이터를 저장
web3_scrapper.saveForUser("web3_jobs", jobs2)

# 스크래퍼 인스턴스 생성
wework_scrapper = wework("https://weworkremotely.com/remote-jobs/search?utf8=%E2%9C%93&term=python")

# 데이터를 먼저 가져옴
jobs3 = wework_scrapper.skill_page_keyword("python")

# 가져온 데이터를 저장
wework_scrapper.saveForUser("wework_jobs", jobs3)