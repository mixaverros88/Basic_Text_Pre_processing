"""
Mike-George Verros
ITC6010A1 - NATURAL LANGUAGE PROCESSING - SPRING TERM 2021
HW#1
"""

import re
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from collections import Counter
import string
from langdetect import detect


def get_month_list():
    """
    :return: A list of months Abbreviation
    """
    return ['Dec', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov']


def get_list_of_end_sentence_character():
    """
    :return: A list of end punctuation characters
    """
    return ['.', '!', '?']


def identify_lang_of_a_given_file(file_content):
    lang = detect(file_content)
    print('Lang of given text: ', lang)
    return lang.upper()


def remove_double_spaces(text):
    """
    Remove double spaces in order to tackle cases with consecutively spaces
    :param text:
    :return: The given text without consecutively spaces
    """
    return re.sub(' +', ' ', text)


def get_english_stopwords_file_path():
    """
    :return: Returns a file path
    """
    return 'files/englishStopwords.txt'


def get_greek_stopwords_file_path():
    """
    :return: Returns a file path
    """
    return 'files/stop_words_greek.txt'


def get_generated_file_path():
    """
    :return: Returns a folder path
    """
    return 'generatedFiles/'


def get_generated_file_name():
    """
    :return: Returns a file name
    """
    return 'results.txt'


def get_sample_text_file_path():
    """
    :return: Returns a file path
    """
    return 'files/sample-text.txt'


def get_gr_sample_text_file_path():
    """
    :return: Returns a file path
    """
    return 'tests/files/greek_sample.txt'


def generate_results_file(results_list_of_lists):
    """
    Create a txt file with the results from given list
    :param results_list_of_lists: Every nested list contains 2 items the first is a string that
     indicates the task and the other item is the result e.g. [Number of paragraphs : 8]
    """
    alphabet_char_list = string.ascii_lowercase
    generated_file = open(get_generated_file_path() + get_generated_file_name(), "w+", encoding="utf-8")
    for idx, i in enumerate(results_list_of_lists):
        generated_file.write(alphabet_char_list[idx] + '. ' + i[0] + ' : ' + str(i[1]) + '\n')
    generated_file.close()


def sum_of_paragraphs(text):
    """In order to count the total sum of paragraphs we check the text on every change line character \n, and increase
    the counter by 1"""
    counter = 1  # initialized the counter from 1 since the last paragraph is always omitted
    previous_char = ''
    for char in text:
        if char == '\n':
            # check if the previous character is new line in order to tackle multiples lines separators
            if previous_char != '\n':
                counter += 1
        previous_char = char
    print('sum_of_paragraphs: ', counter)
    return counter


def count_number_of_characters(text):
    """
    Count the total characters of given string
    :param text:
    :return: The sum of characters of a given string
    """
    return len(text)


def sum_of_sentences(text):
    """In order to count the total sum of sentences we check the text on every end of sentence character like '., !, ?'
    and we found this character we also check the previous and the following characters in order to tackle some cases
    like ..., Feb."""
    number_of_characters = count_number_of_characters(text)
    list_of_end_word = get_list_of_end_sentence_character()
    list_of_months = get_month_list()
    counter = 0
    previous_char = ''
    pre_previous_char = ''
    pre_pre_previous_char = ''
    for idx, char in enumerate(text):
        if char in list_of_end_word:
            if previous_char not in list_of_end_word:
                if pre_previous_char not in list_of_end_word:
                    if pre_pre_previous_char not in list_of_end_word:
                        if (pre_pre_previous_char + pre_previous_char + previous_char) not in list_of_months:
                            if idx + 1 < number_of_characters:
                                if text[idx + 1] not in list_of_end_word:
                                    counter += 1
                                    # print(txt[idx - 2] + '' + txt[idx - 1] + '' + txt[idx])
                            else:
                                counter += 1
                                # print(txt[idx - 2] + '' + txt[idx - 1] + '' + txt[idx])
        previous_char = char
        if idx > 0:
            pre_previous_char = text[idx - 1]
        if idx > 1:
            pre_pre_previous_char = text[idx - 2]
    print('sum_of_sentences: ', counter)
    return counter


def get_additional_contractions():
    """
    :return: a list of additional contractions
    """
    return [
        ['won', 'will'],
        ['Won', 'will'],
        ['can', 'can'],
        ['Can', 'can']
    ]


def get_contractions():
    """
    :return: a list of contractions
    """
    return [
        ['ll', 'will'],
        ['ve', 'have'],
        ['d', 'would'],
        ['t', 'not'],
        ['re', 'are'],
        ['m', 'am'],
        ['s', 'is']
    ]


def tokenization(text):
    """In order to perform tokenization to a given text
    1. We iterate in every character
    2. If this character is not in list called list_of_punctuations_and_more then we add the character into variable
    word
    3. But if the character is on list
        4.and doesn't have ''' character we add the word in the words array
        5.Otherwise, we split the word by the ''' character and we check if the right side of splitted word is
        on contraction's list
            6.If yes we check if the contractions have t char in order to tackle the negative cases
            7.Otherwise, we add the two words in the list of words.

    :return: a list of tokens
    """
    list_of_punctuations_and_more = ['(', ')', ',', ':', '!', ' ', '\n', '.', '']
    tokens = []
    token = ''
    for idx, character in enumerate(text):
        if any(character in s for s in list_of_punctuations_and_more):
            if '\'' in token:
                splitted_word = token.split('\'')
                for contraction in get_contractions():
                    if contraction[0] == splitted_word[1]:
                        if contraction[0] == 't':
                            is_on_list = True
                            for additional_contraction in get_additional_contractions():
                                if additional_contraction[0] == splitted_word[0]:
                                    tokens.append(additional_contraction[1])
                                    is_on_list = False
                            if is_on_list:
                                tokens.append(splitted_word[0][:-1])
                                tokens.append(contraction[1])
                        else:
                            tokens.append(splitted_word[0])
                            tokens.append(contraction[1])
            else:
                tokens.append(token)
            tokens.append(character)
            token = ''
        else:
            token = token + character

    unwanted_characters = {'', ' ', '\n'}
    tokens = [ele for ele in tokens if ele not in unwanted_characters]  # remove unwanted characters
    print('Tokens: ', tokens)
    return tokens


def get_stop_words_list(lang_of_file):
    """
    :return: Returns a list with stop words extracted from a file
    """
    stop_words_list = ''
    if lang_of_file == 'EN':
        stop_words_list = get_the_content_of_a_file(get_english_stopwords_file_path())
    elif lang_of_file == 'EL':
        stop_words_list = get_the_content_of_a_file(get_greek_stopwords_file_path())
    return stop_words_list.split('\n')


def remove_stop_words(tokenized_list, lang_of_file):
    """
    This function takes a list with token return a list without some stop words form get_stop_words_list() list
    :param lang_of_file:
    :param tokenized_list: A list of tokens e.g. ['Here', 'are', 'some', 'random']
    :return: A list with the token from given tokenized_list except the words from get_stop_words_list()
    """
    stop_words_list = get_stop_words_list(lang_of_file)
    new_word_list_without_excluded_words = []
    for word in tokenized_list:
        if word not in stop_words_list:
            new_word_list_without_excluded_words.append(word)
    print('remove_stop_words: ', new_word_list_without_excluded_words)
    return new_word_list_without_excluded_words


def order_dictionary(dictionary):
    """
    This function takes a dictionary e.g. {'Here': 1, 'some': 1, 'random': 1} and order it
    :param dictionary: A list of tokens along with the sum o occurrences
    :return: a dictionary most often occurrences in the descending order and if and words which have the same frequency
    count are ordered by lexicographical
    """
    return sorted(dictionary.items(), key=lambda x: (x[1], [-ord(letter) for letter in x[0]]), reverse=True)


def token_frequency(tokenized_list):
    """
    This function takes a list of tokens e.g. ['Here', 'are', 'some', 'random'],
    and creates a dictionary which consist of every token the total number of occurrences
    e.g. {'Here': 1, 'some': 1, 'random': 1}
    After the creation of dictionary calls the order_dictionary() which orders the dictionary by to most often
    occurrences in the descending order and if and words which have the same frequency count are ordered by
    lexicographical order e.g. [('.', 35), ('the', 21), (',', 17), ('is', 14), ('I', 13)]

    :param tokenized_list: A list of tokens e.g. ['Here', 'are', 'some', 'random']
    :return: a dictionary most often occurrences in the descending order and if and words which have the same frequency
    count are ordered by lexicographical
    """

    word_frequency_dictionary = {}
    for token in tokenized_list:
        if not word_frequency_dictionary.__contains__(token):
            dictionary = {token: 1}
            word_frequency_dictionary.update(dictionary)
        else:
            count = word_frequency_dictionary.pop(token) + 1
            dictionary = {token: count}
            word_frequency_dictionary.update(dictionary)
    returned_dict = order_dictionary(word_frequency_dictionary)
    print('token_frequency: ', returned_dict)
    return returned_dict


def get_list_of_taggers():
    """
    :return: A list of regex and the respectively identifier
    """
    return [
        ["^-?[0-9]+(.[0-9]+)?$", 'CD'],
        ["(The|the|A|a|An|an)$", 'AT'],
        [".*able$", 'JJ'],
        [".*ness$", 'NN'],
        [".*ly$", 'RB'],
        [".*s$", 'NNS'],
        [".*ing$", 'VBG'],
        [".*ed$", 'VBD'],
        [".*", 'NN']
    ]


def identify_word_type(tokenized_list):
    """
    :param tokenized_list: A list of tokens e.g. ['Here', 'are', 'some', 'random']
    :return: A dictionary with labeled every word e.g. Here : NN
    """
    word_frequency_dictionary = {}
    for word in tokenized_list:
        for tagger_regex_and_identifier in get_list_of_taggers():
            if re.search(tagger_regex_and_identifier[0], word):
                dictionary = {word: tagger_regex_and_identifier[1]}
                word_frequency_dictionary.update(dictionary)
                break
    print('Word Type: ', word_frequency_dictionary)
    return word_frequency_dictionary


def sum_of_distinct_word_types(tokenized_list):
    """
    :param tokenized_list: A list of tokens e.g. ['Here', 'are', 'some', 'random']
    :return: A list with every type of word and the sum of instances
    """
    word_frequency_list = identify_word_type(tokenized_list)
    list_of_pos = []
    for value in word_frequency_list:
        list_of_pos.append(word_frequency_list[value])
    print('sum_of_distinct_word_types: ', Counter(list_of_pos))
    return Counter(list_of_pos)


def generate_world_cloud_image(list_of_word_frequency_counts, lang_of_file):
    """
    This function takes a dictionary which consists of a token and the sum of frequency,
    e.g. [('.', 35), ('the', 21), (',', 17), ('is', 14), ('I', 13)]
    from this dictionary get the top 50 occurred token and generated a word cloud image
    :param lang_of_file:
    :param list_of_word_frequency_counts:
    """
    print('list_of_word_frequency_counts', list_of_word_frequency_counts)
    # convert a list of dictionaries to a list of strings
    word_list = [f[0] for f in list_of_word_frequency_counts][:50]
    unique_string = " ".join(word_list)  # convert list to string and generate
    word_cloud = WordCloud(width=1000, height=500).generate(unique_string)
    plt.figure(figsize=(15, 8))
    plt.imshow(word_cloud)
    plt.axis('off')
    plt.savefig(get_generated_file_path() + 'word_cloud_' + lang_of_file + '.png', bbox_inches='tight')
    plt.close()


def get_the_content_of_a_file(file_path):
    """
    Takes a file path and returns the content of this file
    :param file_path:
    :return:
    """
    return open(file_path, encoding="utf8").read()
