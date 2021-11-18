import argparse
import string
import pandas as pd
from nltk import pos_tag
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer


class OpinionDetector:

    wnl = WordNetLemmatizer()
    sw = stopwords.words('english')
    punctuation = list(string.punctuation)

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

    def create_lemma_column(self):
        self.my_df['Lemmas'] = self.my_df['Review'].apply(lambda x: self.text_processor(x))

    def text_processor(self, text):
        word_list = word_tokenize(text.lower())  # Lists individual words
        word_list = self.clean_list(word_list)  # remove stop words and punctuation
        word_list = self.pos_sort(word_list)  # filters out only selected pos
        word_list = self.lemmatizer(word_list)  # converts to a dictionary form of lemma
        print(word_list[:7])
        return word_list

    @staticmethod
    def lemmatizer(words):
        wnl = WordNetLemmatizer()
        lemmatized = list()
        for word in words:
            lemmatized.append(wnl.lemmatize(word))
        return lemmatized

    @staticmethod
    def clean_list(words: list):
        return [word for word in words if (word not in OpinionDetector.sw)
                and (word not in OpinionDetector.punctuation)]

    @staticmethod
    def pos_sort(words, part_of_speech='NN'):
        return [word for word in words if pos_tag([word])[0][1] == part_of_speech]


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
    corpus.create_lemma_column()
    print(corpus.my_df['Lemmas'].head())
    print(corpus.my_df['Lemmas'].tail())
