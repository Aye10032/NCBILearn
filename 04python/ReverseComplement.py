import os
from loguru import logger

complement_dict = {'A': 'T',
                   'T': 'A',
                   'C': 'G',
                   'G': 'C',
                   'a': 't',
                   't': 'a',
                   'c': 'g',
                   'g': 'c'}


def reverse_complement_sequence(input_data):
    _reverse_complement = ''

    if os.path.isfile(input_data):
        with open(input_data, 'r') as file:
            sequence = file.read().strip().replace('\n', '').replace(' ', '')
    else:
        sequence = input_data

    for base in sequence[::-1]:
        _reverse_complement += complement_dict[base]

    return _reverse_complement


if __name__ == "__main__":
    reverse_complement = reverse_complement_sequence('ACTAGC')
    logger.info(f'Reverse complement sequence: {reverse_complement}')

    reverse_complement = reverse_complement_sequence('seq.txt')
    logger.info(f'Reverse complement sequence: {reverse_complement}')
