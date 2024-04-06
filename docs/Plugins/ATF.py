input("Enter username")
username = input("Enter username: ")
headers = {"user-agent":"Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/112.0"}
atf_url = "https://booru.allthefallen.moe/"
tag_url = "/posts?tags=ordfav%3A"
url = f"{atf_url}{tag_url}{username}"
import datetime
import json
import os
import re
import requests
import urllib.request
from zipfile import ZipFile
from bs4 import BeautifulSoup as bs
image_name = 0

def Saving(direct_link):
  # Сохранение
  # I could do without global, but I'm lazy.  
  global image_name
  image_name = image_name + 1

  def rename(direct_link):
    last_dot_index = direct_link.rfind('.')
    if last_dot_index != -1:
        return direct_link[last_dot_index + 1:]
    else:
        return direct_link
  image = rename(direct_link)
  image = f"{image_name}.{image}"
  with ZipFile(f"{username}.zip", "a") as myzip:
    urllib.request.urlretrieve(direct_link, image)
    myzip.write(image)
    os.remove(image)
  myzip.close()
  print(f"{image_name}: {direct_link}")

def Getting_Direct_Link(img_urls):
  # Получение прямой ссылки
  request = requests.get(img_urls, headers=headers)
  soup = bs(request.text, "html.parser")
  # Проверка формата
  direct_link = soup.find("img", id="image")
  if direct_link is not None:
      direct_link = direct_link.get("src")
  if direct_link == None:
      direct_link = soup.find("video", id="image")
      if direct_link is not None:
          direct_link = direct_link.get("src")
  # tag = soup.find_all("li", class_="tag-type-0")
  # for tags in tag:
  #     if tags is not None:
  #         tags = tags.get("data-tag-name")
  #         all_tags = all_tags + tags
  Saving(direct_link)
def Getting_Links_New_Page(url):
  # Получение ссылки на новую страницу
    request = requests.get(url, headers=headers)
    soup = bs(request.text, "html.parser")
    up_url = soup.find_all("div", class_="paginator")
    for up_urls in up_url:
        up_urls = up_urls.find("a", class_="paginator-next")
        if up_urls is not None:
            up_urls = up_urls.get("href")
            url = atf_url + up_urls
            Getting_Links_IMG(url)
def Getting_Links_IMG(url):
  # Получение ссылок на картинки 
    request = requests.get(url, headers=headers)
    soup = bs(request.text, "html.parser")
    img_url = soup.find_all("div", class_="post-preview-container")
    for img_urls in img_url:
        img_urls = img_urls.find("a")
        if img_urls is not None:
            img_urls = img_urls.get("href")
            img_urls = atf_url + img_urls
            Getting_Direct_Link(img_urls)
    Getting_Links_New_Page(url)
Getting_Links_IMG(url)