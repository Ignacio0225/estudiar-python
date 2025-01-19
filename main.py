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

"""
