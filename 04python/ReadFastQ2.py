import os.path

from loguru import logger

logger.add('../log/run_time.log')


def read_fastq(input_path, output_path):
    if not os.path.isfile(input_path) or not os.path.isfile(output_path):
        logger.warning('Error input format')

    with open(input_path, 'r') as file:
        with open(output_path, 'a') as output:
            for _ in range(10):
                for i in range(4):
                    line = file.readline()

                    if i == 1:
                        logger.debug(line)
                        length = len(line)
                        gc_content = (line.count('G') + line.count('C')) / length * 100

                        logger.info(f'Length: {length}')
                        logger.info(f'GC Content: {gc_content}%')

                        output.write(f'Length: {length}\n')
                        output.write(f'GC Content: {gc_content}%\n')

                    if i == 3:
                        logger.debug(line)
                        quality_list = [ord(c) - 33 for c in line]
                        avg_quality = sum(quality_list) / len(line)

                        logger.info(f'Avg Quality: {avg_quality}')

                        output.write(f'Avg Quality: {avg_quality}\n')

        output.close()

    file.close()


if __name__ == '__main__':
    read_fastq('H1_1.fq', '../output/result.txt')
