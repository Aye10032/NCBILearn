from io import StringIO

from Bio import Entrez, SeqIO

# 设置NCBI访问邮箱
Entrez.email = "aye10032@gmail.com"

# 搜索并下载符合条件的结果序列
handle = Entrez.esearch(db="nucleotide", term="(H3[Text Word] NOT N2[Text Word]) NOT homo sapiens[Organism]", retmax=100)
search_results = Entrez.read(handle)
handle.close()

# 获取符合条件的结果的详细信息
id_list = search_results['IdList']
handle = Entrez.efetch(db="nucleotide", id=id_list, rettype="fasta", retmode="text")
results = handle.read()
handle.close()

# 进一步筛选符合 segment 和 country 条件的序列
filtered_sequences = []
gb_records = SeqIO.parse(StringIO(results), "genbank")
for record in gb_records:
    segment = None
    country = None

    # 寻找 FEATURES 部分中的 segment 和 country
    for feature in record.features:
        print(feature)
        if feature.type == "source":
            if "segment" in feature.qualifiers:
                segment = feature.qualifiers["segment"][0]
            if "country" in feature.qualifiers:
                country = feature.qualifiers["country"][0]

    # 如果符合条件，则保留序列
    if segment == "4" and country == "USA":
        filtered_sequences.append(record)

# 打印筛选结果
for record in filtered_sequences:
    print(record.id, record.description)
    print(record.seq)
    print("------")