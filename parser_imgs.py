import os
import eel
import requests 
import json

from bs4 import BeautifulSoup as bs 
IMGS_FOLDER = "imgs/"


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 5.1; rv:47.0) Gecko/20100101 Firefox/47.0",
    "Accept": "text/html,aplication/xhtml+xml,aplication/xml;q=0.9,*/*;q=0.8"
}

emojies = []

def get_list():
    b_url = "https://bloha.ru/editorial/yemodzi-znacheniya-vsekh-2776-smaylikov-na-ay/"
    imgs = []
    emojies = []
    session = requests.Session()
    request = session.get(b_url, headers=headers)

    if (request.status_code == 200):
        soup = bs(request.content, "lxml")
        emoji_table = soup.find_all("table")[0]
        emoji_table2 = soup.find_all("table")[1]

        trs = emoji_table.find_all("tr")
        trs2 = emoji_table2.find_all("tr")

        def get_info (trs): 
            for tr in trs[1:]:
                try:
                    title = tr.findAll("h5")[2].get_text()
                except: 
                    title = ""
                
                src = tr.find_all("img")[0]['data-src']

                emoji_id = src.split('/')[-1][0:-4]
                img = src

                emojies.append({
                    "id": emoji_id,
                    "name": title,
                    "img": img
                })

        get_info(trs)
        get_info(trs2)
    
    return emojies

emojies = get_list()

def get_file(url):
    response = requests.get(url, stream=True)
    return response

def save_data(name, file_data):
    file = open(IMGS_FOLDER + name , 'bw') #Бинарный режим, изображение передається байтами
    for chunk in file_data.iter_content(4096): # Записываем в файл по блочно данные
        file.write(chunk)

def get_name(url):
    name = url.split('/')[-1]
    return name


for emoji in emojies:
    save_data(get_name(emoji["img"]), get_file(emoji["img"]))


with open('emojies.json', 'w', encoding='utf-8') as json_file:
    json.dump(emojies, json_file, indent=4, sort_keys=True, ensure_ascii=False)

print(emojies) 