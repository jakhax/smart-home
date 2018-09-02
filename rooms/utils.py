import json
def get_home_data():
    with open('rooms/home_architecture.json','r') as rm:
        data=json.load(rm)
    return data

def get_rooms():
    data=get_home_data()
    return [i['name']['text'] for i in data["rooms"]]

def get_nb_icons():
    with open('rooms/nb-icons.txt') as ic:
        icons_list=ic.read().split('\n')
    return icons_list