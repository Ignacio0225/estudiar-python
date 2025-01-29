import requests
from bs4 import BeautifulSoup
import csv


class challenge4:

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


engineering = challenge4(
    url="https://berlinstartupjobs.com/engineering/page/1/")
skill = challenge4(url="https://berlinstartupjobs.com/skill-areas/python/")

#skill.saveCsv(filename="test1.csv",method = skill.skill_page)
engineering.saveCsv(filename="test2.csv",method = engineering.change_page)

# print(len(skill.skill_page()))
# print(len(engineering.change_page()))

# everything = skill.skill_page() + engineering.change_page()
# print(len(everything))
# all_job_combine = []

# for job in skill.skill_page():
#     all_job_combine.append(job)
# for job in engineering.change_page():
#     all_job_combine.append(job)

# all_job_combine.saveAll(filename="file3.csv",list = all_job_combine)
