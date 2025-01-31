import requests
from bs4 import BeautifulSoup

class Scraper():
  def __init__(self,keywords):
    self.keywords = keywords
    self.all_job = []

  class Job_Data():

    def __init__(self, position, company, location, salary):
      self.position = position
      self.company = company
      self.location = location
      self.salary = salary

    # def __repr__(self):
    #   return f"Job_Data(position={self.position!r},company = {self.company!r}, location = {self.location!r}, salary = {self.salary!r})"

    # def __str__(self):
    #   return f"posision:{self.position},company:{self.company},location:{self.location},salary:{self.salary}"


  def remoteok(url):
    print(f"scrapping{url}...")
    response = requests.get(
        url,
        headers={
            "User-Agent":
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
        })
    # print(response.status_code)
    # print(response.content)

    soup = BeautifulSoup(response.content, "html.parser")

    jobs = soup.find("table", id="jobsboard").find_all("tr", class_="job")
    # print(jobs)

    for job in jobs:
      position = job.find("td", class_="company").find(
          "a", class_="preventLink").text.strip()
      company = job.find("span", class_="companyLink").text.strip()
      if len(job.find_all("div", class_="location")) == 2:
        location, salary = job.find_all("div", class_="location")
      else:
        "N/A"

      job_data = scraper.Job_Data(
          position=position,
          company=company,
          location=location.text,
          salary=salary.text,
      )

      self.all_job.append(job_data.__dict__)


  for lang in keyword:
    url = f"https://remoteok.com/remote-{lang}-jobs"
    remoteok(url)
    
  def scrape_all(self):
    for keyword in self.keywords
    self.remoteok(keyword)
    
  def get_all_jobs(self):
    return self.all_jobs

keyword = ["flutter", "python", "golang"]
scraper = Scraper(keyword)
scraper.scrape_all()
print(self.all_job)

