"""
def say_hello(name, age):
  print("hello", name, "how r u?")
  print("i'm", age, "years old")

say_hello("sunhyuk", 34)

def say_bye(say, second):
  print(f"hello {say} , goodbye {second}")

say_bye("sunhyuk", "hyuk")

def tax_calculator(name, salary):
  print(f"{name}", salary * 0.35)

tax_calculator("sunhyuk", 40000000)

def say_hello2(user_name="anonymous"):
  print("hello", user_name)

say_hello2("nico")
say_hello2()

def plus(a=0, b=0):
  print(a + b)

plus(2, 3)

def minus(a=0, b=0):
  print(a - b)

minus(2, 3)

def multiplication(a=0, b=0):
  print(a * b)

multiplication(2, 3)

def division(a=0, b=1):
  print(a / b)

division()

def power(a=0, b=1):
  print(a**b)

power()

# - * / **

def tax_calc(money):
  return money * 0.35

def pay_tax(tax):
  print("thank you for paying", tax)

to_pay = tax_calc(150000000)
pay_tax(to_pay)

my_name = "sunhyuk"
my_age = 34
my_color_eyes = "brown"
print(
    f"hello I'm {my_name}, I have {my_age} years in the earth,{my_color_eyes}is my eye color"
)

def make_juice(fruit):
  return f"{fruit}+🥤"

def add_ice(juice):
  return f"{juice}+🧊"

def add_sugar(iced_juice):
  return f"{iced_juice}+🍬"

juice = make_juice("🍎")
cold_juice = add_ice(juice)
perfect_juice = add_sugar(cold_juice)

print(perfect_juice)

if 10 > 5:
  print("correct!")

a = "nico"

if a == "nico":
  print("true!")

password_correct = False
if password_correct:
  print("Here is your money")
else:
  print("wrong password")

winner = 10

if winner > 10:
  print("Winner is greater than 10")
elif winner < 10:
  print("Winner is less than 10")
else:
  print("Winner is 10")

age = int(input("How old are you?"))
print("user answer", age)

print(type(age))
if age < 18:
  print("You can`t drink.")
elif age >= 18 and age <= 35:
  print("You drink beer!")

  
elif age == 60 or age == 70:
  print("Birthday party!")
else:
  print("Go ahead!")

True and True == True
True and False == False
False and True == False
False and False == False

True or True == True
True or False == True
False or True == True
False or False == False

from random import randint, random, uniform

user_choice = int(input("Choose number."))
pc_choice = randint(1, 50)
if user_choice == pc_choice:
  print("You won")
elif user_choice > pc_choice:
  print("Lower! Computer choose", pc_choice)
elif user_choice < pc_choice:
  print("Higher Computer choose", pc_choice)

distance = 0

while distance < 20:
  print("I'm running:",distance,"km")
  distance = distance + 1


from random import randint
print("Welcome to Python Casino")
pc_choice = randint(1, 50)

playing = True

while playing:
  user_choice = int(input("Choose number."))

  if user_choice == pc_choice:
    print("You won")
    playing = False
  elif user_choice > pc_choice:
    print("Lower!")
  elif user_choice < pc_choice:
    print("Higher")




days_of_week = ["Mon","Tue","Wed","Thu","Fri"]

# name = "nico"
# print(name.upper())

days_of_week.append("Sat")

print(days_of_week)

days_of_week.append("Sun")

print(days_of_week)


days = ( "Mon", "Tue", "Wed")


player = {
  'name': 'nico',
  'age':12,
  'alive': True,
  'fav_food':["🍕","🍔"]
}
print(player.get('age'))
print(player['name'])
print(player['fav_food'])
print(player.get('fav_food'))


print(player)
player.pop('age')
player['xp'] = 1500
print(player)
player['fav_food'].append("🍜")
print(player)


from requests import get

websites = ("google.com", "airbnb.com", "https://twitter.com", "facebook.com",
            "https://tiktok.com")

for website in websites:
  if website.startswith("https://"):
    print("good to go")
  else:
    print("we have to fix it")

for website in websites:
  if not website.startswith("https://"):
    print("we have to fix it")

results = {}

for website in websites:
  if not website.startswith("https://"):
    website = f"https://{website}"
  response = get(website)
  if response.status_code >= 200 and response.status_code <= 299:
    results[website] = "OK"
  elif response.status_code >= 300 and response.status_code <= 399:
    results[website] = "Redirection"
  else:
    results[website] = "FALIED"
print(results)


class Puppy:
  def __init__(self):
   self.name = "Ruffus"
   self.age = 0.1
   self.breed = "beegle" 

ruffus = Puppy()
bibi = Puppy()
print(ruffus.name, bibi.name) #둘은 동일하게 같은걸 갖고 있음  self로 자기자신을 불러오기때문 




class Puppy:
  def __init__(self,name,breed):
   self.name = name
   self.age = 0.1
   self.breed = breed

ruffus = Puppy( name = "Ruggus",breed = "Beagle")

bibi = Puppy("Bibi","Dalathian")

print(ruffus.name, bibi.name)

#루푸스 이름과 비비이름이 설정된후 출력


class Puppy:
  def __init__(self,name,breed):
   self.name = name
   self.age = 0.1
   self.breed = breed

  def __str__(self):
    return f"{self.breed} named puppy is{self.name}"

ruffus = Puppy( name = "Ruffus",breed = "Beagle")
bibi = Puppy("Bibi","Dalathian")
print(ruffus, bibi) #__str__메소드가 들어가면 굳이 프린트에 메소드를 넣지 않아도 모든정보를 가져올 수 있음 ( __str__ 자동으로 불러와주는 메소드)

from typing import get_args


class Dog:

  def __init__(self, name, breed, age):
    self.name = name
    self.breed = breed
    self.age = age

  def sleep(self):
    print("zzzzzz.......")


class GuardDog(Dog):

  def __init__(self, name, breed):
    super().__init__(
        name,
        breed,
        5,
    )
    self.agrresive = True #Dog 클래스와 별개로 다른 property를 가질 수있음
    
  def rrrrr(self):
    print("stay away")


class Puppy(Dog):

  def __init__(self, name, breed):
    super().__init__(
        name,
        breed,
        0.1,
    )
    self.spoiled = True#Dog 클래스와 별개로 다른 property를 가질 수있음

  
  #  self.name = name
  #  self.age = 0.1
  #  self.breed = breed

  # def __str__(self):
     # return f"{self.breed} named puppy is {self.name}"

  def woof_woof(self):
    print("woof woof")

  # def introduce(self):
  #   self.woof_woof()
  #   print(f"my name is {self.name} and I'm a baby {self.breed}")
  #   self.woof_woof()


ruffus = Puppy(name="Ruffus", breed="Beagle")
bibi = GuardDog("Bibi", "Dalathian")
print(ruffus, bibi)

# bibi.introduce() # __str__메소드가 들어가면 굳이 프린트에 메소드를 넣지 않아도 모든정보를 가져올 수 있음 ( __str__ 자동으로 불러와주는 메소드)

ruffus.woof_woof()
bibi.rrrrr()

ruffus.sleep()

"""

# class Player:

#   def __init__(self, name, team):
#     self.name = name
#     self.xp = 1500
#     self.team = team

#   def introduce(self):
#     print(f"hello I`m {self.name} and I play for {self.team}")

# class Team:

#   def __init__(self, team_name):
#     self.team_name = team_name
#     self.players = []

#   def show_players(self):
#     for player in self.players:
#       player.introduce()

#   def add_player(self, name):
#     new_player = Player(name, self.team_name)
#     self.players.append(new_player)

# team_x = Team("Team X")

# teamtest = team_x.add_player("nico")

# team_x.show_players()

# team_blue = Team("Blue Team")

# team_blue.add_player("lynn")

# team_blue.show_players()

# 팀에서 플레이어를 리무브 하는법을 해보기

import webscrape



from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import time

class JobScraper:
    def __init__(self, url, scroll_count=5, scroll_pause=5):
        self.url = url
        self.scroll_count = scroll_count
        self.scroll_pause = scroll_pause
        self.jobs_db = []

    def fetch_page_content(self):
        """Playwright를 사용하여 페이지 콘텐츠를 가져옵니다."""
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False)
            page = browser.new_page()
            page.goto(self.url)

            # 페이지 스크롤
            for _ in range(self.scroll_count):
                time.sleep(self.scroll_pause)
                page.keyboard.down("End")
            
            time.sleep(self.scroll_pause)
            content = page.content()
            browser.close()
        return content

    def parse_jobs(self, content):
        """BeautifulSoup을 사용하여 HTML에서 잡 정보를 추출합니다."""
        soup = BeautifulSoup(content, "html.parser")
        jobs = soup.find_all("div", class_="JobCard_container__REty8")
        for job in jobs:
            link = f"https://www.wanted.co.kr/{job.find('a')['href']}"  # 링크 추출
            title = job.find("strong", class_="JobCard_title__HBpZf").text
            company_name = job.find("span", class_="JobCard_companyName__N1YrF").text
            reward = job.find("span", class_="JobCard_reward__cNlG5").text
            self.jobs_db.append({
                "title": title,
                "company_name": company_name,
                "reward": reward,
                "link": link
            })

    def scrape_jobs(self):
        """잡 스크래핑의 전체 프로세스를 실행합니다."""
        content = self.fetch_page_content()
        self.parse_jobs(content)
        return self.jobs_db

# 실행 코드
if __name__ == "__main__":
    scraper = JobScraper(url="https://www.wanted.co.kr/search?query=flutter&tab=position")
    jobs = scraper.scrape_jobs()
    print(jobs)
    print(f"Total jobs scraped: {len(jobs)}")
