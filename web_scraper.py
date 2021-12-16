import schedule
import time
import re
from bs4 import BeautifulSoup
import requests
from google_sheet import records_data



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
        data = json['Menu']['MenuProducts'][item]['Product']
        item_dict = {'name': data['MarketingName'], 'ContainsEggs': data['ContainsEggs'], 'ContainsFish': data['ContainsFish'], 'ContainsMilk': data['ContainsMilk'], 'ContainsPeanuts': data['ContainsPeanuts'], 'ContainsShellfish': data['ContainsShellfish'],
                     'ContainsSoy': data['ContainsSoy'], 'ContainsTreeNuts': data['ContainsTreeNuts'], 'ContainsWheat': data['ContainsWheat'], 'IsGlutenFree': data['IsGlutenFree'], 'IsHalal': data['IsHalal'], 'IsVegan': data['IsVegan'], 'IsVegetarian': data['IsVegetarian']}
        todays_food_items.append(
            item_dict)
    return todays_food_items


def get_russell_menu():
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
        data = json['Menu']['MenuProducts'][item]['Product']
        item_dict = {'name': data['MarketingName'], 'ContainsEggs': data['ContainsEggs'], 'ContainsFish': data['ContainsFish'], 'ContainsMilk': data['ContainsMilk'], 'ContainsPeanuts': data['ContainsPeanuts'], 'ContainsShellfish': data['ContainsShellfish'],
                     'ContainsSoy': data['ContainsSoy'], 'ContainsTreeNuts': data['ContainsTreeNuts'], 'ContainsWheat': data['ContainsWheat'], 'IsGlutenFree': data['IsGlutenFree'], 'IsHalal': data['IsHalal'], 'IsVegan': data['IsVegan'], 'IsVegetarian': data['IsVegetarian']}
        todays_food_items.append(
            item_dict)
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
        data = json['Menu']['MenuProducts'][item]['Product']
        item_dict = {'name': data['MarketingName'], 'ContainsEggs': data['ContainsEggs'], 'ContainsFish': data['ContainsFish'], 'ContainsMilk': data['ContainsMilk'], 'ContainsPeanuts': data['ContainsPeanuts'], 'ContainsShellfish': data['ContainsShellfish'],
                     'ContainsSoy': data['ContainsSoy'], 'ContainsTreeNuts': data['ContainsTreeNuts'], 'ContainsWheat': data['ContainsWheat'], 'IsGlutenFree': data['IsGlutenFree'], 'IsHalal': data['IsHalal'], 'IsVegan': data['IsVegan'], 'IsVegetarian': data['IsVegetarian']}
        todays_food_items.append(
            item_dict)
    return todays_food_items


def get_all_menus():
    '''
    This function scrapes the web and gets all of the menus for the dining halls.
    Args:
        N/A
    returns:
        A list of the dining hall lists. The first element in the list is the menu at CR, the
        second element is the menu at Russle, the third is the menu at Pencader. It returns a list
        of lists of dictionaries
    '''
    cr_menu = get_cr_menu()
    russle_menu = get_russell_menu()
    pencader_menu = get_pencader_menu()

    return [cr_menu, russle_menu, pencader_menu]

def find_best_place():
    all_menus = get_all_menus()
    

    dining_centers = {'cr':0,'russell':0,'pencader':0}
    n = 0
    for dining_hall in all_menus:
        n += 1
        for food in dining_hall:
            for record in records_data:
                if food['name'] in record:
                    if isinstance(record[food['name']], int):
                        
                        if n == 1:
                            dining_centers['cr'] += record[food['name']]
                        elif n == 2:
                            dining_centers['russell'] += record[food['name']]
                        else:
                            dining_centers['pencader'] += record[food['name']]


    if max(dining_centers.values()) == 0:
        return 'None of the dining centers suit you. Do a meal Exchange'
    max_value = max(dining_centers.values())

    res = []
    for key in dining_centers:
        if dining_centers[key] == max_value:
            res.append(key)
    return res


# schedule.every().day.at("06:00").do(find_best_place)
# schedule.every().day.at("16:00").do(find_best_place)

# while True:
#     schedule.run_pending()
#     time.sleep(50)  # wait fifty seconds

