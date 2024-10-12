from bs4 import BeautifulSoup
from selenium import webdriver
import requests 

url = "https://albert.nyu.edu/albert_index.html"
page = requests.get(url)
soup = BeautifulSoup(page.text, "html")
print(soup)

username = "cw4483"
password = "password"
driver = webdriver.Chrome()
