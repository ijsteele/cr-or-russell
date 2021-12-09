import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox import service
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
import time

s=Service(GeckoDriverManager().install())

url = 'https://udel.campusdish.com/LocationsAndMenus/CaesarRodneyFreshFoodCompany'

browser = webdriver.Firefox(service=s)
browser.get(url=url)
time.sleep(3)
html = browser.page_source
soup = BeautifulSoup(html, 'html.parser')
meal_ids = soup.findAll("svg",class_='sc-fTQvRK jqTRnq check-plus')

meals = []
for meal_id in meal_ids:
    meal = meal_id.find('title').get('id')
    meals.append(meal[meal.find('_')+1:meal.rfind('_')])
print(meals)
print(len(meals))

# TODO: create json file and add the GET json response from each meal id
# TODO: add menus of other locations
    
browser.close()