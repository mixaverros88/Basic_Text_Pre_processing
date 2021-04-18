def count_paragraphs(txt):
    counter = 0
    previous_char = ''
    for c in txt:
        if c == '\n':
            if previous_char != '\n':
                counter += 1
        previous_char = c
    print(counter)


def count_sentences(txt):
    list_of_end_word = ['.', '!', '?']
    list_of_months = ['Feb']
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
                            counter += 1
                            print(txt[idx - 2] + '' + txt[idx - 1] + '' + txt[idx])
        previous_char = c
        if idx > 0:
            pre_previous_char = txt[idx - 1]
        if idx > 1:
            pre_pre_previous_char = txt[idx - 2]

    print(counter)


def count_words(txt):
    counter = 0
    list_of_end_word = ['\n', '\t', '\r']
    for w in txt.split(' '):
        if w not in list_of_end_word:
            counter += 1
            print(w)
            print(w.encode('raw_unicode_escape'))
    print(counter)
# def count_distinct_words():
#
#
# def remove_stop_words():
