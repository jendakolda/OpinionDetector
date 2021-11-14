from hstest import StageTest, TestCase, CheckResult, WrongAnswer
import os

SAR_sample = """" Space . It is the best Bond movie forever . The space is excellent " ,10
" defines the 80 's . this is a classic . if you havent seen this movie you are missing out . " ,10
" Great Aviation movie . That 's all I could say . Great aviation movie if you are a pilot ! " ,10
" Pure genius . . Rent . Watch . Worship . Repeat . " ,10
" Yesss . The Best movie I saw in my all life Great actors Great Story just Great ... " ,10
" great movie . Great story and great action ! Needless to say anything beyond this !! " ,10
" groovy ... . It was very good . I laughed all the time . And it was frightening too . . " ,8
" Why ? . Why , oh why , oh why ? " ,1
" Two words : . Headache-inducing ! " ,1
" Very Good ! . This was a very entertaining movie.The locations were beautiful . " ,10
" Film 1 star , Actress 10 stars . . Emily Watson gets 10 stars ! " ,1
" Beautiful , touching . A real tear-jerker . Love that Meg . ` nuff said . An 8 . " ,8
" Awful . Totally unworthy of Meg Ryan and Nicholas Cage -- boring and predictible . " ,3
" Spectacular . Spectacular , loved it ! Was Laughing almost through the entire movie . " ,10
" A great movie . An absolute visual feast . Disturbing , and unusual . Perfect . " ,10
" UG . A Review ? That 's Easy . One word : POINTLESS ! " ,3
" You Have Got to be Kidding . Yawn . Yawn . Yawn . Yawn . Who thinks up these messes ? " ,1
" big city kid in a small town . amazing movie ... amazing actors ... nuff said " ,10"""
head = """                                              Review Score
0  " The first art-film ? . this is possibly the ...    10
1  " collision between the tradition of family va...    10
2  " An everyday occurrence for posterity . Louis...     4
3  " The first family film ? . Monsieur Lumi re n...     4
4  " Ouch ! That 's Got ta Hurt ! -LRB- SPOILERS ...     8"""
tail = """                                                   Review Score
233595  " Without the king . The trailer for the film ...     9
233596  " with a king . I watched your documentary sir...     1
233597  " What was the casting dept thinking ?? . Well...     2
233598  " This could be a `` so '' good movie . What f...     4
233599  " Nifty supernatural serial killer thriller . ...     8"""
head_sample = """                                              Review Score
0  " Space . It is the best Bond movie forever . ...    10
1  " defines the 80 's . this is a classic . if y...    10
2  " Great Aviation movie . That 's all I could s...    10
3  " Pure genius . . Rent . Watch . Worship . Rep...    10
4  " Yesss . The Best movie I saw in my all life ...    10"""
tail_sample = """                                               Review Score
13  " Spectacular . Spectacular , loved it ! Was L...    10
14  " A great movie . An absolute visual feast . D...    10
15  " UG . A Review ? That 's Easy . One word : PO...     3
16  " You Have Got to be Kidding . Yawn . Yawn . Y...     1
17  " big city kid in a small town . amazing movie...    10"""

with open('SAR14_sample.txt', 'w', encoding='utf-8') as f:
    f.write(SAR_sample)
PATH_1 = 'SAR14.txt'
PATH_2 = 'SAR14_sample.txt'
if not os.path.exists(PATH_2):
    raise WrongAnswer("Can't find the corpus 'SAR14.txt' in the folder.")


class UploadTheCorpusTest(StageTest):

    def generate(self):
        return [TestCase(stdin=PATH_1, attach=f'{head}\n{tail}', time_limit=0),
                TestCase(stdin=PATH_2, attach=f'{head_sample}\n{tail_sample}', time_limit=0)]

    def check(self, reply, attach):

        if len(reply.splitlines()) < len(attach.splitlines()):
            return CheckResult.wrong(f'Your program should output {len(attach.splitlines())} lines, '
                                     f'but {len(reply.splitlines())} lines were found. Make sure you printed '
                                     f'both the first five and the last five lines of the dataframe.')
        if len(reply.splitlines()) > len(attach.splitlines()):
            return CheckResult.wrong(f'Your program should output {len(attach.splitlines())} lines, '
                                     f'but {len(reply.splitlines())} lines were found.')
        if reply.strip('\n\n') not in attach:
            return CheckResult.wrong("Seems like you didn't print the required parts of the dataframe.")

        return CheckResult.correct()

    def after_all_tests(self):
        os.remove('SAR14_sample.txt')


if __name__ == '__main__':
    UploadTheCorpusTest().run_tests()
