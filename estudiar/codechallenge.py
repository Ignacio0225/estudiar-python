import requests
from bs4 import BeautifulSoup

keyword = ["flutter", "python", "golang"]

all_job = []


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

    job_data = Job_Data(
        positio=position,
        company=company,
        location=location.text,
        salary=salary.text,
    )

    all_job.append(job_data.__dict__)


for lang in keyword:
  url = f"https://remoteok.com/remote-{lang}-jobs"
  remoteok(url)

print(all_job)
