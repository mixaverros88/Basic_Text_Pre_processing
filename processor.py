"""
Mike-George Verros
ITC6010A1 - NATURAL LANGUAGE PROCESSING - SPRING TERM 2021
HW#1
"""

from functions.functions import *

# EN File
en_file_content = get_the_content_of_a_file(get_sample_text_file_path())
file_lang = identify_lang_of_a_given_file(en_file_content)
tokenized_list = tokenization(en_file_content)
list_of_word_frequency_counts = token_frequency(tokenized_list)

results_en = [['File Lang: ' + file_lang + ', Number of paragraphs', sum_of_paragraphs(en_file_content)],
              ['File Lang: ' + file_lang + ', Number of sentences', sum_of_sentences(en_file_content)],
              ['File Lang: ' + file_lang + ', Number of words', len(tokenized_list)],
              ['File Lang: ' + file_lang + ', Number of distinct words', sum_of_distinct_word_types(tokenized_list)],
              ['File Lang: ' + file_lang + ', List of word frequency counts', list_of_word_frequency_counts],
              ['File Lang: ' + file_lang + ', Remove the stopwords', remove_stop_words(tokenized_list, file_lang)],
              ['File Lang: ' + file_lang + ', Tokens', tokenized_list],
              ]

generate_world_cloud_image(list_of_word_frequency_counts, file_lang)

# GR File
gr_file_content = get_the_content_of_a_file(get_gr_sample_text_file_path())

file_lang = identify_lang_of_a_given_file(gr_file_content)
tokenized_list_gr = tokenization(gr_file_content)
list_of_word_frequency_counts = token_frequency(tokenized_list_gr)

results_gr = [['File Lang: ' + file_lang + ', Number of paragraphs', sum_of_paragraphs(gr_file_content)],
              ['File Lang: ' + file_lang + ', Number of sentences', sum_of_sentences(gr_file_content)],
              ['File Lang: ' + file_lang + ', Number of words', len(tokenized_list_gr)],
              ['File Lang: ' + file_lang + ', Tokens', tokenized_list_gr],
              ['File Lang: ' + file_lang + ', Remove the stopwords', remove_stop_words(tokenized_list_gr, file_lang)]
              ]

generate_world_cloud_image(list_of_word_frequency_counts, file_lang)
generate_results_file(results_en + results_gr)
