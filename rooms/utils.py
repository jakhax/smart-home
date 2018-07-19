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

def serialize_devices(devices):
    fdata=[{"id":i.id,"device_type":i.device_type.id,"room":i.room,"name":i.name,"state":i.pin.default_state} for i in devices]
    return json.dumps(fdata)