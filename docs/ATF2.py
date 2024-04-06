import os
import re
import time
import json
import smtplib
import requests
import datetime
import urllib.request
from zipfile import ZipFile
from threading import Thread
from bs4 import BeautifulSoup as bs
from email.message import EmailMessage

DATA =  open('docs/JSON/DATA.json', 'r')
DATA = json.load(DATA)

headers = DATA["headers"]
atf_id = DATA["variables"]["atf_id"]
atf_user_name = DATA["ATF"]["atf_user_name"]
atf = DATA["ATF"]["atf"]
atf_user_id = DATA["ATF"]["atf_user_id"]
atf_user_id = f'{atf_user_id}{atf_id}'
atf_user_id_fullLink = f'{atf}{atf_user_id}'

request = requests.get(atf_user_id_fullLink, headers=headers)
soup = bs(request.text, "html.parser")
user_name = soup.find("a", class_="user user-member")
if user_name is not None:
    user_name = user_name.get("data-user-name")

atf_user_name_fullLink = f'{atf}{atf_user_name}{user_name}'
url = atf_user_name_fullLink

def getting_direct_links_pictures(full_picture_links):
    request = requests.get(full_picture_links, headers=headers)
    status_code = request.status_code
    if status_code == 200:
        soup = bs(request.text, "html.parser")
        direct_link = soup.find("a", class_="image-view-original-link")
        if direct_link is not None:
            direct_link = direct_link.get("href")
        elif direct_link == None:
            direct_link = soup.find("img", id="image")
            if direct_link is not None:
                direct_link = direct_link.get("src")
            elif direct_link == None:
                direct_link = soup.find("video", id="image")
                if direct_link is not None:
                    direct_link = direct_link.get("src")
    print(direct_link)
    
    else:
        time.sleep(2)
        return getting_direct_links_pictures(full_picture_links)

def getting_links_pictures(url):
    request = requests.get(url, headers=headers)
    soup = bs(request.text, "html.parser")
    picture_link = soup.find_all("a", class_="post-preview-link")
    for picture_links in picture_link:
        if picture_links is not None:
            picture_links = picture_links.get("href")
            full_picture_links = f'{atf}{picture_links}'
            print(full_picture_links)
            flow = Thread(target=getting_direct_links_pictures, args=(full_picture_links,))
            flow.start()
            time.sleep(2)

def linking_new_page(url):
    pass

getting_links_pictures(url)

