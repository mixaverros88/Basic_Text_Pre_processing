"""
Mike-George Verros
ITC6010A1 - NATURAL LANGUAGE PROCESSING - SPRING TERM 2021
HW#1
"""

import re
import matplotlib.pyplot as plt
from wordcloud import WordCloud


def get_month_list():
    """Get a list of months """
    return ['Dec', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov']


def get_list_of_punctuations():
    """Get a list of end words """
    return ['.', '!', '?']


def get_list_of_confusion_characters():
    return ['(', ')', ',']


def remove_double_spaces(txt):
    """Remove double spaces in order to tackle cases  with consecutively spaces"""
    return re.sub(' +', ' ', txt)


def get_english_stopwords_file_path():
    return 'files/englishStopwords.txt'


def get_generated_file_path():
    return 'generatedFiles/'


def get_generated_file_name():
    return 'results.txt'


def get_sample_text_file_path():
    return 'files/sample-text.txt'


def generate_results_file(results):
    """This is a function create a txt file with the results """
    generated_file = open(get_generated_file_path() + get_generated_file_name(), "w+")
    for i in results:
        generated_file.write(i[0] + str(i[1]) + '\n')
    generated_file.close()


def sanitize_string(txt):
    """This is a custom sanitizer function in order to get rid of same unneeded characters for easiest text
    manipulation """
    list_with \
        = get_list_of_punctuations() + get_list_of_punctuations() + ['-', ',', '\'', '"', '\n', '\t', '\r', '(', ')']
    for char in list_with:
        if char != '-' and char != '\n':
            txt = txt.replace(char, "")
        else:
            txt = txt.replace(char, " ")
    return remove_double_spaces(txt).strip()


def sum_of_paragraphs(txt):
    """In order to count the total sum ot paragraphs we split the txt on every change line character \n"""
    counter = 1  # initialized the counter from 1 since the last paragraph is always omitted
    previous_char = ''
    for c in txt:
        if c == '\n':
            if previous_char != '\n':  # check if the previous character is new line in order to tackle multiples lines
                counter += 1
        previous_char = c
    return counter


def count_number_of_characters(txt):
    """Count the characters of given string"""
    return len(txt)


def sum_of_sentences(txt):
    number_of_characters = count_number_of_characters(txt)
    list_of_end_word = get_list_of_punctuations()
    list_of_months = get_month_list()
    counter = 0
    previous_char = ''
    pre_previous_char = ''
    pre_pre_previous_char = ''
    for idx, c in enumerate(txt):
        if c in list_of_end_word:
            if previous_char not in list_of_end_word:
                if pre_previous_char not in list_of_end_word:
                    if pre_pre_previous_char not in list_of_end_word:
                        if (pre_pre_previous_char + pre_previous_char + previous_char) not in list_of_months:
                            if idx + 1 < number_of_characters:
                                if txt[idx + 1] not in list_of_end_word:
                                    counter += 1
                                    # print(txt[idx - 2] + '' + txt[idx - 1] + '' + txt[idx])
                            else:
                                counter += 1
                                # print(txt[idx - 2] + '' + txt[idx - 1] + '' + txt[idx])
        previous_char = c
        if idx > 0:
            pre_previous_char = txt[idx - 1]
        if idx > 1:
            pre_pre_previous_char = txt[idx - 2]
    print('sum_of_sentences: ', counter)
    return counter


def sum_of_words(txt):
    list_of_p = ['(', ')', ',', ':', '!', ' ', '\n', '.']
    words = []
    word = ''
    for w in txt:
        if any(w in s for s in list_of_p):
            if word != '':
                words.append(word)
            words.append(w)
            word = ''
        else:
            word = word + w
    while '' in words: words.remove('')
    while ' ' in words: words.remove(' ')
    while '\n' in words: words.remove('\n')
    while '.' in words: words.remove('.')
    while ',' in words: words.remove(',')
    while ':' in words: words.remove(':')
    while '!' in words: words.remove('!')
    while '(' in words: words.remove('(')
    while ')' in words: words.remove(')')
    print(words)
    print('sum_of_words: ', len(words))

    return len(words)


def tokenization(txt):
    list_of_p = ['(', ')', ',', ':', '!', ' ', '\n', '.']
    words = []
    word = ''
    for w in txt:
        if any(w in s for s in list_of_p):
            if word != '':
                words.append(word)
            words.append(w)
            word = ''
        else:
            word = word + w
    while '' in words: words.remove('')
    while ' ' in words: words.remove(' ')
    while '\n' in words: words.remove('\n')
    return words


def get_words(txt):
    print('get_words: ', txt.split(' '))
    return txt.split(' ')


def sum_of_distinct_words(txt):
    print('sum_of_distinct_words: ', len(set(tokenization(txt))))
    return len(set(tokenization(txt)))


def get_stop_words_list():
    stop_words_list = open(get_english_stopwords_file_path()).read()
    return stop_words_list.split('\n')


def remove_stop_words(txt):
    stop_words_list = get_stop_words_list()
    new_list = []
    for word in get_words(txt):
        if word not in stop_words_list:
            new_list.append(word)
    print('remove_stop_words: ', new_list)
    return new_list


# https://stackoverflow.com/questions/62918528/sort-dict-or-list-by-second-value-of-the-tuple-and-then-by-the-first-one
def order_dictionary(data):
    return sorted(data.items(), key=lambda x: (x[1], [-ord(letter) for letter in x[0]]), reverse=True)


def word_frequency(txt):
    word_frequency_list = {}
    for w in txt:
        if not word_frequency_list.__contains__(w):
            d = {w: 1}
            word_frequency_list.update(d)
        else:
            count = word_frequency_list.pop(w) + 1
            d = {w: count}
            word_frequency_list.update(d)
    print('word_frequency:', order_dictionary(word_frequency_list))
    return order_dictionary(word_frequency_list)


def generate_world_cloud(word_list):
    word_list = [f[0] for f in word_list][:50]  # convert a list of dictionaries to a list of strings
    unique_string = " ".join(word_list)  # convert list to string and generate
    word_cloud = WordCloud(width=1000, height=500).generate(unique_string)
    plt.figure(figsize=(15, 8))
    plt.imshow(word_cloud)
    plt.axis('off')
    plt.savefig(get_generated_file_path() + 'word_cloud' + '.png', bbox_inches='tight')
    plt.close()
