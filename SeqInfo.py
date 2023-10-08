from Bio import Entrez, SeqIO

# 设置邮箱
Entrez.email = 'aye10032@gmail.com'

handle = Entrez.esearch(db='nucleotide', term='LBML01000000')
record = Entrez.read(handle, "genbank")

handle = Entrez.efetch(db='nucleotide', id=record['IdList'][0], rettype='gb', retmode='text')
seq = SeqIO.read(handle, 'genbank')
