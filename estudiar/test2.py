import requests
from bs4 import BeautifulSoup

all_job = []

def scrape(url):
    response = requests.get(url,headers={"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36"})
    soup = BeautifulSoup(response.content, "html.parser")
    jobs = soup.find_all("tr",class_="table_row")
    # print(response.content)
    # print(response.status_code)
    print("Number of jobs found:", len(jobs))

    for job in jobs:
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

        job_data = {
        "company" : company,
        "title" : title,
        "disc or location" : loca,
        "link" : f"https://web3.career/{link}",}
        all_job.append(job_data)

def skill_page_keyword(keyword):
    url = f"https://berlinstartupjobs.com/skill-areas/{keyword}/"
    scrape()


python = scrape("https://web3.career/python-jobs")

print(all_job)