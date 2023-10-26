from Bio import Entrez, Medline

# 设置Entrez参数
Entrez.email = 'aye10032@gmail.com'
db = 'PMC'
search_term = '\"Altered Chromatin States Drive Cryptic Transcription in Aging Mammalian Stem Cells\"'

# 搜索文章
handle = Entrez.esearch(db=db, term=search_term)
record = Entrez.read(handle)

# 获取文章摘要记录
record_ids = record['IdList']
handle = Entrez.efetch(db=db, id=record_ids[0], rettype='medline', retmode='text')
article = Medline.read(handle)

# 提取所需信息
authors = article.get('AU', [])
affiliations = article.get('AD', [])
publication_date = article.get('DP', '')

# 打印结果
print('Authors: ', ', '.join(authors))
print('Affiliations: ', affiliations)
print('Publication Date: ', publication_date)
print(article['AB'])
