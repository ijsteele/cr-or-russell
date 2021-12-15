import schedule
import time
import re
from bs4 import BeautifulSoup
import requests

def get_cr_menu():
    '''
    This gets the menu from CR
    :return:
        A list of strings
        a list of the items from the dining hall. Each item is a string
    '''
    import json

    url = "https://udel.campusdish.com/LocationsAndMenus/CaesarRodneyFreshFoodCompany"

    result = requests.get(url)
    doc = BeautifulSoup(result.text, "html.parser")

    source = doc.prettify()

    m = re.search("model: ({.*})", source)
    model = m.group(1)
    json = json.loads(model)

    todays_food_items = []

    for item in range(0, len(json['Menu']['MenuProducts'])):
        todays_food_items.append(json['Menu']['MenuProducts'][item]['Product']['MarketingName'])

    return todays_food_items


def get_russle_menu():
    '''
    This gets the menu from Russle dinding hall

    :return:
        A list of strings.
        A list of the items from the dining hall. Each item is a string
    '''
    import json
    url = "https://udel.campusdish.com/LocationsAndMenus/RussellDiningHall"

    result = requests.get(url)
    doc = BeautifulSoup(result.text, "html.parser")

    source = doc.prettify()

    m = re.search("model: ({.*})", source)
    model = m.group(1)
    json = json.loads(model)

    todays_food_items = []

    for item in range(0, len(json['Menu']['MenuProducts'])):
        todays_food_items.append(json['Menu']['MenuProducts'][item]['Product']['MarketingName'])

    return todays_food_items


def get_pencader_menu():
    '''
    This gets the menu from pencader
    :return:
        A list of strings
        A list of the items on the menu
    '''
    import json
    url = "https://udel.campusdish.com/LocationsAndMenus/PencaderDiningHall"

    result = requests.get(url)
    doc = BeautifulSoup(result.text, "html.parser")
    source = doc.prettify()

    m = re.search("model: ({.*})", source)
    model = m.group(1)
    json = json.loads(model)

    todays_food_items = []

    for item in range(0, len(json['Menu']['MenuProducts'])):
        todays_food_items.append(json['Menu']['MenuProducts'][item]['Product']['MarketingName'])

    return todays_food_items

def get_all_menus():
    '''
    This function scrapes the web and gets all of the menus for the dining halls.
    Args:
        N/A
    returns:
        A list of the dining hall lists. The first element in the list is the menu at CR, the
        second element is the menu at Russle, the third is the menu at Pencader. It is a list
        of lists of strings
    '''
    cr_menu = get_cr_menu()
    russle_menu = get_russle_menu()
    pencader_menu = get_pencader_menu()
    print("i did a thing")

    return [cr_menu, russle_menu, pencader_menu]



schedule.every().day.at("06:00").do(get_all_menus)
schedule.every().day.at("16:00").do(get_all_menus)

while True:
    schedule.run_pending()
    time.sleep(50)# wait ten seconds
