import argparse
import pandas as pd
from nltk.corpus import stopwords


class OpinionDetector:
    def __init__(self, dataset_file):
        dataset = [['Review', 'Score']]
        with open(dataset_file) as f:
            for line in f.readlines():
                line = line.strip('\n')
                review = line[:-2] if line[-2].isdigit() else line[:-1]
                score = line[-2:] if line[-2].isdigit() else line[-1:]
                dataset.append([review, score])
            # self.my_df = pd.read_csv(dataset_file, dtype=str, delimiter="\n", header=None)
        self.my_df = pd.DataFrame(dataset[1:], columns=dataset[0])


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Specify import file containing Corpus to analyze')
    parser.add_argument('-i', '--import_from', help='File to import from')
    args = parser.parse_args()
    if args.import_from:
        corpus_file = args.import_from
    else:
        corpus_file = input()
        # corpus_file = 'SAR14.txt'
    corpus = OpinionDetector(corpus_file)
    print(corpus.my_df.head())
    print(corpus.my_df.tail())


