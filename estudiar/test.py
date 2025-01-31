import requests
from bs4 import BeautifulSoup

class web3():
    def __init__(self, url):
        self.url = url
        self.all_job = []

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

python = web3(url = "https://web3.career/python-jobs")
print(python.skill_page_keyword(keyword = "python"))