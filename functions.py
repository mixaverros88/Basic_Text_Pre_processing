import re


def get_month_list():
    """Get a list of months """
    return ['Dec', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov']


def get_list_of_end_words():
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
    f = open(get_generated_file_path() + get_generated_file_name(), "w+")
    for i in results:
        f.write(i[0] + str(i[1]) + '\n')
    f.close()


def sanitize_string(txt):
    """This is a custom sanitizer function in order to get rid of same unneeded characters for easiest text manipulation"""
    list_with = get_list_of_end_words() + get_list_of_end_words() + ['-', ',', '\'', '"', '\n', '\t', '\r', '(', ')']
    for char in list_with:
        if char != '-' and char != '\n':
            txt = txt.replace(char, "")
        else:
            txt = txt.replace(char, " ")
    return remove_double_spaces(txt).strip()


def count_paragraphs(txt):
    """In order to count the total sum ot paragraphs we split the txt on every change line character \n"""
    counter = 1  # initialized the counter from 1 since the last paragraph is always omitted
    previous_char = ''
    for c in txt:
        if c == '\n':
            if previous_char != '\n':
                counter += 1
        previous_char = c
    return counter


def count_number_of_characters(txt):
    """Count the characters of given string"""
    return len(txt)


def count_sentences(txt):
    number_of_characters = count_number_of_characters(txt)
    list_of_end_word = get_list_of_end_words()
    list_of_months = get_month_list()
    counter = 0
    previous_char = ''
    pre_previous_char = ''
    pre_pre_previous_char = ''
    for idx, c in enumerate(txt):
        if c in list_of_end_word:
            if previous_char not in list_of_end_word and previous_char:
                if pre_previous_char not in list_of_end_word and previous_char:
                    if pre_pre_previous_char not in list_of_end_word and previous_char:
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
    return counter


def count_words(txt):
    counter = 0
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
            word = word+w
    while '' in words : words.remove('')
    while ' ' in words : words.remove(' ')
    while '\n' in words : words.remove('\n')
    print(words)
    return counter


def get_words(txt):
    return txt.split(' ')


def count_distinct_words(txt):
    return len(set(txt))


def get_stop_words_list():
    stop_words_list = open(get_english_stopwords_file_path()).read()
    return stop_words_list.split('\n')


def remove_stop_words(txt):
    stop_words_list = get_stop_words_list()
    new_list = []
    for word in get_words(txt):
        if word not in stop_words_list:
            new_list.append(word)
    return new_list


def word_frequency(txt):
    case_list = []
    for word in txt:
        if word in case_list:
            print(case.get(word))
            case_list.append(case.get(word) + 1)
        else:
            case = {'word': word, 'frequecy': 1}
        case_list.append(case)
    print(case_list)
    return case_list

