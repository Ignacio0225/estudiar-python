import requests
from bs4 import BeautifulSoup
import csv


class main():
    def __init__(self,url):
        self.url = url
        self.all_job =[]
        self.keywords = ["python","typescript","javascript","rust"]

    def saveForUser(self,filename,all_jobs):
            file = open(f"{filename}.csv","w")
            writer = csv.writer(file)
            writer.writerow(["Company","Title","Disc or Location","Link"])
            for job in all_jobs:
                writer.writerow(job.values())
            file.close()

class berlins(main):

    
    def __init__(self,url):
        super().__init__(url)

    def response(self):
        response = requests.get(self.url,headers={"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36"})
        return BeautifulSoup(response.content,"html.parser")

    def scrape(self):
        self.soup = self.response()
        self.jobs = self.soup.find_all("li",class_="bjs-jlid")   

        for job in self.jobs:
            title = job.find("a").text
            company = job.find("a",class_= "bjs-jlid__b").text
            disc = job.find("div",class_="bjs-jlid__description").text.strip()
            link = job.find("h4",class_="bjs-jlid__h").find_next_sibling("a")["href"]
    
            self.job_data = {
                "company" : company,
                "title" : title,
                "disc" : disc,
                "link" : link,
                }
            self.all_job.append(self.job_data)
            

            # if self.job_data not in self.all_job:
            #     self.all_job.append(self.job_data)

    def check_page(self):
        self.soup = self.response()
        return len(self.soup.find("ul",class_="bsj-nav").find_all(class_="page-numbers"))
    
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
    
    def skill_page_keyword(self,keyword):
            self.url = f"https://berlinstartupjobs.com/skill-areas/{keyword}/"
            self.scrape()
            return self.all_job

    def saveCsv(self,filename,method):
        method()
        file = open(f"{filename}","w")
        writer = csv.writer(file)
        writer.writerow(["Company","Title","Disc","Link"])
        for job in self.all_job:
            writer.writerow(job.values())
        file.close()


class web3(berlins):
    def __init__(self,url):
        super().__init__(url)

    def response(self):
        response = requests.get(self.url,headers={"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36"})
        return BeautifulSoup(response.content,"html.parser")

    def scrape(self):
        self.soup = self.response()
        self.jobs = self.soup.find_all("tr",class_="table_row")   

        for job in self.jobs:
            if job.find("h2",class_="fs-6"):
                title = job.find("h2",class_="fs-6").text
            else:
                "N/A"
            if job.find("td",class_= "job-location-mobile") and job.find("td",class_= "job-location-mobile").find("h3"):
                company = job.find("td",class_= "job-location-mobile").find("h3").text
            else:
                "N/A"
            if job.find("a",href="/web3-jobs-paris"):
                loca = job.find("a",href="/web3-jobs-paris").text
            else:
                "N/A"
            if job.find("td",class_="job-location-mobile") and job.find("td",class_="job-location-mobile").find("a")["href"]:
                link = job.find("td",class_="job-location-mobile").find("a")["href"]
            else:
                "N/A"

            self.job_data = {
                "company" : company,
                "title" : title,
                "disc or location" : loca,
                "link" : f"https://web3.career/{link}",
                }
            self.all_job.append(self.job_data)

    def skill_page_keyword(self, keyword):
        self.url = f"https://web3.career/{keyword}-jobs"
        return super().skill_page_keyword(keyword)

            

# class wework:

# engineering = berlins("https://berlinstartupjobs.com/skill-areas/python/")
# skill = berlins()
python= web3("https://web3.career/python-jobs")
# skill.saveCsv(filename="skill.csv",method = skill.skill_page)
# engineering.saveCsv(filename="engineering.csv",method = engineering.change_page)

# print(len(skill.skill_page()))
print(len(engineering.change_page()))
# print(len(python.skill_page_keyword(keyword = "python")))

# everything = skill.skill_page() + engineering.change_page()
# print(len(everything))

# all_job_combine = []

# for job in skill.skill_page():
#     all_job_combine.append(job)
# for job in engineering.change_page():
#     all_job_combine.append(job)

# all_job_combine.saveAll(filename="file3.csv",list = all_job_combine)