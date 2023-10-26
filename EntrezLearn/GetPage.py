import requests
from bs4 import BeautifulSoup

# 目标网页的URL
url = 'https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8570536/'

# 发起请求并获取响应内容
response = requests.get(url)
html_content = response.content

# 打开本地HTML文件
# filename = 'D:/program/python/NCBILearn/art.html'
# with open(filename, 'r', encoding='utf-8') as file:
#     html_content = file.read()

soup = BeautifulSoup(html_content, 'html.parser')

data_block = (soup.find('div', id='mc')
              .find('div', class_='jig-ncbiinpagenav')
              .find('div', id='ass-data')
              .find('dd', id='data-avl-stmnt'))
if data_block:
    _url = data_block.find('a')['href'] if data_block.find('a') else 'no'
    print(_url)
