from collections import Counter
from zipfile import ZipFile
import re

kWORDS = re.compile("[a-z]{4,}")

def text_from_zipfile(zip_file):
    """
    Given a zip file, yield an iterator over the text in each file in the
    zip file.
    """

    with ZipFile(zip_file) as myzip:
        for name in myzip.namelist():
            if '.txt' in name:
                with myzip.open(name) as myfile:
                    for line in myfile:
                        try:
                            line = line.decode('UTF-8')
                        except UnicodeDecodeError:
                            pass
                        yield line
    # Modify this function

def words(text):
    """
    Return all words in a string, where a word is four or more contiguous
    characters in the range a-z or A-Z.  The resulting words should be
    lower case.
    """
    textmod = []
    for word in text.lower().split():
        word = str(word)
    # textmod = text.lower().split()
    # print(textmod)
        for letter in word:
            if not letter.isalpha():
                word = word.replace(letter, '')
                              #hack: workaround for bthe, which gets past
                              #decoding from bytes to string somehow
        if len(word) >= 4 and word != 'bthe':
            textmod.append(word)
            #print('yes')
            # del(textmod[i])

    # Modify this function
    return textmod

def accumulate_counts(words, total=Counter()):
    """
    Take an iterator over words, add the sum to the total, and return the
    total.

    @words An iterable object that contains the words in a document
    @total The total counter we should add the counts to
    """
    assert isinstance(total, Counter)

    for word in words:
        total[word] += 1
    # Modify this function
    return total

if __name__ == "__main__":
    # You should not need to modify this part of the code
    total = Counter()
    for tt in text_from_zipfile("../data/state_union.zip"):
        total = accumulate_counts(words(tt), total)

    for ii, cc in total.most_common(100):
        print("%s\t%i" % (ii, cc))

    #text_from_zipfile('../data/state_union.zip')
    #print(accumulate_counts(words("This! is an an the! idiot idiot sentence. 12345")))
