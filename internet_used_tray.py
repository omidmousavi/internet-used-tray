import pystray
from PIL import Image, ImageDraw
import subprocess
import json 
import math
import time
import threading


def convert_size(size_bytes):
   if size_bytes == 0:
       return "0B"
   size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
   i = int(math.floor(math.log(size_bytes, 1024)))
   p = math.pow(1024, i)
   s = round(size_bytes / p, 2)
   return "%s %s" % (s, size_name[i])

def create_image(width, height, color1, color2):
    # Generate an image and draw a pattern
    image = Image.new('RGB', (width, height), color1)
    dc = ImageDraw.Draw(image)
    dc.rectangle(
        (width // 2, 0, width, height // 2),
        fill=color2)
    dc.rectangle(
        (0, height // 2, width // 2, height),
        fill=color2)

    return image

def test():
    print("test")

def get_internet_used():
    result = subprocess.run(['vnstat', '-i', 'wlp3s0', '--json', 'd', '1'], stdout=subprocess.PIPE)
    result = result.stdout.decode('utf-8')

    json_result = json.loads(result)

    day_rx = json_result["interfaces"][0]["traffic"]["day"][0]["rx"]
    day_tx = json_result["interfaces"][0]["traffic"]["day"][0]["tx"]

    return convert_size(day_rx+day_tx)


def t1():    
    global icon
    icon.run()

def t2():
    while True:
        menu_items.pop()
        menu_items.append(pystray.MenuItem(text='Total internet used : ' + get_internet_used(), action=test))
        icon.update_menu()
        time.sleep(10)


menu_items = [pystray.MenuItem(text='Total internet used : ', action=test)]

icon = pystray.Icon(" ", icon=create_image(64, 64, '#000', '#fff'), menu=pystray.Menu(lambda: menu_items))

t1 = threading.Thread(target=t1, args=[])
t2 = threading.Thread(target=t2, args=[])

t1.start()
t2.start()
