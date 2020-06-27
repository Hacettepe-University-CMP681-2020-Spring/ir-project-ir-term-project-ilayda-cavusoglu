import re

cList = {
    "ain't": "am not",
    "ain’t": "am not",
    "aren’t": "are not",
    "can't": "cannot",
    "can’t": "cannot",
    "can't've": "cannot have",
    "can’t’ve": "cannot have",
    "'cause": "because",
    "’cause": "because",
    "could've": "could have",
    "could’ve": "could have",
    "couldn't": "could not",
    "couldn’t": "could not",
    "couldn't've": "could not have",
    "couldn’t’ve": "could not have",
    "didn't": "did not",
    "didn’t": "did not",
    "doesn't": "does not",
    "doesn’t": "does not",
    "don't": "do not",
    "don’t": "do not",
    "hadn't": "had not",
    "hadn’t": "had not",
    "hadn't've": "had not have",
    "hadn’t’ve": "had not have",
    "hasn't": "has not",
    "hasn’t": "has not",
    "haven't": "have not",
    "haven’t": "have not",
    "he'd": "he would",
    "he’d": "he would",
    "he'd've": "he would have",
    "he’d’ve": "he would have",
    "he'll": "he will",
    "he’ll": "he will",
    "he'll've": "he will have",
    "he’ll’ve": "he will have",
    "he's": "he is",
    "he’s": "he is",
    "how'd": "how did",
    "how’d": "how did",
    "how'd'y": "how do you",
    "how’d’y": "how do you",
    "how'll": "how will",
    "how’ll": "how will",
    "how's": "how is",
    "how’s": "how is",
    "i'd": "i would",
    "i’d": "i would",
    "i'd've": "i would have",
    "i’d’ve": "i would have",
    "i'll": "i will",
    "i’ll": "i will",
    "i'll've": "i will have",
    "i’ll’ve": "i will have",
    "i'm": "i am",
    "i’m": "i am",
    "i've": "i have",
    "i’ve": "i have",
    "isn't": "is not",
    "isn’t": "is not",
    "it'd": "it had",
    "it’d": "it had",
    "it'd've": "it would have",
    "it’d’ve": "it would have",
    "it'll": "it will",
    "it’ll": "it will",
    "it'll've": "it will have",
    "it’ll’ve": "it will have",
    "it's": "it is",
    "it’s": "it is",
    "let's": "let us",
    "let’s": "let us",
    "ma'am": "madam",
    "ma’am": "madam",
    "mayn't": "may not",
    "mayn’t": "may not",
    "might've": "might have",
    "might’ve": "might have",
    "mightn't": "might not",
    "mightn’t": "might not",
    "mightn't've": "might not have",
    "mightn’t’ve": "might not have",
    "must've": "must have",
    "must’ve": "must have",
    "mustn't": "must not",
    "mustn’t": "must not",
    "mustn't've": "must not have",
    "mustn’t’ve": "must not have",
    "needn't": "need not",
    "needn’t": "need not",
    "needn't've": "need not have",
    "needn’t’ve": "need not have",
    "o'clock": "of the clock",
    "o’clock": "of the clock",
    "oughtn't": "ought not",
    "oughtn’t": "ought not",
    "oughtn't've": "ought not have",
    "oughtn’t’ve": "ought not have",
    "shan't": "shall not",
    "shan’t": "shall not",
    "sha'n't": "shall not",
    "sha’n’t": "shall not",
    "shan't've": "shall not have",
    "shan’t’ve": "shall not have",
    "she'd": "she would",
    "she’d": "she would",
    "she'd've": "she would have",
    "she’d’ve": "she would have",
    "she'll": "she will",
    "she’ll": "she will",
    "she'll've": "she will have",
    "she’ll’ve": "she will have",
    "she's": "she is",
    "she’s": "she is",
    "should've": "should have",
    "should’ve": "should have",
    "shouldn't": "should not",
    "shouldn’t": "should not",
    "shouldn't've": "should not have",
    "shouldn’t’ve": "should not have",
    "so've": "so have",
    "so’ve": "so have",
    "so's": "so is",
    "so’s": "so is",
    "that'd": "that would",
    "that’d": "that would",
    "that'd've": "that would have",
    "that’d’ve": "that would have",
    "that's": "that is",
    "that’s": "that is",
    "there'd": "there had",
    "there’d": "there had",
    "there'd've": "there would have",
    "there’d’ve": "there would have",
    "there's": "there is",
    "there’s": "there is",
    "they'd": "they would",
    "they’d": "they would",
    "they'd've": "they would have",
    "they’d’ve": "they would have",
    "they'll": "they will",
    "they’ll": "they will",
    "they'll've": "they will have",
    "they’ll’ve": "they will have",
    "they're": "they are",
    "they’re": "they are",
    "they've": "they have",
    "they’ve": "they have",
    "to've": "to have",
    "to’ve": "to have",
    "wasn't": "was not",
    "wasn’t": "was not",
    "we'd": "we had",
    "we’d": "we had",
    "we'd've": "we would have",
    "we’d’ve": "we would have",
    "we'll": "we will",
    "we’ll": "we will",
    "we'll've": "we will have",
    "we’ll’ve": "we will have",
    "we're": "we are",
    "we’re": "we are",
    "we've": "we have",
    "we’ve": "we have",
    "weren't": "were not",
    "weren’t": "were not",
    "what'll": "what will",
    "what’ll": "what will",
    "what'll've": "what will have",
    "what’ll’ve": "what will have",
    "what're": "what are",
    "what’re": "what are",
    "what's": "what is",
    "what’s": "what is",
    "what've": "what have",
    "what’ve": "what have",
    "when's": "when is",
    "when’s": "when is",
    "when've": "when have",
    "when’ve": "when have",
    "where'd": "where did",
    "where’d": "where did",
    "where's": "where is",
    "where’s": "where is",
    "where've": "where have",
    "where’ve": "where have",
    "who'll": "who will",
    "who’ll": "who will",
    "who'll've": "who will have",
    "who’ll’ve": "who will have",
    "who's": "who is",
    "who’s": "who is",
    "who've": "who have",
    "who’ve": "who have",
    "why's": "why is",
    "why’s": "why is",
    "why've": "why have",
    "why’ve": "why have",
    "will've": "will have",
    "will’ve": "will have",
    "won't": "will not",
    "won’t": "will not",
    "won't've": "will not have",
    "won’t’ve": "will not have",
    "would've": "would have",
    "would’ve": "would have",
    "wouldn't": "would not",
    "wouldn’t": "would not",
    "wouldn't've": "would not have",
    "wouldn’t’ve": "would not have",
    "y'all": "you all",
    "y’all": "you all",
    "y'alls": "you alls",
    "y’alls": "you alls",
    "y'all'd": "you all would",
    "y’all’d": "you all would",
    "y'all'd've": "you all would have",
    "y’all’d’ve": "you all would have",
    "y'all're": "you all are",
    "y’all’re": "you all are",
    "y'all've": "you all have",
    "y’all’ve": "you all have",
    "you'd": "you had",
    "you’d": "you had",
    "you'd've": "you would have",
    "you’d’ve": "you would have",
    "you'll": "you you will",
    "you’ll": "you you will",
    "you'll've": "you you will have",
    "you’ll’ve": "you you will have",
    "you're": "you are",
    "you’re": "you are",
    "you've": "you have",
    "you’ve": "you have",
}

c_re = re.compile('(^%s$)' % '$|^'.join(cList.keys()))


def expandContractions(text, c_re=c_re):
    def replace(match):
        return cList[match.group(0)]

    return c_re.sub(replace, text.lower())
