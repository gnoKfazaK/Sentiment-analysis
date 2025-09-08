from nltk.corpus import wordnet
import nltk
from nltk.tokenize import RegexpTokenizer

nltk.download('wordnet')


def dictionary(seed):
    for syn in wordnet.synsets(seed):
        for l in syn.lemmas():
            if(not (l.name() in synonyms)):
                synonyms.append(l.name())
            if l.antonyms():
                if(not(l.antonyms() in antonyms)):
                    antonyms.append(l.antonyms()[0].name())


def dictionary500():
    # print("Hello")
    for i in synonyms:
        # print("Not done")
        if len(antonyms) + len(synonyms) >= 500:
            # print("Done")
            # print(str(len(antonyms)) + " " + str(len(synonyms)))
            break
        dictionary(i)

if __name__ == "__main__":
    word = input("Please input a positive word: ")
    synonyms = []
    antonyms = []
    dictionary(word)
    print("Positive word: ")
    print(set(synonyms))
    print("Negative word: ")
    print(set(antonyms))
    print("\n")
    dictionary500()


    tokenizer = RegexpTokenizer(r'\w+')
    with open('1155176931.txt', 'r', encoding="utf8") as f:
        for i in range(15):
            score = 0
            line = tokenizer.tokenize(f.readline().strip("\n"))
            for j in line:
                if j in synonyms:
                    score += 1
                elif j in antonyms:
                    score -= 1

            score /= len(line)
            print("s(d)of line " + str(i + 1) + " = " + str(score))








