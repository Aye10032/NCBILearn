import os.path

from Bio import SeqIO
from loguru import logger

logger.add('../log/run_time.log')


def read_fastq(input_path):
    if not os.path.isfile(input_path):
        logger.warning('Error input format')

    with open(input_path, 'r') as file:
        records = list(SeqIO.parse(file, 'fastq'))[:10]

        for record in records:
            length = len(record.seq)

            avg_quality = sum(record.letter_annotations['phred_quality']) / length

            gc_content = (record.seq.count('G') + record.seq.count('C')) / length * 100

            logger.info(f'Length: {length}')
            logger.info(f'Avg Quality: {avg_quality}')
            logger.info(f'GC Content: {gc_content}%')

    file.close()


if __name__ == '__main__':
    read_fastq('H1_1.fq')
