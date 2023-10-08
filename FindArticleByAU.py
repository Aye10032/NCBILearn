import requests
from Bio import Entrez, SeqIO, Medline
from bs4 import BeautifulSoup

pmc_list = []
pm_list = []
# 设置Entrez参数
Entrez.email = 'aye10032@gmail.com'
db = 'PMC'


def get_articles():
    global pmc_list, pm_list

    search_term = ('(Sun, Luyang[Full Author Name]) AND '
                   '('
                   '(Auburn University[Affiliation]) OR '
                   '(Baylor College of Medicine[Affiliation]) OR '
                   '(Qingdao Institute of Bioenergy and Bioprocess Technology[Affiliation])'
                   ') AND '
                   '(\"2013-01-01\"[Publication Date] : \"3000\"[Publication Date])')

    handle = Entrez.esearch(db=db, term=search_term)
    record = Entrez.read(handle)
    handle.close()

    pmc_list = record['IdList']

    with open('output.txt', 'a') as _file:
        for pmc in pmc_list:
            handle = Entrez.efetch(db=db, id=pmc, rettype='medline', retmode='text')
            article = Medline.read(handle)
            handle.close()

            pm_list.append(article['PMID'])
            _file.write(article['TI'] + '\n')
            _file.write(f'PMC:{pmc}\n')
            _file.write('PubMed:' + article['PMID'] + '\n')
            _file.write(article['AID'][0] + '\n\n')


def get_seq_database():
    global pmc_list
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    for pmc_id in pmc_list:
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


if __name__ == '__main__':
    with open('output.txt', 'a') as file:
        file.write('过去10年内发表文章:\n\n')

    get_articles()
    get_seq_database()
