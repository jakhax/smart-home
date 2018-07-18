def get_gpio_pins():
    pin_list=[]
    with open('raspberry/GPIO_pins.txt') as ic:
        data=ic.read()
    for i in data.split('\n'):
        try:
            pin_list.append(int(i))
        except:
            pass
    return pin_list