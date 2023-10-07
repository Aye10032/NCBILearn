import requests
from Bio import Entrez, SeqIO
from bs4 import BeautifulSoup

article_list = []
# 设置Entrez参数
Entrez.email = 'aye10032@gmail.com'
db = 'PMC'


def get_articles():
    global article_list
    search_term = ('(Sun, Luyang[Full Author Name]) AND '
                   '('
                   '(Auburn University[Affiliation]) OR '
                   '(Baylor College of Medicine[Affiliation]) OR '
                   '(Qingdao Institute of Bioenergy and Bioprocess Technology[Affiliation])'
                   ') AND '
                   '(\"2013-01-01\"[Publication Date] : \"3000\"[Publication Date])')

    handle = Entrez.esearch(db=db, term=search_term)
    record = Entrez.read(handle)

    article_list = record['IdList']

    print(article_list)


def get_seq_database():
    global article_list
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    for pmc_id in article_list:
        url = f'https://www.ncbi.nlm.nih.gov/pmc/articles/PMC{pmc_id}/'
        print(url)

        response = requests.get(url, headers=headers)
        html_content = response.content
        soup = BeautifulSoup(html_content, 'html.parser')

        try:
            data_block = (soup.find('div', id='mc')
                          .find('div', class_='jig-ncbiinpagenav')
                          .find('div', id='ass-data')
                          .find('dd', id='data-avl-stmnt'))

            _url = data_block.find('a')['href']
            print(_url)
        except AttributeError:
            print('no')

        print()


get_articles()
get_seq_database()
