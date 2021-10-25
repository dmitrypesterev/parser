import os
import eel
import requests 
import json
from bs4 import BeautifulSoup as bs 

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 5.1; rv:47.0) Gecko/20100101 Firefox/47.0",
    "Accept": "text/html,aplication/xhtml+xml,aplication/xml;q=0.9,*/*;q=0.8"
}

# @eel.expose
# def get_list():
#     b_url = "https://bloha.ru/editorial/yemodzi-znacheniya-vsekh-2776-smaylikov-na-ay/"
#     emojies = []

#     session = requests.Session()
#     request = session.get(b_url, headers=headers)

#     if (request.status_code == 200):
#         soup = bs(request.content, "lxml")
#         emoji_table = soup.find_all("table")[0]
#         emoji_table2 = soup.find_all("table")[1]

#         trs = emoji_table.find_all("tr")
#         trs2 = emoji_table2.find_all("tr")

#         def get_info (trs): 
#             for tr in trs[1:]:
#                 try:
#                     title = tr.findAll("h5")[2].get_text()
#                 except: 
#                     title = ""
                
#                 src = tr.find_all("img")[0]['data-src']

#                 emoji_id = src.split('/')[-1][0:-4]
#                 img = src

#                 emojies.append({
#                     "id": emoji_id,
#                     "name": title,
#                     "translate": title,
#                     "img": img,
#                     "group": ""
#                 })

#         get_info(trs)
#         get_info(trs2)
    
#     return emojies



@eel.expose
def get_list():
    file = open('allemojies.json', encoding='utf-8')
    allemojies = json.load(file)

    return allemojies

@eel.expose
def get_app_list():
    file = open('emojies.json', encoding='utf-8')
    emojies = json.load(file)

    return emojies



@eel.expose
def save_emojies(emojies):
    with open('emojies.json', 'w', encoding='utf-8') as json_file:
        json_file.write(emojies)


