# BLUEPRINT | DONT EDIT

import requests
from bs4 import BeautifulSoup
import csv

all_job = []

def scrape_page(url):
    
    response = requests.get(
        url,
        headers={
            "User-Agent":
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        })
    soup = BeautifulSoup(response.content, 'html.parser',)
    jobs = soup.find('ul', class_='jobs-list-items').find_all('li')


    for job in jobs:
        try:
            company_name = job.find('a', class_='bjs-jlid__b').text
            company_position = job.find('h4', class_='bjs-jlid__h').text.strip()
            company_explain = job.find('div', class_='bjs-jlid__description').text.strip()
            company_url = job.find('h4', class_='bjs-jlid__h').find('a')['href']
        except:
            continue
        
        jobs_data = {
            'company_name' : company_name,
            'position' : company_position,
            'explain' : company_explain,
            'url' : company_url, 
        }
        all_job.append(jobs_data)
        for i in all_job:
            for key, value in i.items():
                print(f'❤ {key} : {value}')
            print('-----------------')
    
    

def pagination():
    all_job.clear()
    response = requests.get('https://berlinstartupjobs.com/engineering/page/1/',headers={
                "User-Agent":
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
            })
    soup = BeautifulSoup(response.content, 'html.parser')
    jobs = soup.find('div', class_='bsj-template__b')
    nav = jobs.find('ul', class_='bsj-nav')
    button = len(nav.find_all('a', class_='page-numbers'))
    for x in range(button):
        url = f'https://berlinstartupjobs.com/engineering/page/{x+1}/'
        scrape_page(url)
    return all_job
    

def skill_job():
    all_job.clear()
    skills = ["python", "typescript", "javascript", "rust"]
    for skill in skills :
        url = f'https://berlinstartupjobs.com/skill-areas/{skill}/'
        print(f'🧐 skill : {skill}')
        scrape_page(url)
    return all_job

pagination_results = pagination()
print("Pagination results:", len(pagination_results))
skill_job_results = skill_job()
print("Skill job results:", len(skill_job_results))