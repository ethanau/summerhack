import requests
import pandas as pd

API_URL = 'https://api.dictionaryapi.dev/api/v2/entries/en/'


def word_interpreter(ielts_word):
    response = requests.get(API_URL + ielts_word)
    interpretation = response.json()
    meaning = interpretation[0]['meanings'][0]['definitions'][0]['definition']
    return meaning


ielts_words = pd.read_csv("data/ielts_words_list.csv")
ielts_words_list = ielts_words['word'].tolist()

words_meaning_list = [word_interpreter(word) for word in ielts_words_list]

words_dict = {
    'word': ielts_words_list,
    'meaning': words_meaning_list
}

pd.DataFrame(data=words_dict).to_csv("data/ielts_words_list.csv", index=False)

data = pd.read_csv("data/ielts_words_list.csv")
words_list = data['word'].to_list()
meaning_list = data['meaning'].to_list()

new_meaning_list = [word.replace('"', '') for word in meaning_list]
print(new_meaning_list)
words_dict = {
    'word': words_list,
    'meaning': new_meaning_list
}

pd.DataFrame(data=words_dict).to_csv("data/ielts_words_list.csv", index=False)
