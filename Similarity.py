import numpy as np


def cal_similarity(list1, list2, match_score=1, mismatch_penalty=-1, gap_penalty=-3):
    score = np.zeros((len(list1) + 1, len(list2) + 1), dtype=int)

    for i in range(1, len(list1) + 1):
        for j in range(1, len(list2) + 1):
            if list1[i - 1] == list2[j - 1]:
                match = score[i - 1][j - 1] + match_score
                score[i][j] = max(0, match.real)
            else:
                mismatch = score[i - 1][j - 1] + mismatch_penalty
                gap1 = score[i][j - 1] + gap_penalty
                gap2 = score[i - 1][j] + gap_penalty
                score[i][j] = max(0, mismatch.real, gap1.real, gap2.real)

    max_score = np.max(score)

    return max_score / max(len(list1), len(list2))


seq1 = 'AGGTTTTTTTTGCAGTTCAGATTCTACTGACTGTGTATCAAACAAAGTGAGCATCCAGCCTCTGGATGAAACTGCTGTCACAGATAAAGAGAACAATCTGCATGAATCAGAGTATGGTGA'
seq2 = 'AGGTTTTTTTGCAGTTCAGATTCTACTGACTGTGTATCAAACAAAGTGAGCATCCAGCCTCTGGATGAAACTGCTGTCACAGATAAAGAGAACAATCTGCATGAATCAGAGTATGGAGA'

str1 = "I want to perform sequence alignment using BLAST provided by NCBI."
str2 = "I want to perform sequence alignment using BLAST provided by CNCB."

similarity = cal_similarity(seq1, seq2)
print(f'相似度：{similarity}')

similarity = cal_similarity(str1.split(' '), str2.split(' '))
print(f'相似度：{similarity}')
